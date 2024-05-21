
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QListWidget,QHeaderView,QPushButton
from PyQt6.QtGui import *
from bs4 import BeautifulSoup

from GUI.Ui_Dialog_ServiceQuery import Ui_ServiceQuery
from GUI.Ui_Dialog_ServiceQuery_Apply import Ui_Service_Apply

class ServiceQuery(QtWidgets.QMainWindow, Ui_ServiceQuery):
    def __init__(self, parent=None,lhuAuth=None):
        super(ServiceQuery, self).__init__(parent)
        self.setupUi(self)
        self.action()

        self.lhuAuth=lhuAuth
        self.startSearch()


    def action(self):
        self.btnServiceApply.clicked.connect(self.btnServiceApply_OnClick)
            
    def btnServiceApply_OnClick(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        LaoZuoApplyDict=self.lhuAuth.getPage_ServiceQuery_Apply() 

        self.loadingDialog.close()

        Service_Apply(self,LaoZuoApplyDict,self.lhuAuth).show()


    def startSearch(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        RecordDict=self.lhuAuth.getPage_ServiceQuery() 
        self.loadingDialog.close()



        StatusIco1="🔴"
        StatusIco2="🔴"
        StatusIco3="🔴"
        if RecordDict['iCourseLast'] == 0:
            StatusIco1="🟢"
        if RecordDict['iActLast'] == 0: #1&1
            StatusIco2="🟢"
        if RecordDict['iRefLast'] == 0: #1&1
            StatusIco3="🟢"


        if RecordDict == False:
            tmp="查無服務學習資料"
        else:
            self.textBrowser.setText(f"""
            {StatusIco1}課程時數：{RecordDict["iCourse"]}/2    \n
            {StatusIco2}活動時數：{RecordDict["iAct"]}/16 \n
            {StatusIco3}省思時數：{RecordDict["iRef"]}/2 \n
            """)
            #tmp=f"[FBI Warning]發生未處理的錯誤({RecordDict})"
        if StatusIco1 == "🟢" and StatusIco2 == "🟢" and StatusIco3 == "🟢":
            self.Label_Status.setText("服務學習已完成！")
        else:
            self.Label_Status.setText("服務學習未完成")


class Service_Apply(QtWidgets.QMainWindow, Ui_Service_Apply):
    def __init__(self, parent=None,LaoZuoApplyDict=None,lhuAuth=None):
        super(Service_Apply, self).__init__(parent)
        self.setupUi(self)
        self.action()
        self.bShowAct = True
        self.bShowSpeech = True

        self.bFilterFull=False

        
        self.lhuAuth=lhuAuth
        self.LaoZuoApplyDict=LaoZuoApplyDict
        self.startSearchV2()
        self.tmpDialog = QMessageBox(self)
        self.tmpDialog.setStyleSheet("QLabel{ color: black}")
        self.tmpDialog.setWindowTitle("提示")
        self.tmpDialog.addButton(QMessageBox.StandardButton.Ok)  
        self.joinFlag = False 

    def action(self):
        self.checkBox_bShowAct.clicked.connect(self.onCheckBoxClick_bShowAct)
        self.checkBox_bShowSpeech.clicked.connect(self.onCheckBoxClick_bShowSpeech)

        self.checkBox_bFilterFull.clicked.connect(self.onCheckBoxClick_bFilterFull)
        self.tableWidget.itemClicked.connect(self.printTitle)


    def onCheckBoxClick_bShowAct(self):
        checkbox = self.sender()
        self.bShowAct=checkbox.isChecked()
        self.LaoZuoApply_textUpdate()

    def onCheckBoxClick_bShowSpeech(self):
        checkbox = self.sender()
        self.bShowSpeech= checkbox.isChecked()
        self.LaoZuoApply_textUpdate()



    def onCheckBoxClick_bFilterFull(self):
        checkbox = self.sender()
        self.bFilterFull= checkbox.isChecked()
        self.LaoZuoApply_textUpdate()


    def startSearchV2(self):

        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(7) 
        self.tableWidget.setHorizontalHeaderLabels(["類型", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題","報名"])


        row = 0
        for key, data in self.LaoZuoApplyDict.items():
            self.addIndex(row,data)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortByColumn(6, Qt.SortOrder.DescendingOrder)



    def LaoZuoApply_textUpdate(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(7) 
        self.tableWidget.setHorizontalHeaderLabels(["類型", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題","報名"])
        
        row = 0
        for key,val in self.LaoZuoApplyDict.items():
            if self.bFilterFull:
                if self.LaoZuoApplyDict[key]["iMaxNum"] != self.LaoZuoApplyDict[key]["iCurrNum"] : #篩掉已滿
                    if self.bShowAct and self.LaoZuoApplyDict[key]["szType"] == '活動': 
                        self.addIndex(row,val)
                    if self.bShowSpeech and self.LaoZuoApplyDict[key]["szType"] == '課程演講': 
                        self.addIndex(row,val)

            else:
                    if self.bShowAct and self.LaoZuoApplyDict[key]["szType"] == '活動': 
                        self.addIndex(row,val)
                    if self.bShowSpeech and self.LaoZuoApplyDict[key]["szType"] == '課程演講': 
                        self.addIndex(row,val)

        self.tableWidget.setSortingEnabled(True)

        self.tableWidget.sortByColumn(6, Qt.SortOrder.DescendingOrder)


    def addIndex(self,row,val):
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(val['szType']))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{val['iCurrNum']}/{val['iMaxNum']}"))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(val['szHours'])))
        self.tableWidget.setItem(row, 3, QTableWidgetItem(val['szStartApplyDate']))
        self.tableWidget.setItem(row, 4, QTableWidgetItem(val['szStopApplyDate']))
        self.tableWidget.setItem(row, 5, QTableWidgetItem(val['szTitle']))
        szBtnText=""
        if val['szBtnText'] == "活動人數額滿":
            szBtnText="已額滿"
        elif val['szBtnText'] == "報名參加此活動":
            szBtnText="可報名(查看詳情)"
        elif val['szBtnText'] == "取消參加此活動":
            szBtnText="已報名(點擊取消)"

        #if val['szType'] == "課程演講":
        #    szBtnText="查看詳情"
        self.tableWidget.setItem(row, 6, QTableWidgetItem(szBtnText))
        
        row += 1
        #["時段", "目前/最大人數", "時數", "開始報名日", "截止報名日", "標題"]
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 60)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 300)
        self.tableWidget.setColumnWidth(6, 120)
    def printTitle(self, item):
        title=""
        szUrl=""
        retText=""
        btnTextOld=""
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
                retText=f'''確定是否報名<{title}>？\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*服務內容*：\n{value['服務內容']}\n\n*服務時應注意事項*：\n{value['服務時應注意事項']}'''

            elif item.text() == "已報名(點擊取消)":
                retText=f'''是否取消報名<{title}>？\n\n*集合時間_地點*：{value['集合時間_地點']}\n*活動地點*：{value['活動地點']}\n\n*服務內容*：\n{value['服務內容']}\n\n*服務時應注意事項*：\n{value['服務時應注意事項']}'''


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
                    self.LaoZuoApplyDict=self.lhuAuth.getPage_ServiceQuery_Apply() 
                    self.LaoZuoApply_textUpdate()
                    self.refreshDialog.close()


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