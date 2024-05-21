import sys
import os
import requests
import time
from PyQt6 import QtWidgets 
from PyQt6.QtCore import pyqtSignal , QThread
from PyQt6.QtWidgets import QApplication, QMessageBox

from GUI.Ui_UpdateWindow import Ui_UpdateWindow
import subprocess
import zipfile

os.chdir(os.path.dirname(sys.argv[0])+'/Main.dist')

print(os.path.dirname(sys.argv[0]),os.path.join(os.path.dirname(__file__)))

class UpdateWindow(QtWidgets.QMainWindow, Ui_UpdateWindow):
    def __init__(self, parent=None):
        super(UpdateWindow, self).__init__(parent)
        self.setupUi(self)



    def update_text(self, value):
        self.label_text.setText(value)
        if value == '更新完成':
            subprocess.Popen(['main.exe'])
            sys.exit()
    def update_progress_bar(self, value):
        self.progressBar.setValue(value)
        #if value == 100:
        #    atexit.register(os.execl, self.NewEXEName,self.NewEXEName)
        #    with open(os.path.join(os.environ['USERPROFILE'], 'Version.bytes'),'wb') as f:
        #        data=json.dumps({'bIsNeedRemoveOld':True,'szExeName':self.NewEXEName}) 
        #        f.write(data)

            
    def expand_short_url(self,url):
        r = requests.head(url, allow_redirects=False)
        r.raise_for_status()
        if 300 < r.status_code < 400:
            url = r.headers.get('Location', url)
        return url
    

    def VersionFileError(self):
        reply = QMessageBox.question(
            self, "Confirmation", f"找不到Version.bytes\n將在{os.getcwd()}安裝更新,是否繼續?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Cancel:
            QApplication.quit()
            sys.exit()



    def checkVersion(self):
        #從DMCDN 提版本訊息
        def vers(v):
            return tuple(map(int, (v.split("."))))
        link = "https://raw.githubusercontent.com/DMCDN/assets/main/versionConfig.txt"
        r = requests.get(link)
        VersionInfo=r.json()
        server_AppVer=VersionInfo["Version"]
        server_ResVer=VersionInfo["RVersion"]
        self.updateUrl=self.expand_short_url(VersionInfo["updateUrl"])
        #本地版本訊息
        if os.path.exists('Version.bytes'):
            with open('Version.bytes', "r") as f:
                data = f.read()
                dataList = data.split('|')
        else:
            self.VersionFileError()
            dataList=['1.0.0','1']

        Locate_AppVer = dataList[0]
        Locate_ResVer = dataList[1]

        #比對
        #if vers(Locate_AppVer) < vers(server_AppVer):
        #    self.startAppUpdate()
        #else:
        #    print('App沒有更新')

        if Locate_ResVer != server_ResVer:
            print(f'Res版本不匹配:{Locate_ResVer}-|{server_ResVer}')
            self.startResUpdate()
        else:
            print('Res沒有更新')
            subprocess.Popen(['main.exe'])
            sys.exit()

    def startResUpdate(self):
        self.progressBar.setValue(0)
        self.worker_thread = WorkerThread(self.updateUrl,'Update_res')
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

        self.text_updated.emit("正在解壓資源")

        with zipfile.ZipFile(self.path, "r") as zip_ref:
            zip_ref.extractall()
        self.text_updated.emit("更新完成")

def format_size(size):
    suffixes = ["B", "KB", "MB", "GB", "TB"]
    suffix_index = 0
    while size >= 1024 and suffix_index < len(suffixes) - 1:
        suffix_index += 1
        size /= 1024
    return f"{size:.2f} {suffixes[suffix_index]}"


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    updateMain = UpdateWindow()
    updateMain.show()
    updateMain.checkVersion()
    app.exec()

    
