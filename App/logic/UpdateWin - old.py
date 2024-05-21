import sys
import os
import json
import atexit
import requests
import time
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *

from GUI.Ui_UpdateWindow import Ui_UpdateWindow

from resDReader import respkg

class UpdateWindow(QtWidgets.QMainWindow, Ui_UpdateWindow):
    def __init__(self, parent=None,path="",NewVer="",updateUrl=""):
        super(UpdateWindow, self).__init__(parent)
        self.setupUi(self)
        self.startUpdate(path,NewVer,updateUrl)
        self.NewEXEName = path

    def update_text(self, value):
        self.label_text.setText(value)

    def update_progress_bar(self, value):
        self.progressBar.setValue(value)

        if value == 100:
            atexit.register(os.execl, self.NewEXEName,self.NewEXEName)
            with open(os.path.join(os.environ['USERPROFILE'], 'Version.bytes'),'wb') as f:
                data=json.dumps({'bIsNeedRemoveOld':True,'szExeName':self.NewEXEName}) 
                f.write(respkg().encryptRes('Version.bytes',data))
            sys.exit()


    def startUpdate(self, path,NewVer,updateUrl):
        self.progressBar.setValue(0)


        exeName = os.path.basename(sys.argv[0])
        if '.pyc' in exeName:
            print(exeName,'FBI WARNING')
        else:
            #self.NewEXEName = os.path.join(os.path.dirname(__file__),f'Setup_{NewVer}.exe')

            self.worker_thread = WorkerThread(updateUrl,path)
            self.worker_thread.progress_updated.connect(self.update_progress_bar)
            self.worker_thread.text_updated.connect(self.update_text)
            self.worker_thread.start()

class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)
    text_updated = pyqtSignal(str)

    def __init__(self, url,path):
        super().__init__()
        self.url = url
        self.path = path

    def run(self):
        response = requests.get(self.url, stream=True)
        total_size = int(response.headers.get('Content-Length', 0))
        downloaded_size = 0
        start_time = time.monotonic()

        with open(self.path, 'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                f.write(data)
                downloaded_size += len(data)
                progress = downloaded_size * 100 // total_size
                self.progress_updated.emit(progress)

                elapsed_time = time.monotonic() - start_time
                if elapsed_time == 0:
                    download_speed = 0
                else:
                    download_speed = downloaded_size / elapsed_time
                #download_speed = downloaded_size / elapsed_time
                download_speed_str = format_size(download_speed)
                total_size_str = format_size(total_size)
                downloaded_size_str = format_size(downloaded_size)
                text = f"正在下載更新: {downloaded_size_str} / {total_size_str} ({progress}%)" \
                       f"\n當前速度: {download_speed_str}/s"
                self.text_updated.emit(text)

        self.text_updated.emit("下載完成")

def format_size(size):
    suffixes = ["B", "KB", "MB", "GB", "TB"]
    suffix_index = 0
    while size >= 1024 and suffix_index < len(suffixes) - 1:
        suffix_index += 1
        size /= 1024
    return f"{size:.2f} {suffixes[suffix_index]}"



#old
""" onefile 更新
    def btnUpdate_OnClick(self):
        def vers(v):
            return tuple(map(int, (v.split("."))))

        link = "https://raw.githubusercontent.com/DMCDN/assets/main/version.txt"
        r = requests.get(link)
        NewVer=r.text.replace('\n','')
        if vers(VERSION) < vers(NewVer):
            mb1 = True
            if mb1 is True:
                exeName = os.path.basename(sys.argv[0])
                if '.pyc' in exeName:
                    print(exeName,'FBI WARNING')
                else:
                    
                    downloader = Downloader(worker=24,
                                            part_size=1024*1024,
                                            info=True,
                                            resumable=True)
                    NewEXEName = f'Main_{NewVer}.exe'
                    downloader.download(url="https://raw.githubusercontent.com/DMCDN/assets/main/Main.exe",
                                            path= NewEXEName)
                    atexit.register(os.execl, NewEXEName,NewEXEName)
                    with open(os.path.join(os.environ['USERPROFILE'], 'Version.bytes'),'wb') as f:
                        data=json.dumps({'bIsNeedRemoveOld':True,'szExeName':sys.argv[0]}) 
                        f.write(respkg().encryptRes('Version.bytes',data))
                    sys.exit()
                    #
                    
            elif mb1 == 'No':
                pass
        else:
            print('沒有更新')


"""

""" cmd 更新
    def btnUpdate_OnClick(self):
        def vers(v):
            return tuple(map(int, (v.split("."))))

        link = "https://raw.githubusercontent.com/DMCDN/assets/main/versionConfig.txt"
        r = requests.get(link)
        VersionInfo=r.json()
        NewVer=VersionInfo["version"]
        updateUrl=self.expand_short_url(VersionInfo["updateUrl"])
        #print(updateUrl)
        
        if vers(VERSION) < vers(NewVer):
            mb1 = True
            if mb1 is True:
                self.UpdateWin.show()
                exeName = os.path.basename(sys.argv[0])
                if '.pyc' in exeName:
                    print(exeName,'FBI WARNING')
                else:
                    downloader = Downloader(worker=24,
                                            part_size=1024*1024,
                                            info=True,
                                            resumable=True)
                    NewEXEName = os.path.join(os.path.dirname(__file__),f'Setup_{NewVer}.exe')
                    downloader.download(url=updateUrl,
                                            path=NewEXEName)
                    atexit.register(os.execl, NewEXEName,NewEXEName)
                    with open(os.path.join(os.environ['USERPROFILE'], 'Version.bytes'),'wb') as f:
                        data=json.dumps({'bIsNeedRemoveOld':True,'szExeName':NewEXEName}) 
                        f.write(respkg().encryptRes('Version.bytes',data))
                    sys.exit()
                    #
                    
            elif mb1 == 'No':
                pass
        else:
            print('沒有更新')
"""