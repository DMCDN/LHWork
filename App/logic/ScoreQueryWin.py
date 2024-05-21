
from PyQt6 import QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QHeaderView, QPushButton
from PyQt6.QtGui import *
from GUI.Ui_Dialog_ScoreQuery import Ui_ScoreQuery
from GUI.Ui_Dialog_ScoreQuery_GlobalStdData import Ui_ScoreQuery_GlobalStdData
import hashlib
import requests
import json
import zstandard as zstd

class ScoreQuery(QtWidgets.QMainWindow, Ui_ScoreQuery):
    def __init__(self, parent=None,lhuAuth=None):
        super(ScoreQuery, self).__init__(parent)
        self.setupUi(self)
        self.action()
        self.lhuAuth=lhuAuth
        self.GlobalStdData=None
        self.btnScoreQuery_OnClick()
        self.filterText.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.filterText and isinstance(event, QKeyEvent):
            #阻止按enter時 真的把換行打進去 順便重新觸發filterTable
            if event.key() == Qt.Key.Key_Return:
                self.filterTable()
                return True 
        return super().eventFilter(obj, event)
    
    def action(self):
        self.btnPoint1.clicked.connect(self.showDT1)
        self.btnPoint2.clicked.connect(self.showDT2)
        self.btnPoint3.clicked.connect(self.showDT3)
        self.btnUnPass.clicked.connect(self.showDTUnPass)
        self.btnPointAll.clicked.connect(self.showDTAll)
        self.filterText.textChanged.connect(self.filterTable)
        self.btnGlobalPassRate.clicked.connect(self.btnGlobalPassRate_OnClick)

    def btnGlobalPassRate_OnClick(self):
        self.GlobalPassRateWin = ScoreQuery_GlobalStdData(self,self.GlobalStdData)
        self.GlobalPassRateWin.show()
    
    def btnScoreQuery_OnClick(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()


        msgBox = QMessageBox()
        msgBox.setWindowTitle("DEBUG")
        msgBox.setText("匹配方式")

        buttonA = QPushButton("配當表")
        buttonB = QPushButton("SQL")

        msgBox.addButton(buttonA, QMessageBox.ButtonRole.YesRole)
        msgBox.addButton(buttonB, QMessageBox.ButtonRole.NoRole)

        msgBox.exec()
        if msgBox.clickedButton() == buttonA:
            DT_ScoreQuery=self.lhuAuth.DT_ScoreQuery_V2() 
        elif msgBox.clickedButton() == buttonB:
            DT_ScoreQuery=self.lhuAuth.DT_ScoreQuery_V2_SQL() 
            self.startUpload(DT_ScoreQuery["ScoreDataDict"])
           
        ScoreDataDict2=DT_ScoreQuery['ScoreDataDict2']
        FBIWarningText=DT_ScoreQuery['FBIWarningText']
        Score=DT_ScoreQuery['Score']
        point1=DT_ScoreQuery['point1']
        point2=DT_ScoreQuery['point2']
        point3=DT_ScoreQuery['point3']
        pointS1=DT_ScoreQuery['pointS1']
        pointS1BlackList=DT_ScoreQuery['pointS1BlackList']
        ScoreDataDict_ALL=DT_ScoreQuery['ScoreDataDict']

        self.loadingDialog.close()
        if FBIWarningText:
            self.loadingDialog.setWindowTitle("FBI WARNING!!!")
            self.loadingDialog.setText(FBIWarningText)
            self.loadingDialog.setStyleSheet('color: rgb(0, 0, 0);')
            self.loadingDialog.show()

        self.show()

        self.textBrowser.setText(f"""
        應修學分:{Score}/128 學分\n
        校(選擇性)必修、院訂必修:{point1}/36 學分\n 
        院、系專業必修:{point2}/68 學分\n
        系專業選修:{point3}/24 學分\n
        通職:{pointS1}/4 通過項目 (已過:{pointS1BlackList})
        
        \n
        ScoreDataDict_ALL:{ScoreDataDict_ALL}
        \n
        ScoreDataDict2:{ScoreDataDict2}
        """)

        self.currentData = ScoreDataDict2



    def showDT1(self):
        self.fillTableWithData(self.currentData.get("校選修_校必修_院訂必修_校選擇性必修", {}))
        self.filterTable()
    def showDT2(self):
        self.fillTableWithData(self.currentData.get("系專業必修_院專業必修", {}))
        self.filterTable()
    def showDT3(self):
        self.fillTableWithData(self.currentData.get("系專業選修", {}))
        self.filterTable()
    def showDTUnPass(self):
        self.fillTableWithData(self.currentData.get("未通過", {}))
        self.filterTable()

    def showDTAll(self):
        all_data = []
        for key, value in self.currentData.items():
            all_data.extend(value)
        self.fillTableWithData(all_data)


    def fillTableWithData(self, data):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["學期", "課號", "科目名稱", "學分", "成績"])

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        row = 0
        for course in data:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(course["學年-學期"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(course["課號"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(course["科目名稱"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(course["學分"])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(course["成績"])))
            row += 1

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortByColumn(4, Qt.SortOrder.DescendingOrder)


    def filterTable(self):
        text = self.filterText.toPlainText().strip()
        if not text:
            # text為空 顯示所有data
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(row, False)
        else:

            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 2)  # 科目名稱 row 2
                if item and text.lower() in item.text().lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)


    def LogText_Update(self, value):
        #print(value)
        if value:
            self.GlobalStdData = value
            self.btnGlobalPassRate.setEnabled(True)
            self.btnGlobalPassRate.setText('查詢各科通過率')
        else:
            self.btnGlobalPassRate.setText('伺服器錯誤')

    def startUpload(self, ScoreDataDict):
        self.worker_thread = WorkerThread(ScoreDataDict,self.lhuAuth.UserID)
        self.worker_thread.LogText.connect(self.LogText_Update)
        self.worker_thread.start()

class WorkerThread(QThread):
    LogText = pyqtSignal(list)
    
    def __init__(self, ScoreDataDict,UserID):
        super().__init__()
        self.UserID = UserID
        self.ScoreDataDict=ScoreDataDict
        self.HashFilePath = 'ScoreDataRecord.txt' 

    def GetMd5(self):
        newHash = hashlib.md5(json.dumps(self.ScoreDataDict).encode('utf-8')).hexdigest()
        with open(self.HashFilePath, 'w') as f:
            f.write(newHash)
        return(newHash)

    def LoadMd5(self):
        try:
            with open(self.HashFilePath, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def run(self):

        try:
            #資料寫入server
            r = requests.get('https://raw.githubusercontent.com/DMCDN/assets/main/ThirdUrl')
            ThirdUrl=r.json()
            Global_StdDataURL=ThirdUrl["Global_StdDataURL"]

            old_md5 = self.LoadMd5()
            new_md5 = self.GetMd5()

            if old_md5 != new_md5 or not old_md5: #新舊不匹配 / 無紀錄文件
                headers = {'Content-Type': 'application/json'}
                data = {
                    'ScoreDataDict': self.ScoreDataDict,
                    'StdID': self.UserID
                }
                r = requests.post(Global_StdDataURL, data=json.dumps(data), headers=headers)
                if r.status_code == 200:
                    print('Post完成')
                else:
                    print(f'Post錯誤:{r.status_code}|{r.text}')
                    self.LogText.emit([])

            else:
                print('Post完成(無更動)')

            #讀取server資料
            r = requests.get(Global_StdDataURL)
            if r.status_code == 200:
                if r.headers.get('Content-Encoding') == 'zstd':
                    dctx = zstd.ZstdDecompressor()
                    data = dctx.decompress(r.content)
                    result = json.loads(data.decode('utf-8'))
                    print(r.content)
                    self.LogText.emit(result)
                else:
                    print(r.text)
            else:
                print(f'Get錯誤:{r.status_code}|{r.text}')
                self.LogText.emit([])

        except Exception as e :
           print(f'錯誤：{e}')
           self.LogText.emit([])



from collections import defaultdict

class ScoreQuery_GlobalStdData(QtWidgets.QMainWindow, Ui_ScoreQuery_GlobalStdData):
    def __init__(self, parent=None,GlobalStdData=None):
        super(ScoreQuery_GlobalStdData, self).__init__(parent)
        self.setupUi(self)
        self.GlobalStdData=GlobalStdData
        self.action()
        self.filterText.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.filterText and isinstance(event, QKeyEvent):
            #阻止按enter時 真的把換行打進去 順便重新觸發filterTable
            if event.key() == Qt.Key.Key_Return:
                self.filterTable()
                return True 
        return super().eventFilter(obj, event)
    
    def action(self):
        data = self.GlobalStdData
        
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['課號', '課程名稱', '平均分數', '通過率', '不通過率', '壓線通過率(目前範圍:60~65)', '資料總數'])

        for i, item in enumerate(data):
            ClassID = item["ClassID"]
            ClassName = item["ClassName"]
            ScoreList = item["ScoreList"]
            
            # 平均
            Score_AVG = sum(ScoreList) / len(ScoreList)
            # 通過率
            PassRate = len([score for score in ScoreList if score >= 60]) / len(ScoreList) * 100
            UnPassRate = len([score for score in ScoreList if score < 60]) / len(ScoreList) * 100
            #PassRate_str = f"{PassRate:.2f}%" if PassRate % 1 != 0 else f"{int(PassRate)}%" #無小數則顯示整數
            print(len([score for score in ScoreList if 60 <= score <= 70]),PassRate)
            # 壓線通過數量 60-65
            if PassRate == 0:
                borderlinePassRate = 0
            else:
                borderlinePassRate = len([score for score in ScoreList if 60 <= score <= 65]) / len(ScoreList) * 100

            # 資料總數
            ScoreList_Len = len(ScoreList)
            
 
            self.tableWidget.setItem(i, 0, QTableWidgetItem(ClassID))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(ClassName))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(f"{Score_AVG:.2f}"))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(f"{PassRate:.2f}%"))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(f"{UnPassRate:.2f}%"))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(f"{borderlinePassRate:.1f}%"))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(ScoreList_Len)))

        # 調整tableWidget大小
        self.tableWidget.resizeColumnsToContents()

        self.filterText.textChanged.connect(self.filterTable)


    def filterTable(self):
        text = self.filterText.toPlainText().strip()
        if not text:
            # text為空 顯示所有data
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(row, False)
        else:

            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 1)  # 科目名稱 row 1
                if item and text.lower() in item.text().lower():
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)

