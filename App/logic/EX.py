
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *

from GUI.Ui_Dialog_LaoZuo_Apply import Ui_LaoZuo_Apply


class LaoZuo_Apply(QtWidgets.QMainWindow, Ui_LaoZuo_Apply):
    def __init__(self, parent=None,LaoZuoApplyDict=None,lhuAuth=None):
        super(LaoZuo_Apply, self).__init__(parent)
        self.setupUi(self)
        self.action()
        self.bShowMidd = True
        self.bShowPM = True
        self.bShowOther = True

        
        self.lhuAuth=lhuAuth
        self.LaoZuoApplyDict=LaoZuoApplyDict
        self.startSearch()

    def action(self):
        self.checkBox_bShowMidd.clicked.connect(self.onCheckBoxClick_bShowMidd)
        self.checkBox_bShowPM.clicked.connect(self.onCheckBoxClick_bShowPM)
        self.checkBox_bShowOther.clicked.connect(self.onCheckBoxClick_bShowOther)

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

    def startSearch(self):

        self.setStyleSheet("background-color: rgb(185, 185, 185);")
        szTmpText=f'時段|目前/最大人數|開始報名日|截止報名日|標題\n'
        for key,val in self.LaoZuoApplyDict.items():
            if self.LaoZuoApplyDict[key]["iMaxNum"] != self.LaoZuoApplyDict[key]["iCurrNum"]: #篩掉已滿
                szTmpText+=f'{self.LaoZuoApplyDict[key]["szMTime"]}|       {self.LaoZuoApplyDict[key]["iCurrNum"]}/{self.LaoZuoApplyDict[key]["iMaxNum"]}        |{self.LaoZuoApplyDict[key]["szStartApplyDate"]}|{self.LaoZuoApplyDict[key]["szStopApplyDate"]}|{self.LaoZuoApplyDict[key]["szTitle"]}\n'

        self.textBrowser.setText(szTmpText)


    def LaoZuoApply_textUpdate(self):
        szTmpText=f'時段|目前/最大人數|開始報名日|截止報名日|標題\n'
        for key,val in self.LaoZuoApplyDict.items():
            if self.LaoZuoApplyDict[key]["iMaxNum"] != self.LaoZuoApplyDict[key]["iCurrNum"]: #篩掉已滿
                if self.bShowMidd and self.LaoZuoApplyDict[key]["szMTime"] == '中午': #篩掉中午時段
                    szTmpText+=f'{self.LaoZuoApplyDict[key]["szMTime"]}|       {self.LaoZuoApplyDict[key]["iCurrNum"]}/{self.LaoZuoApplyDict[key]["iMaxNum"]}        |{self.LaoZuoApplyDict[key]["szStartApplyDate"]}|{self.LaoZuoApplyDict[key]["szStopApplyDate"]}|{self.LaoZuoApplyDict[key]["szTitle"]}\n'
                else:
                    pass

                if self.bShowPM and self.LaoZuoApplyDict[key]["szMTime"] == '下午': #篩掉下午時段
                    szTmpText+=f'{self.LaoZuoApplyDict[key]["szMTime"]}|       {self.LaoZuoApplyDict[key]["iCurrNum"]}/{self.LaoZuoApplyDict[key]["iMaxNum"]}        |{self.LaoZuoApplyDict[key]["szStartApplyDate"]}|{self.LaoZuoApplyDict[key]["szStopApplyDate"]}|{self.LaoZuoApplyDict[key]["szTitle"]}\n'
                else:
                    pass

                if self.bShowOther and self.LaoZuoApplyDict[key]["szMTime"] == '其他': 
                    szTmpText+=f'{self.LaoZuoApplyDict[key]["szMTime"]}|       {self.LaoZuoApplyDict[key]["iCurrNum"]}/{self.LaoZuoApplyDict[key]["iMaxNum"]}        |{self.LaoZuoApplyDict[key]["szStartApplyDate"]}|{self.LaoZuoApplyDict[key]["szStopApplyDate"]}|{self.LaoZuoApplyDict[key]["szTitle"]}\n'
                else:
                    pass

        self.textBrowser.setText(szTmpText)