
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QListWidget,QHeaderView,QPushButton
from PyQt6.QtGui import *

from GUI.Ui_Dialog_LaoZuo import Ui_LaoZuo
from GUI.Ui_Dialog_LaoZuo_Apply import Ui_LaoZuo_Apply
from GUI.Ui_Dialog_LaoZuo_ApplyReserve import Ui_LaoZuo_ApplyReserve
from bs4 import BeautifulSoup

import sqlite3

conn = sqlite3.connect('SQL/LaborApplyReserve.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Labors
             (id INTEGER PRIMARY KEY AUTOINCREMENT, szUrl TEXT, szMTime TEXT, szTitle TEXT, szStartApplyDate TEXT, 
             szStopApplyDate TEXT, szHours TEXT, iMaxNum INTEGER, iCurrNum INTEGER, szBtnText TEXT, 
             szCollectionTimePlace TEXT, szActivityPlace TEXT, szContent TEXT, szNote TEXT, bSuccess INTEGER)''')
conn.commit()

def checkDTExist(title, start_apply_date):
    c.execute("SELECT * FROM Labors WHERE szTitle = ? AND szStartApplyDate = ?", (title, start_apply_date))
    result = c.fetchone()
    if result:
        return True
    else:
        return False

def writeDT(data):
    if not checkDTExist(data['szTitle'], data['szStartApplyDate']):
        c.execute('''INSERT INTO Labors (szUrl, szMTime, szTitle, szStartApplyDate, szStopApplyDate, szHours, iMaxNum, 
                    iCurrNum, szBtnText, szCollectionTimePlace, szActivityPlace, szContent, szNote, bSuccess)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (data['szUrl'], data['szMTime'], data['szTitle'], data['szStartApplyDate'], data['szStopApplyDate'],
                    data['szHours'], data['iMaxNum'], data['iCurrNum'], data['szBtnText'], data['集合時間_地點'],
                    data['活動地點'], data['勞作教育內容'], data['勞作教育注意事項'], 0))
        conn.commit()
        return True
    else:
        return False

def dropDT(data):
    c.execute("DELETE FROM Labors WHERE szTitle = ? AND szStartApplyDate = ?", (data['szTitle'], data['szStartApplyDate']))
    conn.commit()


class LaoZuo(QtWidgets.QMainWindow, Ui_LaoZuo):
    def __init__(self, parent=None,lhuAuth=None):
        super(LaoZuo, self).__init__(parent)
        self.setupUi(self)
        self.action()

        self.lhuAuth=lhuAuth
        self.startSearch()

    def action(self):
        self.btnLaoZuoApply.clicked.connect(self.btnLaoZuoApply_OnClick)

    def startSearch(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        LaoZuoRecordDict=self.lhuAuth.getPage_LaoZuo() 
        self.loadingDialog.close()


        #LaoZuoRecordDict
        #{'iLastTime1': 12, 'bIsPracticed1': False, 'bIsFeedbacked1': False, 
        # 'iLastTime2': 12, 'bIsPracticed2': False, 'bIsFeedbacked2': False}
        LZ1_Status=""
        LZ1_StatusIco=""
        if LaoZuoRecordDict['bIsPracticed1'] and LaoZuoRecordDict['bIsFeedbacked1']: #1&1
            LZ1_Status="已完成"
            LZ1_StatusIco="🟢"
        elif LaoZuoRecordDict['bIsPracticed1'] and (LaoZuoRecordDict['bIsFeedbacked1'] == False): #1&0
            LZ1_Status="勞作時數已滿，但心得尚未填寫"
            LZ1_StatusIco="🔴"
        elif (LaoZuoRecordDict['bIsPracticed1'] == False) and LaoZuoRecordDict['bIsFeedbacked1']: #0&1
            LZ1_Status="心得已填寫，但勞作時數未達標"
            LZ1_StatusIco="🔴"
        else:
            LZ1_Status="未完成"
            LZ1_StatusIco="🔴"

        LZ2_Status=""
        LZ2_StatusIco=""
        if LaoZuoRecordDict['bIsPracticed2'] and LaoZuoRecordDict['bIsFeedbacked2']: #1&1
            LZ2_Status="已完成"
            LZ2_StatusIco="🟢"
        elif LaoZuoRecordDict['bIsPracticed2'] and (LaoZuoRecordDict['bIsFeedbacked2'] == False): #1&0
            LZ2_Status="勞作時數已滿，但心得尚未填寫"
            LZ2_StatusIco="🔴"
        elif (LaoZuoRecordDict['bIsPracticed2'] == False) and LaoZuoRecordDict['bIsFeedbacked2']: #0&1
            LZ2_Status="心得已填寫，但勞作時數未達標"
            LZ2_StatusIco="🔴"
        else:
            LZ2_Status="未完成"
            LZ2_StatusIco="🔴"

        
        
        self.textBrowser.setText(f"""
        {LZ1_StatusIco}勞作教育(一)：{LZ1_Status}\n
        \t  已完成時數：{12 - LaoZuoRecordDict["iLastTime1"]}/12 \n
        \t  心得填寫狀態：{LaoZuoRecordDict["szFeedbackedStatus1"]} \n
        {LZ2_StatusIco}勞作教育(二)：{LZ2_Status}\n
        \t  已完成時數：{12 - LaoZuoRecordDict["iLastTime2"]}/12 \n
        \t  心得填寫狀態：{LaoZuoRecordDict["szFeedbackedStatus2"]} \n

        \n
        LaoZuoRecordDict:{LaoZuoRecordDict}
        """)

        if LZ1_StatusIco == "🟢" and LZ2_StatusIco == "🟢":
            self.Label_Status.setText("勞作教育已完成！")
            self.btnLaoZuoApply.setEnabled(False)
            self.btnLaoZuoApply.setText("已完成勞作不提供查詢")
        else:
            self.Label_Status.setText("勞作教育未完成！")

    def btnLaoZuoApply_OnClick(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        LaoZuoApplyDict=self.lhuAuth.getPage_LaborApply() 

        self.loadingDialog.close()

        LaoZuo_Apply(self,LaoZuoApplyDict,self.lhuAuth).show()



class LaoZuo_Apply(QtWidgets.QMainWindow, Ui_LaoZuo_Apply):
    def __init__(self, parent=None,LaoZuoApplyDict=None,lhuAuth=None):
        super(LaoZuo_Apply, self).__init__(parent)
        self.setupUi(self)
        self.action()
        self.bShowMidd = True
        self.bShowPM = True
        self.bShowOther = True
        self.bFilterFull=False

        
        self.lhuAuth=lhuAuth
        self.LaoZuoApplyDict=LaoZuoApplyDict
        self.startSearchV2()
        self.tmpDialog = QMessageBox(self)
        self.tmpDialog.setStyleSheet("QLabel{ color: black}")
        self.tmpDialog.setWindowTitle("提示")
        self.tmpDialog.addButton(QMessageBox.StandardButton.Ok)  
        self.joinFlag = False 

    def msgbox_Question(self, title, infoText):
        reply = QMessageBox.question(
            self, title, infoText,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.No:
            return False
        if reply == QMessageBox.StandardButton.Yes:
            return True
        
    def msgbox(self,title,infoText):
        self.msgboxDefault = QMessageBox(self)
        self.msgboxDefault.setStyleSheet("QLabel{ color: black}")
        self.msgboxDefault.setWindowTitle(title)
        self.msgboxDefault.setText(infoText)
        self.msgboxDefault.show()



    def action(self):
        self.checkBox_bShowMidd.clicked.connect(self.onCheckBoxClick_bShowMidd)
        self.checkBox_bShowPM.clicked.connect(self.onCheckBoxClick_bShowPM)
        self.checkBox_bShowOther.clicked.connect(self.onCheckBoxClick_bShowOther)
        self.checkBox_bFilterFull.clicked.connect(self.onCheckBoxClick_bFilterFull)
        self.tableWidget.itemClicked.connect(self.printTitle)
        self.btnReserve.clicked.connect(self.btnReserve_OnClick)
        
    def btnReserve_OnClick(self):
        self.LaoZuo_ApplyReserveWin = LaoZuo_ApplyReserve(self,self.lhuAuth)
        self.LaoZuo_ApplyReserveWin.show()
    def onCheckBoxClick_bShowMidd(self):
        checkbox = self.sender()
        self.bShowMidd=checkbox.isChecked()
        self.LaoZuoApply_textUpdate()
    def onCheckBoxClick_bShowPM(self):
        checkbox = self.sender()
        self.bShowPM= checkbox.isChecked()
        self.LaoZuoApply_textUpdate()
    def onCheckBoxClick_bShowOther(self):
        checkbox = self.sender()
        self.bShowOther= checkbox.isChecked()
        self.LaoZuoApply_textUpdate()

    def onCheckBoxClick_bFilterFull(self):
        checkbox = self.sender()
        self.bFilterFull= checkbox.isChecked()
        self.LaoZuoApply_textUpdate()

    """
    def startSearch(self):

        szTmpText=f'時段|目前/最大人數|開始報名日|截止報名日|標題\n'
        for key,val in self.LaoZuoApplyDict.items():
            if self.LaoZuoApplyDict[key]["iMaxNum"] != self.LaoZuoApplyDict[key]["iCurrNum"]: #篩掉已滿
                szTmpText+=f'{self.LaoZuoApplyDict[key]["szMTime"]}|       {self.LaoZuoApplyDict[key]["iCurrNum"]}/{self.LaoZuoApplyDict[key]["iMaxNum"]}        |{self.LaoZuoApplyDict[key]["szStartApplyDate"]}|{self.LaoZuoApplyDict[key]["szStopApplyDate"]}|{self.LaoZuoApplyDict[key]["szTitle"]}\n'

        self.textBrowser.setText(szTmpText)
    """
    def startSearchV2(self):

        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(7) 
        self.tableWidget.setHorizontalHeaderLabels(["時段", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題","報名"])

        row = 0
        for key, data in self.LaoZuoApplyDict.items():
            self.addIndex(row,data)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortByColumn(6, Qt.SortOrder.DescendingOrder)



    def LaoZuoApply_textUpdate(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(7) 
        self.tableWidget.setHorizontalHeaderLabels(["時段", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題","報名"])
        
        row = 0
        for key,val in self.LaoZuoApplyDict.items():
            if self.bFilterFull:
                if self.LaoZuoApplyDict[key]["iMaxNum"] != self.LaoZuoApplyDict[key]["iCurrNum"] : #篩掉已滿
                    if self.bShowMidd and self.LaoZuoApplyDict[key]["szMTime"] == '中午': #中午時段
                        self.addIndex(row,val)
                    if self.bShowPM and self.LaoZuoApplyDict[key]["szMTime"] == '下午': #下午時段
                        self.addIndex(row,val)

                    if self.bShowOther and self.LaoZuoApplyDict[key]["szMTime"] == '其他': 
                        self.addIndex(row,val)
            else:
                    if self.bShowMidd and self.LaoZuoApplyDict[key]["szMTime"] == '中午': #中午時段
                        self.addIndex(row,val)
                    if self.bShowPM and self.LaoZuoApplyDict[key]["szMTime"] == '下午': #下午時段
                        self.addIndex(row,val)

                    if self.bShowOther and self.LaoZuoApplyDict[key]["szMTime"] == '其他': 
                        self.addIndex(row,val)
        self.tableWidget.setSortingEnabled(True)

        self.tableWidget.sortByColumn(6, Qt.SortOrder.DescendingOrder)


    def addIndex(self,row,val):
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(val['szMTime']))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{val['iCurrNum']}/{val['iMaxNum']}"))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(val['szHours'])))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(val['szStartApplyDate']))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(val['szStopApplyDate']))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(val['szTitle']))
        szBtnText=""
        if val['szBtnText'] == "活動人數額滿":

            if checkDTExist(val['szTitle'], val['szStartApplyDate']):
                szBtnText="已額滿(取消預訂)"
            else:
                szBtnText="已額滿(可預訂)"

        elif val['szBtnText'] == "報名參加此活動":
            szBtnText="可報名(查看詳情)"
        elif val['szBtnText'] == "取消參加此活動":
            szBtnText="已報名(點擊取消)"


        self.tableWidget.setItem(row, 6, QTableWidgetItem(szBtnText))
        row += 1
        #["時段", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題"]
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 320)
        self.tableWidget.setColumnWidth(6, 110)
    def printTitle(self, item):
        title=""
        szUrl=""
        retText=""
        btnTextOld=""
        #報名&取消報名
        if item.column() == 6 and item.text() in ["可報名(查看詳情)","已報名(點擊取消)"]: #戳了第6行 & 戳的格子 文字=報名
            row = item.row()
            title = self.tableWidget.item(row, 5).text()
            szStartApplyDate = self.tableWidget.item(row, 3).text()
            for key, value in self.LaoZuoApplyDict.items():
                if value['szTitle'] == title and value['szStartApplyDate'] == szStartApplyDate:
                    #print(value['szUrl'])
                    szUrl=value['szUrl']
                    title=value['szTitle']
                    btnTextOld=value['szBtnText']
                    break  
            if item.text() == "可報名(查看詳情)":
                retText=f'''確定是否報名<{title}>？\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*勞作教育內容*：\n{value['勞作教育內容']}\n\n*勞作教育注意事項*：\n{value['勞作教育注意事項']}'''

            elif item.text() == "已報名(點擊取消)":
                retText=f'''是否取消報名<{title}>？\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*勞作教育內容*：\n{value['勞作教育內容']}\n\n*勞作教育注意事項*：\n{value['勞作教育注意事項']}'''


            if szUrl:
                reply = QMessageBox.question(
                    self, title, retText,
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.No:
                    pass
                if reply == QMessageBox.StandardButton.Yes:
                    self.postJoin(szUrl,btnTextOld)

                    self.refreshDialog = QMessageBox(self)
                    self.refreshDialog.setStyleSheet("QLabel{ color: black}")
                    self.refreshDialog.setWindowTitle("正在重新同步.........")
                    self.refreshDialog.setText("更新中.........")
                    self.refreshDialog.show()
                    self.LaoZuoApplyDict=self.lhuAuth.getPage_LaborApply() 
                    self.LaoZuoApply_textUpdate()
                    self.refreshDialog.close()
            return
        #預定
        if item.column() == 6 and item.text() in ["已額滿(可預訂)"]: #戳了第6行 & 戳的格子 文字=報名
            row = item.row()
            title = self.tableWidget.item(row, 5).text()
            szStartApplyDate = self.tableWidget.item(row, 3).text()
            for key, value in self.LaoZuoApplyDict.items():
                if value['szTitle'] == title and value['szStartApplyDate'] == szStartApplyDate:
                    szUrl=value['szUrl']
                    title=value['szTitle']
                    writeDT(value)
                    new_item = QTableWidgetItem('已額滿(取消預訂)')
                    self.tableWidget.setItem(row, 6, new_item)

                    self.msgbox(title='提示',infoText=f'''預定<{title}>成功\n開啟<[未命名][test]LaborMiner>掛著即可\n介面開啟時,每過10分鐘會自動嘗試報名一次直到成功\n\n以下是您預定的活動詳情：\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*勞作教育內容*：\n{value['勞作教育內容']}\n\n*勞作教育注意事項*：\n{value['勞作教育注意事項']}''')
                    try:
                        self.LaoZuo_ApplyReserveWin.syncDataTabel()
                    except:
                        pass
                    break 
            return
        #取消預定
        if item.column() == 6 and item.text() in ["已額滿(取消預訂)"]: #戳了第6行 & 戳的格子 文字=報名
            row = item.row()
            title = self.tableWidget.item(row, 5).text()
            szStartApplyDate = self.tableWidget.item(row, 3).text()
            for key, value in self.LaoZuoApplyDict.items():
                if value['szTitle'] == title and value['szStartApplyDate'] == szStartApplyDate:
                    dropDT(value)
                    new_item = QTableWidgetItem('已額滿(可預訂)')
                    self.tableWidget.setItem(row, 6, new_item)

                    self.msgbox(title='提示',infoText=f'''取消預定<{title}>成功\n\n以下是您取消預定的活動詳情：\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*勞作教育內容*：\n{value['勞作教育內容']}\n\n*勞作教育注意事項*：\n{value['勞作教育注意事項']}''')
                    try:
                        self.LaoZuo_ApplyReserveWin.syncDataTabel()
                    except:
                        pass
                    break 
            return

    def postJoin(self,url,btnTextOld):
        btnTextOld=btnTextOld
        r22 = self.lhuAuth.MainSession.get(url)

        #提VIEWSTATE
        soup = BeautifulSoup(r22.text, 'html.parser')
        form = soup.find('form')
        __VIEWSTATE = form.find('input', {'name': '__VIEWSTATE'})['value']
        btnTextNew = soup.find('input', {'name': 'Btn_Join'})['value']


        data = {
            '__VIEWSTATE': __VIEWSTATE,
            'Btn_Join': '報名參加此活動',
        }
        #取消參加此活動
        r = self.lhuAuth.MainSession.post(url, data=data)
        #檢測是否同步
        if btnTextOld == btnTextNew:
            self.tmpDialog.setText("操作成功") 
            self.tmpDialog.show()
        else:
            self.tmpDialog.setText(f"操作失敗:本地與server端不同步\n{btnTextOld}|{btnTextNew}") 
            self.tmpDialog.show()

class LaoZuo_ApplyReserve(QtWidgets.QMainWindow, Ui_LaoZuo_ApplyReserve):
    def __init__(self, parent=None,lhuAuth=None):
        super(LaoZuo_ApplyReserve, self).__init__(parent)
        self.lhuAuth = lhuAuth
        self.setupUi(self)

        QTimer.singleShot(0, self.runAfterShow)
        
    def runAfterShow(self):
        self.action()
        self.funcTest40304()


    def action(self):
        # 待搶活動表格
        self.ReserveTable.setColumnCount(6)
        self.ReserveTable.setHorizontalHeaderLabels(['時段', '活動標題', '開始報名日期', '截止報名日期','時數',
                                                    '操作'])
        # 已搶成功活動表格
        self.SuccessTable.setColumnCount(6)
        self.SuccessTable.setHorizontalHeaderLabels(['時段', '活動標題', '開始報名日期', '截止報名日期','時數',
                                                    '操作'])

        self.ReserveTable.setColumnWidth(0, 50)
        self.ReserveTable.setColumnWidth(1, 350)
        self.ReserveTable.setColumnWidth(2, 100)
        self.ReserveTable.setColumnWidth(3, 100)
        self.ReserveTable.setColumnWidth(4, 60)
        self.ReserveTable.setColumnWidth(5, 110)

        self.SuccessTable.setColumnWidth(0, 50)
        self.SuccessTable.setColumnWidth(1, 350)
        self.SuccessTable.setColumnWidth(2, 100)
        self.SuccessTable.setColumnWidth(3, 100)
        self.SuccessTable.setColumnWidth(4, 60)
        self.SuccessTable.setColumnWidth(5, 110)

        self.btnClearSuccess.clicked.connect(self.clearSuccessTable)
        
        #定時器
        self.timer = QTimer()
        self.timer.timeout.connect(self.funcTest40304)
        #定時器訊息
        self.timerInfo = QTimer()
        self.timerInfo.timeout.connect(self.timerUpdater)

        self.timerInfo.start(1000)  #每秒更新一次
        self.timer.start(10 * 60 * 1000) 
        

    def timerUpdater(self):
        remainingTime = self.timer.remainingTime() / 1000  #提timer當前剩餘時間
        self.RemainTimeText.setText(f'下一次嘗試剩餘時間：{int(remainingTime)} 秒')
        progress = (1 - remainingTime / 600) * 100
        self.progressBar_RemainTime.setValue(progress)

    def insertText(self, text):
        currText = self.textbox_Logger.toPlainText()
        self.textbox_Logger.setPlainText(text + '\n' + currText)
    """
        szUrl, szMTime, szTitle, szStartApplyDate, szStopApplyDate, szHours, iMaxNum, 
        iCurrNum, szBtnText, szCollectionTimePlace, szActivityPlace, szContent, szNote, bSuccess
  
        data['szUrl'], data['szMTime'], data['szTitle'], data['szStartApplyDate'], data['szStopApplyDate'],
        data['szHours'], data['iMaxNum'], data['iCurrNum'], data['szBtnText'], data['集合時間_地點'],
        data['活動地點'], data['勞作教育內容'], data['勞作教育注意事項'], 0

    """

    def add_row(self, table, data):
        row_position = table.rowCount()
        table.insertRow(row_position)

        table.setItem(row_position, 0, QTableWidgetItem(data[2]))
        table.setItem(row_position, 1, QTableWidgetItem(data[3]))     
        table.setItem(row_position, 2, QTableWidgetItem(data[4]))    
        table.setItem(row_position, 3, QTableWidgetItem(data[5])) 
        table.setItem(row_position, 4, QTableWidgetItem(data[6]))
        table.setItem(row_position, 5, QTableWidgetItem(data[9]))  

        #QTableWidgetItem(str(data[0])))  # ID
        #QTableWidgetItem(data[1]))      # URL
        #QTableWidgetItem(data[2]))      # 時段
        #QTableWidgetItem(data[3]))      # 活動標題
        #QTableWidgetItem(data[4]))      # 開始報名日期
        #QTableWidgetItem(data[5]))      # szStopApplyDate
        #QTableWidgetItem(data[6]))      # szHours
        #QTableWidgetItem(str(data[7])))  # iMaxNum
        #QTableWidgetItem(str(data[8])))  # iCurrNum
        #QTableWidgetItem(data[9]))      # szBtnText
        # QTableWidgetItem(data[10]))    # 集合時間_地點
        # QTableWidgetItem(data[11]))    # 活動地點
        # QTableWidgetItem(data[12]))    # 勞作教育內容
        # QTableWidgetItem(data[13]))    # 勞作教育注意事項

    def clearSuccessTable(self):
        print(f'[DEBUG][clearSuccessTable]')
        self.SuccessTable.setRowCount(0)
        c.execute("DELETE FROM Labors WHERE bSuccess = 1")
        conn.commit()

    def syncDataTabel(self):
        self.ReserveTable.setRowCount(0)
        self.SuccessTable.setRowCount(0)
        # 同步待搶表
        c.execute("SELECT * FROM Labors WHERE bSuccess = 0")
        DT_ReserveActivities = c.fetchall()
        for activity in DT_ReserveActivities:
            self.add_row(self.ReserveTable, activity)
        # 同步成功表
        c.execute("SELECT * FROM Labors WHERE bSuccess = 1")
        DT_SuccessActivities = c.fetchall()
        for activity in DT_SuccessActivities:
            self.add_row(self.SuccessTable, activity)


    def funcTest40304(self):
        print(f'[DEBUG][START]funcTest40304')
        # 清空兩個表格
        self.ReserveTable.setRowCount(0)
        self.SuccessTable.setRowCount(0)

        # 查詢待搶表&嘗試搶
        c.execute("SELECT * FROM Labors WHERE bSuccess = 0")
        DT_ReserveActivities = c.fetchall()
        for activity in DT_ReserveActivities:
            url = activity[1]  # URL
            actTitle = activity[3]  # 活動標題
            print(f'[DEBUG]嘗試 {url}')
            
            if self.tryJoin(url) == 1: #0已滿 1成功 2已截止
                c.execute("UPDATE Labors SET bSuccess = 1 WHERE szUrl = ?", (url,))
                conn.commit()
                self.insertText(f"[成功]<{actTitle}>報名成功")

            elif self.tryJoin(url) == 2:
                self.insertText(f"[已截止]<{actTitle}>報名已截止,將從列表中移除")
                c.execute("DELETE FROM Labors WHERE szUrl = ? AND szTitle = ?", (url, actTitle))
                conn.commit()
            elif self.tryJoin(url) == 0:
                self.insertText(f"[人數已滿]嘗試報名<{actTitle}>失敗,幾分鐘後將自動再次嘗試")
        self.syncDataTabel()

        print(f'[DEBUG][END]funcTest40304')

    def tryJoin(self,url):

        r22 = self.lhuAuth.MainSession.get(url)
        soup = BeautifulSoup(r22.text, 'html.parser')
        form = soup.find('form')
        __VIEWSTATE = form.find('input', {'name': '__VIEWSTATE'})['value']
        btnTextNew = soup.find('input', {'name': 'Btn_Join'})['value']
        data = {
            '__VIEWSTATE': __VIEWSTATE,
            'Btn_Join': '報名參加此活動',
        }

        if btnTextNew == "報名參加此活動":
            r=self.lhuAuth.MainSession.post(url, data=data)
            print(f'[DEBUG][成功]')
            return 1
        elif btnTextNew == "報名日期已截止":
            print(f'[DEBUG][報名日期已截止]')
            return 2
        else:
            print(f'[DEBUG][失敗]')
            return 0

