import sys
import os
import json
import requests
#from pygame import mixer
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox,QCompleter,QLabel
from PyQt6.QtGui import *
#from PyQt6.QtMultimedia import QMediaPlayer, QMediaContent
#from PyQt6.QtMultimedia import *

import speech_recognition as sr
import difflib
#------ui------
from GUI.Ui_main import Ui_MainWindow
from GUI.Ui_login import Ui_LoginWindow
from GUI.Ui_Dialog_ScoreQuery import Ui_ScoreQuery
from GUI.Ui_Dialog_Cert import Ui_Cert
from GUI.Ui_Dialog_LaoZuo import Ui_LaoZuo
from GUI.Ui_Dialog_LaoZuo_Apply import Ui_LaoZuo_Apply
from GUI.Ui_Dialog_AbsendWarning import Ui_AbsendWarning
#from GUI_Guest.Ui_guestWebView import Ui_guestWebView
#------logic------
import logic.ScoreQueryWin as ScoreQueryWin
import logic.LaborWin as LaborWin
import logic.ServiceQueryWin as ServiceQueryWin
import logic.SocietyWin as SocietyWin
import logic.SpeechEventWin as SpeechEventWin
import logic.AbsendWarningWin as AbsendWarningWin
import logic.DebugToolWin as DebugToolWin
import logic.GraduationWin as GraduationWin
#import LOGIC_Guest.guestWebViewWin as guestWebViewWin
#from logic_Login import LoginWindow

from resDReader import respkg
from lhuAuth import lhuFunc
import traceback
import logging

lhuAuth=lhuFunc()

print(os.path.join(os.path.dirname(__file__)))

def loadResources(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
logging.basicConfig(filename='errorLog.log',
                    filemode='a',
                    format='\n[%(asctime)s.%(msecs)d][%(name)s][%(levelname)s]%(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    level=logging.ERROR,
                    )

try:
    with open('Version.bytes', "r") as f:
        data = f.read()
        dataList = data.split('|')
    Locate_AppVer=dataList[0]
    Locate_ResVer=dataList[1]
    VERSION=f'{Locate_AppVer}|{Locate_ResVer}'
except:
    VERSION=f'獲取版本錯誤'

    
class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(mywindow, self).__init__()
       # self.LoginWin = LoginWindow(self)
        

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(self.loadResources('icon.ico'))) #設置icon
        self.setAcceptDrops(True)
        #self.setDisabled(True)
        self.label_Ver.setText(VERSION) 
        
        #-----Dialog彈窗UI預建置-----#
        self.CertWin = Cert(self)
        self.AbsendWarningWin = AbsendWarning(self)
        self.action()
        
        #-----其餘配置preload-----#
        sys.excepthook = self.exception_hook #報錯談窗hook
        
        #self.lhuAuth=lhuFunc()
        #self.res = respkg().DecodePkg(self.loadResources('res'))

        #登入from開啟 禁用主視窗

        #-----[old]語音辨識-----#
        #self.worker_thread = SpeechThread()



    #報錯hook
    def exception_hook(self,exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
    
        logger.error("", exc_info=(exc_type, exc_value, exc_traceback))
        msg = QMessageBox()

        msg.setText(f'錯誤:')
        errormsg=''
        err=traceback.format_exception(exc_type, exc_value, exc_traceback)
        for i in err:
            errormsg+=i
        
        msg.setInformativeText(f'{errormsg}')

        msg.setWindowTitle("Error")
        msg.exec()

    
    def loadResources(self,file_name: str) -> str:
        return os.path.join(os.path.dirname(__file__), file_name)

    #connect 所有btn
    def action(self):
        #主介面
        self.btnScoreQuery.clicked.connect(self.btnScoreQuery_OnClick)
        self.btnCert.clicked.connect(self.btnCert_OnClick)
        self.btnLaoZuo.clicked.connect(self.btnLaoZuo_OnClick)
        self.btnAbsendWarning.clicked.connect(self.btnAbsendWarning_OnClick)
        self.btnServiceQuery.clicked.connect(self.btnServiceQuery_OnClick)
        self.btnSpeechEvent.clicked.connect(self.btnSpeechEvent_OnClick)
        #self.btnSociety.clicked.connect(self.btnSociety_OnClick)
        self.btnGraduation.clicked.connect(self.btnGraduation_OnClick)

        #self.btnLogout.clicked.connect(self.btnLogout_OnClick)
        
        self.btnUpdate.clicked.connect(self.btnUpdate_OnClick)
        self.btnDebugTool.clicked.connect(self.btnDebugTool_OnClick)

    
    def btnUpdate_OnClick(self):
        VersionInfo=requests.get("https://raw.githubusercontent.com/DMCDN/assets/main/versionConfig.txt").json()
        server_AppVer=VersionInfo["Version"]
        server_ResVer=VersionInfo["RVersion"]
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: black}")
        self.loadingDialog.setWindowTitle("GUI")
        if Locate_ResVer != server_ResVer:
            self.loadingDialog.setText(f'''發現新版本，重啟後將會自動更新
            App版本:{Locate_AppVer}-|{server_AppVer}
            Res版本:{Locate_ResVer}-|{server_ResVer}''')
        else:
            self.loadingDialog.setText("當前無須更新")
        self.loadingDialog.show()
    
    #Main-證照
    def btnCert_OnClick(self):

        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        CertDict=lhuAuth.getPage_Cert() 
        self.loadingDialog.close()

        self.CertWin.show()
        print(CertDict)

        szTmpText=""
        if CertDict :
            for key,val in CertDict.items():
                szTmpText+=f'{key}(證照數量：{(len(val))}):\n'
                for k,v in val.items():
                    szTmpText+=f'       {k+1}:\n'
                    szTmpText+=f'           證照名稱:{val[k]["證照名稱Title"]}\n'
                    szTmpText+=f'           證照等級:{val[k]["證照等級Levels"]}\n'
                szTmpText+=f'\n\n'
        else:
            szTmpText="您沒有任何已登記的證照"
        self.CertWin.textBrowser.setText(szTmpText)

    #Main-學分查詢
    def btnScoreQuery_OnClick(self):
        self.ScoreQueryWin = ScoreQueryWin.ScoreQuery(self,lhuAuth)
        self.ScoreQueryWin.show()

    #Main-勞作教育統計
    def btnLaoZuo_OnClick(self):
        LaborWin.LaoZuo(self,lhuAuth).show()
    def btnAbsendWarning_OnClick(self):
        AbsendWarningWin.AbsendWarning(self,lhuAuth).show()
    #Main-服務學習查詢
    def btnServiceQuery_OnClick(self):
        ServiceQueryWin.ServiceQuery(self,lhuAuth).show()
    def btnSpeechEvent_OnClick(self):
        SpeechEventWin.SpeechEvent(self,lhuAuth).show()
    def btnSociety_OnClick(self):
        SocietyWin.Society(self,lhuAuth).show()
    def btnDebugTool_OnClick(self):
        DebugToolWin.DebugTool(self,lhuAuth).show()
    def btnGraduation_OnClick(self):
        self.GraduationWin = GraduationWin.Graduation(self,lhuAuth)
        self.GraduationWin.show()
        
    def btnLogout_OnClick(self):
        LoginWin.bIsLogin = False
        lhuFunc() #初始化
        self.label_UserID.setText('') 
        try:
            os.remove('userInfo.bytes')
        except:
            pass
        try:
            os.remove('tempc')
        except:
            pass
        #self.setDisabled(True)
        #登入from開啟 禁用main
        self.hide()

        
    #def playBGMusic(self):
    #    content = self.res.extractfile("res/bg.mp3").read()
    #    bytestream = io.BytesIO(content)
    #    bytestream.seek(0)
    #    mixer.init()
    #    mixer.music.load(bytestream)
    #    time.sleep(0.8) #暫時拿來擋load卡頓
    #    mixer.music.set_volume(0.2)
    #    mixer.music.play(loops=10)


class SpeechThread(QThread):

    speechText_Signal = pyqtSignal(str)
    audio_recorded = pyqtSignal(sr.AudioData)

    def __init__(self):
        super().__init__()

    def run(self):
        self.recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                audio_recorded = self.recognizer.listen(source)
            self.speechText_Signal.emit('等待錄音結果..')

            try:
                text = self.recognizer.recognize_google(audio_recorded, language="zh-TW")
                self.speechText_Signal.emit(text)
            except sr.UnknownValueError:
                self.speechText_Signal.emit("無法辨識")
            except sr.RequestError:
                self.speechText_Signal.emit("網路錯誤")

        except OSError as e:
            self.speechText_Signal.emit("找不到麥克風")
            print(f'[找不到麥克風]{str(e)}')

    """
    def run(self):
        self.recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                self.speechText_Signal.emit("檢測開始")
                self.audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(self.audio, language="zh-TW")
                    self.speechText_Signal.emit(text)
                except sr.UnknownValueError:
                    self.speechText_Signal.emit("無法辨識")
                except sr.RequestError:
                    self.speechText_Signal.emit("網路錯誤")
        except OSError as e:
            self.speechText_Signal.emit("找不到麥克風")
            print(f'[找不到麥克風]{str(e)}')
    """

    #def stop_recognition(self):
    #    if hasattr(self, 'recognizer'):
    #        self.recognizer.__exit__()
    #        self.speechText_Signal.emit("停止")
    #        del self.recognizer




#多視窗：
#https://stackoverflow.com/questions/36768033/pyqt-how-to-open-new-window
class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.bIsLogin = False
        #self.show()
        #self.hide()
        self.setDisabled(False)
        self.AutoLogin()
        #登入介面
        self.btnLogin.clicked.connect(self.btnLogin_OnClick)
        self.textEdit_Password.returnPressed.connect(self.btnLogin_OnClick)
        #self.btnGuest.clicked.connect(self.btnGuest_OnClick)
        

    #Login-登入btn
    def btnLogin_OnClick(self):


        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(self.btnLogin.geometry()) 
        #QMovie
        self.movie = QMovie("005.gif")
        self.movie.setScaledSize(self.label.size()) 
        self.label.setMovie(self.movie)
        
        # 替換btn->gif
        self.btnLogin.hide()
        self.label.show()
        self.movie.start()


        self.hintText.setText("登入中...")
        self.worker_thread = LoginThread(self.textEdit_Account.text(),self.textEdit_Password.text())
        self.worker_thread.bIsLoginSucces.connect(self.func_Login)
        self.worker_thread.start()



        
    def func_Login(self,bIsLoginSucces):
        #替換gif->btn
        self.label.hide()
        self.movie.stop()
        self.btnLogin.show()
        
        if bIsLoginSucces:
            #window.show()
            self.bIsLogin = True
            self.close()
            window.label_UserID.setText(self.textEdit_Account.text()) 
            introwin.label_UserID.setText(f'當前用戶：{self.textEdit_Account.text()}') 
            introwin.label_UserID.setStyleSheet(introwin.label_UserID.styleSheet() + "background-color: rgb(22, 222, 0);") 
            introwin.bEnableSpeechText = True
            #introwin.searchTextbox.setEnabled(True)
            if self.checkBox_bAutoLogin.isChecked():
                userInfoDict={'userID':self.textEdit_Account.text(),'pw':self.textEdit_Password.text()}
                with open('userInfo.bytes','wb') as f:
                    data=json.dumps(userInfoDict) 
                    f.write(respkg().encryptRaw('userInfo.bytes',data))
            self.textEdit_Password.setText("")
            self.hintText.setText("")
            self.btnLogin.setText("登入")
        else:
            self.hintText.setText("帳號或密碼錯誤")
            self.btnLogin.setText("登入失敗")

        
    def func_AutoLogin(self,bIsLoginSucces):
        
        #替換gif->btn
        self.label.hide()
        self.movie.stop()
        self.btnLogin.show()
        if bIsLoginSucces:
            self.bIsLogin = True
            self.close()

            window.label_UserID.setText(self.textEdit_Account.text()) 
            introwin.label_UserID.setText(f'當前用戶：{self.textEdit_Account.text()}') 
            introwin.label_UserID.setStyleSheet(introwin.label_UserID.styleSheet() + "background-color: rgb(22, 222, 0);") 
            introwin.bEnableSpeechText = True
            #introwin.searchTextbox.setEnabled(True)
            self.textEdit_Password.setText("")
        else:
            self.hintText.setText("帳號或密碼錯誤")
            self.btnLogin.setText("登入失敗")
        self.hintText.setText("")
        self.btnLogin.setText("登入")
        
    def AutoLogin(self):
        try:
            with open('userInfo.bytes', "rb") as f:
                data=f.read()
                data=respkg().decryptRaw('userInfo.bytes',data)
                userInfoDict = json.loads(data.decode("utf-8"))

            #檢測b有已保存的uid/pw
            userInfoDict['userID']
            userInfoDict['pw']

            self.show()
            self.textEdit_Account.setText(userInfoDict['userID'])
            self.textEdit_Password.setText(userInfoDict['pw'])

            self.label = QLabel(self)
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.label.setGeometry(self.btnLogin.geometry()) 
            #QMovie
            self.movie = QMovie("005.gif")
            self.movie.setScaledSize(self.label.size()) 
            self.label.setMovie(self.movie)
            
            # 替換btn->gif
            self.btnLogin.hide()
            self.label.show()
            self.movie.start()


            self.hintText.setText("自動登入中...")
            self.worker_thread = LoginThread(userInfoDict['userID'],userInfoDict['pw'])
            self.worker_thread.bIsLoginSucces.connect(self.func_AutoLogin)
            self.worker_thread.start()
        except:
            pass


    #def btnGuest_OnClick(self):
    #    self.close()
    #    guestWebViewWin.guestWebView(self).show()


class LoginThread(QThread):

    bIsLoginSucces = pyqtSignal(bool)

    def __init__(self,uid,pwd):
        super().__init__()
        self.uid = uid
        self.pwd = pwd

    def run(self):
        b=lhuAuth.login(self.uid,self.pwd)
        self.bIsLoginSucces.emit(b)



class Cert(QtWidgets.QMainWindow, Ui_Cert):
    def __init__(self, parent=None):
        super(Cert, self).__init__(parent)
        self.setupUi(self)
class AbsendWarning(QtWidgets.QMainWindow, Ui_AbsendWarning):
    def __init__(self, parent=None):
        super(AbsendWarning, self).__init__(parent)
        self.setupUi(self)


from GUI.Ui_mainView import Ui_MainViewWindow
class MainViewWindow(QtWidgets.QMainWindow, Ui_MainViewWindow):
    def __init__(self, parent=None):
        super(MainViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.label_Ver.setText(VERSION) 
        self.setWindowIcon(QtGui.QIcon(loadResources('icon.ico')))
        #self.hide()
        self.bEnableSpeechText = False
        #ACTIONS
        self.btnLogin.clicked.connect(self.btnLogin_OnClick)
        #self.btnGuest.clicked.connect(self.btnGuest_OnClick)
        self.btnMenu.clicked.connect(self.btnMenu_OnClick)

        self.worker_thread = SpeechThread()
        self.CertWin = Cert(self)
        self.AbsendWarningWin = AbsendWarning(self)
        
    def keyPressEvent(self, event):
        if self.bEnableSpeechText:
            if event.key() == Qt.Key.Key_Control:

                self.speechText.setText('開始錄音')
                self.worker_thread.start()
                if not hasattr(self, 'speech_signal_connected'):
                    self.speech_signal_connected = True
                    self.worker_thread.speechText_Signal.connect(self.updateSpeechText)
                else:
                    pass
        
    def updateSpeechText(self, sText):

        if sText in ['找不到麥克風','網路錯誤','開始錄音','等待錄音結果..']:
            self.speechText.setText(sText)
            return


        self.speechText.setText(sText)
        if '學分' in sText:
            ScoreQueryWin.ScoreQuery(self,lhuAuth).show()
        if '證照' in sText:
            self.btnCert_OnClick()
        if '勞作' in sText:
            LaborWin.LaoZuo(self,lhuAuth).show()
        if '服務' in sText:
            ServiceQueryWin.ServiceQuery(self,lhuAuth).show()

        if '缺礦' in sText:
            AbsendWarningWin.AbsendWarning(self,lhuAuth).show()
        if '總覽' in sText:
            GraduationWin.Graduation(self,lhuAuth).show()

        if '拜訪家園' in sText:
            os.system("start \"\" https://www.youtube.com/watch?v=fJilVnglVhA")

        valid_AbsendWarning = ["缺曠", "曠課", "課程預警", "課程", "缺勤", "缺席"]
        valid_Graduation = ["畢業", "畢業門檻", "門檻"]
        #缺礦
        mostSimilar = difflib.get_close_matches(sText, valid_AbsendWarning, n=1)
        if mostSimilar:
            corrected_result = mostSimilar[0]
            print(f"[31004]孝正1：{sText} -> {corrected_result}")
            AbsendWarningWin.AbsendWarning(self,lhuAuth).show()

        #畢業門檻
        mostSimilar = difflib.get_close_matches(sText, valid_Graduation, n=1)
        if mostSimilar:
            corrected_result = mostSimilar[0]
            print(f"[31004]孝正2：{sText} -> {corrected_result}")
            GraduationWin.Graduation(self,lhuAuth).show()
        self.bIsSpeechEnable = True

    def btnCert_OnClick(self):

        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        CertDict=lhuAuth.getPage_Cert() 
        self.loadingDialog.close()

        self.CertWin.show()
        print(CertDict)

        szTmpText=""
        if CertDict :
            for key,val in CertDict.items():
                szTmpText+=f'{key}(證照數量：{(len(val))}):\n'
                for k,v in val.items():
                    szTmpText+=f'       {k+1}:\n'
                    szTmpText+=f'           證照名稱:{val[k]["證照名稱Title"]}\n'
                    szTmpText+=f'           證照等級:{val[k]["證照等級Levels"]}\n'
                szTmpText+=f'\n\n'
        else:
            szTmpText="您沒有任何已登記的證照"
        self.CertWin.textBrowser.setText(szTmpText)

    #def btnGuest_OnClick(self):
    #    guestWebViewWin.guestWebView(self).show()
        
    def btnLogin_OnClick(self):
        if LoginWin.bIsLogin:
            reply = QMessageBox.question(
                self, '提示', '確定是否登出？',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.No:
                pass
            if reply == QMessageBox.StandardButton.Yes:
                introwin.label_UserID.setStyleSheet(introwin.label_UserID.styleSheet() + "background-color: rgb(255, 130, 126);") 
                introwin.label_UserID.setText(f'當前用戶：您尚未登入') 
                
                window.btnLogout_OnClick()
                self.loginDialog = QMessageBox(self)
                self.loginDialog.setWindowTitle("提示")
                self.loginDialog.setText("登出成功")
                self.loginDialog.show()
                #self.searchTextbox.setEnabled(False)
                self.bEnableSpeechText = False
        else:
            LoginWin.show()

    def btnMenu_OnClick(self):
        if LoginWin.bIsLogin:
            window.show()
        else:
            self.loginDialog = QMessageBox(self)
            self.loginDialog.setWindowTitle("錯誤")
            self.loginDialog.setText("請先登入")
            self.loginDialog.show()
"""
def startUpload(self, ScoreDataDict):
    self.worker_thread = CheckHWIDThread()
    self.worker_thread.LogText.connect(self.LogText_Update)
    self.worker_thread.start()

class CheckHWIDThread(QThread):
    LogText = pyqtSignal(list)
    
    def __init__(self, ScoreDataDict,UserID):
        super().__init__()
        self.UserID = UserID
        self.ScoreDataDict=ScoreDataDict
        self.HashFilePath = 'ScoreDataRecord.txt' 

    def get_SerialNumber():
        output = subprocess.check_output("wmic diskdrive get serialnumber", shell=True)
        serial_number = output.decode().strip().split("\n")[-1].split("=")[-1].strip()
        return serial_number
    def run(self):
        pass

#app = QtWidgets.QApplication(sys.argv)
#introwin = MainViewWindow()
#LoginWin = LoginWindow()
#window = mywindow()
#app.exec()
"""
if __name__ == '__main__':

    #if len(sys.argv) < 2:
    #    app = QtWidgets.QApplication(sys.argv)
    #    message_box = QMessageBox()
    #    message_box.setWindowTitle("L")
    #    message_box.setText("請使用正常程序開啟")
    #    message_box.exec()
    #elif sys.argv[1] != 'keytest':
    #    app = QtWidgets.QApplication(sys.argv)
    #    message_box = QMessageBox()
    #    message_box.setWindowTitle("L")
    #    message_box.setText("請使用正常程序開啟")
    #    message_box.exec()
    #else:
        app = QtWidgets.QApplication(sys.argv)
        introwin = MainViewWindow()
        LoginWin = LoginWindow()
        window = mywindow()
        
        #window.hide()
        app.exec()


