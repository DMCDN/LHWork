import sys
import os
import requests
import time
from PyQt6 import QtWidgets 
from PyQt6.QtCore import pyqtSignal , QThread , Qt
from PyQt6.QtWidgets import QApplication, QMessageBox, QPushButton, QLabel
from PyQt6.QtGui import QMovie
from GUI.Ui_Graduation import Ui_Graduation



class Graduation(QtWidgets.QMainWindow, Ui_Graduation):
    def __init__(self, mainWin,lhuAuth=None,parent=None):
        super(Graduation, self).__init__(parent)
        self.setupUi(self)
        self.mainWin = mainWin
        self.lhuAuth=lhuAuth
        self.startCheck()
        self.action()

    def action(self):
        #主介面
        self.btnScoreQuery.clicked.connect(self.mainWin.btnScoreQuery_OnClick)
        self.btnLaoZuo.clicked.connect(self.mainWin.btnLaoZuo_OnClick)
        self.btnFuWu.clicked.connect(self.mainWin.btnServiceQuery_OnClick)
        self.btnSpeechEvent.clicked.connect(self.mainWin.btnSpeechEvent_OnClick)


    def ScoreQueryText_Update(self, value, tips):
        self.btnScoreQuery.setText(value)
        if value == '未通過':
            self.btnScoreQuery.setEnabled(True)
            self.btnScoreQuery.setToolTip(tips)

    def LaoZuoText_Update(self, value, tips):
        self.btnLaoZuo.setText(value)
        if value == '未通過':
            self.btnLaoZuo.setEnabled(True)
            self.btnLaoZuo.setToolTip(tips)

    def FuWuText_Update(self, value, tips):
        self.btnFuWu.setText(value)
        if value == '未通過':
            self.btnFuWu.setEnabled(True)
            self.btnFuWu.setToolTip(tips)

    def CertMainText_Update(self, value):
        self.btnCertMain.setText(value)
        if value == '未通過':
            self.btnCertMain.setEnabled(True)
    def CertForeignText_Update(self, value):
        self.btnCertForeign.setText(value)
        if value == '未通過':
            self.btnCertForeign.setEnabled(True)
            
    def SpeechEventText_Update(self, value, tips):
        self.btnSpeechEvent.setText(value)
        if value == '未通過':
            self.btnSpeechEvent.setEnabled(True)
            self.btnSpeechEvent.setToolTip(tips)


    def startCheck(self):
        self.worker_thread = WorkerThread(self.lhuAuth)
        self.worker_thread.ScoreQueryText.connect(self.ScoreQueryText_Update)
        self.worker_thread.LaoZuoText.connect(self.LaoZuoText_Update)
        self.worker_thread.FuWuText.connect(self.FuWuText_Update)
        self.worker_thread.CertMainText.connect(self.CertMainText_Update)
        self.worker_thread.CertForeignText.connect(self.CertForeignText_Update)

        self.worker_thread.SpeechEventText.connect(self.SpeechEventText_Update)
        self.worker_thread.start()
        

class WorkerThread(QThread):
    #progress_updated = pyqtSignal(int)
    ScoreQueryText = pyqtSignal(str,str)
    LaoZuoText = pyqtSignal(str,str)
    FuWuText = pyqtSignal(str,str)
    SpeechEventText = pyqtSignal(str,str)

    CertMainText = pyqtSignal(str)
    CertForeignText = pyqtSignal(str)
    
    def __init__(self, lhuAuth):
        super().__init__()
        self.lhuAuth=lhuAuth

    def run(self):
        self.ScoreQueryText.emit('查詢中..','')
        self.ScoreQuery_Check()

        self.LaoZuoText.emit('查詢中..','')
        self.LaoZuo_Check()

        self.FuWuText.emit('查詢中..','')
        self.FuWu_Check()

        self.SpeechEventText.emit('查詢中..','')
        self.SpeechEvent_Check()

        self.CertMainText.emit('查詢中..')
        self.CertForeignText.emit('查詢中..')
        self.Cert_Check()

    def ScoreQuery_Check(self):
        DT_ScoreQuery=self.lhuAuth.DT_ScoreQuery_V2_SQL() 
        Score=DT_ScoreQuery['Score']
        point1=DT_ScoreQuery['point1']
        point2=DT_ScoreQuery['point2']
        point3=DT_ScoreQuery['point3']
        pointS1=DT_ScoreQuery['pointS1']
        if Score >= 128 and point1 >= 36 and point2 >= 68 and point3 >= 24 and pointS1 >= 4 :
            self.ScoreQueryText.emit('已通過','')
        else:
            strTips=''
            if not point1 >= 36:
                strTips+= f'校(選擇性)必修、院訂必修：{point1}/36 (還需要{36-int(point1)}學分)\n'
            if not point2 >= 68:
                strTips+= f'院、系專業必修：{point2}/68 (還需要{68-int(point2)}學分)\n'
            if not point3 >= 24:
                strTips+= f'系專業選修：{point3}/24 (還需要{24-int(point3)}學分)\n'
            if not pointS1 >= 24:
                strTips+= f'通職：{pointS1}/4 (須通過任4個不同領域中課程 剩餘{4-int(pointS1)}項)\n'

            self.ScoreQueryText.emit('未通過',f'以下需求不足：\n{strTips}')

    def LaoZuo_Check(self):
        LaoZuoRecordDict=self.lhuAuth.getPage_LaoZuo() 
        if LaoZuoRecordDict['bIsPracticed1'] and LaoZuoRecordDict['bIsFeedbacked1'] and LaoZuoRecordDict['bIsPracticed2'] and LaoZuoRecordDict['bIsFeedbacked2']: #1
            self.LaoZuoText.emit('已通過','')
        else:
            strTips=''
            #勞1
            if not (LaoZuoRecordDict['bIsPracticed1'] and LaoZuoRecordDict['bIsFeedbacked1']): #1&1
                strTips+=f'勞作一(上學期)：\n'
                if not LaoZuoRecordDict['bIsPracticed1'] :
                    strTips+=f"勞作時數未達標(剩餘所需次數：{LaoZuoRecordDict['iLastTime1']})\n"
                if not LaoZuoRecordDict['bIsFeedbacked1']:
                    strTips+="心得未填寫\n"
            #勞2
            if not (LaoZuoRecordDict['bIsPracticed2'] and LaoZuoRecordDict['bIsFeedbacked2']): #1&1
                strTips+=f'勞作二(下學期)：\n'
                if not LaoZuoRecordDict['bIsPracticed2'] :
                    strTips+=f"勞作時數未達標(剩餘所需次數：{LaoZuoRecordDict['iLastTime2']})\n"
                if not LaoZuoRecordDict['bIsFeedbacked2']:
                    strTips+="心得未填寫\n"

            self.LaoZuoText.emit('未通過',f'以下需求不足：\n\n{strTips}')

    def FuWu_Check(self):
        FuWuDict=self.lhuAuth.getPage_ServiceQuery() 
        print(FuWuDict)
        if FuWuDict['iCourseLast'] == 0 and FuWuDict['iActLast'] == 0 and FuWuDict['iRefLast'] == 0 : #1
            self.FuWuText.emit('已通過','')

        else:
            strTips=''
            #勞1
            if not FuWuDict['iCourseLast'] == 0: #1&1
                strTips+=f"課程時數 (剩餘所需次數：{FuWuDict['iCourseLast']})\n"
            if not FuWuDict['iActLast'] == 0: #1&1
                strTips+=f"活動時數 (剩餘所需次數：{FuWuDict['iActLast']})\n"
            if not FuWuDict['iRefLast'] == 0: #1&1
                strTips+=f"省思時數 (剩餘所需次數：{FuWuDict['iRefLast']})\n"

            self.FuWuText.emit('未通過',f'以下需求不足：\n{strTips}')

    def SpeechEvent_Check(self):
        RecordDict=self.lhuAuth.getPage_SpeechEvent()
        
        strTips=''
        PassCount = 0
        needPassCount = len(RecordDict)
        for i in RecordDict:

            if i['目前審過次數'] == i['需求次數']: #1
                PassCount += 1
            else:
                strTips += f"{i['類別']}(還需要{ int(i['需求次數'])-int(i['目前審過次數']) }次)\n"

                

        if needPassCount == PassCount:
            self.SpeechEventText.emit('已通過','')
        else:
            self.SpeechEventText.emit('未通過',f'{needPassCount - PassCount}項需求不足：\n{strTips}')

    def Cert_Check(self):
        RecordDict=self.lhuAuth.getPage_Graduation()
        #print(RecordDict)
        #0.學院名稱	1.系別名稱	2.班級名稱	3.學號	4.姓名	5.服務學習	6.勞作教育	7.外語檢定	8.基礎學科	9.專業認證	10.是否通過
        #管理學院	資訊管理系	四技資管二A	D1104241xxx	sun$$	X	X	O	O	X	不通過
        if RecordDict['外語檢定'] == "O":
            self.CertForeignText.emit('已通過')
        else:
            self.CertForeignText.emit('未通過')
            
        if RecordDict['專業認證'] == "O":
            self.CertMainText.emit('已通過')
        else:
            self.CertMainText.emit('未通過')

        
