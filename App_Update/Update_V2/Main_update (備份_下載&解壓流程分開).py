import sys
import os
import requests
import time
from PyQt6 import QtWidgets 
from PyQt6.QtCore import pyqtSignal , QThread
from PyQt6.QtWidgets import QApplication, QMessageBox

from Ui_UpdateWindow import Ui_UpdateWindow
import subprocess
import zlib

import concurrent.futures
from resDReader import respdb
from databin import BinaryStream
from io import BytesIO
import atexit

#mainAppPath=os.path.dirname(sys.argv[0])+'/test.dist'
mainAppPath=os.path.dirname(sys.argv[0])
if not os.path.exists(mainAppPath):
    os.makedirs(mainAppPath)
os.chdir(mainAppPath)

ConfigURL = "https://raw.githubusercontent.com/DMCDN/assets/main/versionConfig.txt" #versionConfig_DEV

class UpdateWindow(QtWidgets.QMainWindow, Ui_UpdateWindow):
    def __init__(self, parent=None):
        super(UpdateWindow, self).__init__(parent)
        self.setupUi(self)


    def updateFinish(self,bUpdateFinish):
        if bUpdateFinish:
            print(failList)
            if failList:
                app.quit()
            else:
                subprocess.Popen(['main.exe'])
                sys.exit()
    
    def update_text(self, value):
        self.label_text.setText(value)



    def update_progress_bar(self, value):
        self.progressBar.setValue(value)


    def GetUpdateUrl(self,rawDataUrl,diffDataUrl):
        if rawDataUrl:
            self.rawDataUrl=rawDataUrl
            self.diffDataUrl=diffDataUrl

    def updateInfo(self,retText):
        #self.loadingDialog = QMessageBox(self)
        #self.loadingDialog.setWindowTitle("更新資訊..........")
        #self.loadingDialog.setText(retText)
        #self.loadingDialog.show()

        currGeometry = self.geometry()
        current_x = currGeometry.x()
        current_y = currGeometry.y()
        self.setGeometry(current_x,current_y,456,403)
        self.label_UpdateInfo.setText(retText)

    def startUpdate(self,retText):
        if retText:

            #reply = QMessageBox.question(
            #    self, "提示", retText,
            #    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            #)
            #if reply == QMessageBox.StandardButton.No:
            #    QApplication.quit()
            #    sys.exit()
            #if reply == QMessageBox.StandardButton.Yes:
            #    self.startUpdate(True)
                self.progressBar.setValue(0)
                self.worker_thread = UpdateThread(self.rawDataUrl,self.diffDataUrl,'')
                self.worker_thread.progress_updated.connect(self.update_progress_bar)
                self.worker_thread.text_updated.connect(self.update_text)
                self.worker_thread.bUpdateFinish_Signal.connect(self.updateFinish)
                self.worker_thread.start()
        else:
            self.VersionFileErrorNew()

    def VersionFileErrorNew(self):
        reply = QMessageBox.question(
            self, "提示", f"找不到Version.bytes\n將在{os.getcwd()}安裝更新,是否繼續?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.No:
            QApplication.quit()
            sys.exit()
        if reply == QMessageBox.StandardButton.Yes:
            self.progressBar.setValue(0)
            self.worker_thread = UpdateThread(self.rawDataUrl,self.diffDataUrl,'')
            self.worker_thread.progress_updated.connect(self.update_progress_bar)
            self.worker_thread.text_updated.connect(self.update_text)
            self.worker_thread.bUpdateFinish_Signal.connect(self.updateFinish)
            self.worker_thread.start()
    
    def checkVersion(self):
        self.startResUpdate()

    def startResUpdate(self):
        self.progressBar.setValue(0)
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_progress_bar)
        self.worker_thread.text_updated.connect(self.update_text)
        self.worker_thread.szGetUpdateUrl_Signal.connect(self.GetUpdateUrl)
        self.worker_thread.startUpdate_Signal.connect(self.startUpdate)
        self.worker_thread.updateInfo_updated.connect(self.updateInfo)

        self.worker_thread.start()




class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)
    text_updated = pyqtSignal(str)
    szGetUpdateUrl_Signal = pyqtSignal(str,str)
    startUpdate_Signal = pyqtSignal(str)
    updateInfo_updated = pyqtSignal(str)

    def __init__(self):
        super().__init__()


    def run(self):
        self.text_updated.emit('正在提取版本訊息..')
        #從DMCDN 提版本訊息
        def vers(v):
            return tuple(map(int, (v.split("."))))
        
        link = ConfigURL
        r = requests.get(link)
        VersionInfo=r.json()
        self.text_updated.emit('正在提取版本訊息...')


        server_AppVer=VersionInfo["Version"]
        server_ResVer=VersionInfo["RVersion"]
        updateInfo=VersionInfo["updateInfo"]
        self.szGetUpdateUrl_Signal.emit(VersionInfo["resUrl"],VersionInfo["resDiffUrl"])
        #本地版本訊息
        if os.path.exists('Version.bytes'):
            with open('Version.bytes', "r") as f:
                data = f.read()
                dataList = data.split('|')

            Locate_AppVer = dataList[0]
            Locate_ResVer = dataList[1]

            self.progress_updated.emit(100)
            if Locate_ResVer != server_ResVer:
                print(f'Res版本不匹配:{Locate_ResVer}-|{server_ResVer}')
                self.startUpdate_Signal.emit(f'Res版本不匹配,是否更新:\nLocate:{Locate_ResVer}-|Server:{server_ResVer}\n更新內容：\n{updateInfo}')

                cnt = int(Locate_ResVer) #1
                patchInfo = ''
                bShowAllInfo = False
                if Locate_AppVer != server_AppVer:
                    bShowAllInfo = True
                for iVer,stVerText in updateInfo.items(): #iVer[13 14 15] 14
                    cnt += 1
                    if not bShowAllInfo: 
                        if int(Locate_ResVer) >= int(iVer):
                            continue
                    if cnt >= int(server_ResVer):
                        print(iVer)
                        patchInfo += f'{server_AppVer}|{iVer}：\n{stVerText}\n\n'
                        
                self.updateInfo_updated.emit(patchInfo)

            else:
                print('Res沒有更新')
                subprocess.Popen(['main.exe'])
                sys.exit()
        else:
            self.startUpdate_Signal.emit('')



class UpdateThread(QThread):

    progress_updated = pyqtSignal(int)
    text_updated = pyqtSignal(str)
    bUpdateFinish_Signal = pyqtSignal(bool)

    def __init__(self,rawDataUrl,diffDataUrl,path):
        super().__init__()
        self.rawDataUrl = rawDataUrl
        self.diffDataUrl = diffDataUrl
        self.path = path

    def run(self):
        
        self.progress_updated.emit(0)
        self.text_updated.emit("正在提取diff列表...")
        #resDir = self.path

        serverDiffData = expand_short_url(self.diffDataUrl)
        self.rawDataUrl = expand_short_url(self.rawDataUrl)

    
        diffBytes = requests.get(serverDiffData).content
        diffBytes = BinaryStream(BytesIO(diffBytes))

        serverDiff=[]
        diffLen = diffBytes.readUInt32()
        for i in range(diffLen):
            serverDiff.append({"szPath":diffBytes.readString16(),
                            "dwOffset":diffBytes.readUInt32(),
                            "dwSize":diffBytes.readUInt32(),
                            "dwCrc":diffBytes.readUInt32(),})
            
        self.text_updated.emit("分析差異")
        filesDataDict = {}
        needDownlaodList=[]
        self.TotalDownSize = 0

        for svDiff in serverDiff:
            crc = int(svDiff["dwCrc"])
            offset = int(svDiff["dwOffset"])
            size = int(svDiff["dwSize"])
            path = svDiff["szPath"]

            #local_fpathFull = os.path.join(resDir, path)
            local_fpathFull = path
            local_crc=0
            if not os.path.exists(os.path.dirname(local_fpathFull)):
                try:
                    os.makedirs(os.path.dirname(local_fpathFull))
                except:
                    pass

            # CRC是否匹配
            if os.path.exists(local_fpathFull):
                local_crc = zlib.crc32(open(local_fpathFull, "rb").read())
            if local_crc != crc:
                needDownlaodList.append([{"Range": f"bytes={offset}-{offset+size-1}"},local_fpathFull+'.temp'])
                self.TotalDownSize +=size


        self.text_updated.emit("正在下載資源")
        #successList = []
        #if len(needDownlaodList) 
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
            futures = []
            for i in needDownlaodList:
                future = executor.submit(self.download_file, i)
                futures.append(future)
            self.downloaded_size = 0
            self.start_time = time.monotonic()
            self.total_size_str = format_size(self.TotalDownSize)
            concurrent.futures.wait(futures)


        
        self.text_updated.emit("正在解壓資源")
        self.progress_updated.emit(0)

        max=len(successList)
        curr = 0
        
        for fpath in successList:
            try:
                with open(fpath, "rb") as r:
                    with open(fpath[:-5], "wb") as f:
                        f.write(Decoder(r.read(),fname=fpath[:-5]))
                os.remove(fpath)
            except PermissionError:
                failList.append(fpath)
            except respdb.respdbError as e:
                print(f"[ERROR]{e.message}")
                failList.append(fpath)
            curr+=1
            progress = curr * 100 // max
            self.progress_updated.emit(progress)
        

        
        self.text_updated.emit("更新完成")
        self.bUpdateFinish_Signal.emit(True)

        #self.text_updated.emit("更新完成")
        #os.remove(self.path)

    def download_file(self, item):
        headers, file_path = item
        response = requests.get(self.rawDataUrl, headers=headers, stream=True)

        print("[開始]",item)
        with open(file_path, 'wb') as f:
            for data in response.iter_content(chunk_size=4096): #4096
                f.write(data)
                self.downloaded_size += len(data)

                # 進度(%)
                progress = self.downloaded_size * 100 // self.TotalDownSize
                self.progress_updated.emit(progress)
                # 當前速度
                elapsed_time = time.monotonic() - self.start_time
                if elapsed_time == 0:
                    download_speed = 0
                else:
                    download_speed = self.downloaded_size / elapsed_time
                download_speed_str = format_size(download_speed)
                #以下載
                downloaded_size_str = format_size(self.downloaded_size)
                text = f"正在下載更新: {downloaded_size_str} / {self.total_size_str} ({progress}%)" \
                    f"\n當前速度: {download_speed_str}/s" \
                    f"\n文件:{file_path}"
                self.text_updated.emit(text)
            successList.append(file_path)

        print("[完成]",item)




def expand_short_url(url):
    r = requests.head(url, allow_redirects=False)
    r.raise_for_status()
    if 300 < r.status_code < 400:
        url = r.headers.get('Location', url)
    return url
def format_size(size):
    suffixes = ["B", "KB", "MB", "GB", "TB"]
    suffix_index = 0
    while size >= 1024 and suffix_index < len(suffixes) - 1:
        suffix_index += 1
        size /= 1024
    return f"{size:.2f} {suffixes[suffix_index]}"

if __name__ == "__main__":
    Decoder=respdb().DecodeFile
    successList = []
    failList=[]


    app = QtWidgets.QApplication(sys.argv)
    updateMain = UpdateWindow()
    updateMain.show()
    updateMain.checkVersion()
    app.exec()
    
    app.quit()

    if failList:
        atexit.register(os.execl, f'{mainAppPath}/Main_update0.exe', f'{mainAppPath}/Main_update0.exe',*failList)

