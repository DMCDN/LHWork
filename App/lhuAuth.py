import json
import requests,pickle
from bs4 import BeautifulSoup
import os   
import sqlite3
class lhuFunc:
    def __init__(self):
        self.MainSession = requests.Session()
        self.UserID = ""
        #self.getCookies()
            #self.login()
    def saveCookies(self):
        with open('tempc', 'wb') as f:
            pickle.dump(self.MainSession.cookies, f)
    def getCookies(self):
        try:
            with open('tempc', 'rb') as f:
                self.MainSession.cookies.update(pickle.load(f))
        except:
            return 0
        urlLoginMsg=f'https://www.lhu.edu.tw/StudAp/LoginMsg.aspx'
        r = self.MainSession.get(urlLoginMsg)
        if '歡迎' in r.text :
            return 1
        else:
            return 0

    def login(self,UserID,PassWord):
        print("[login]登入中...")
        self.UserID = UserID
        self.PassWord = PassWord

        self.stdInfo_Year = self.UserID[1:4]

        if self.getCookies():
            print("[login2]完成")
            return 1
        
        urlAuth=f'http://www.lhu.edu.tw/StudAp/LoginLDAPs.aspx?LogLDAPIDTXSd={self.UserID}&LogLDAPPassTXSd={self.PassWord}&sessionId=dm'
        resp = self.MainSession.post(urlAuth)
        if "帳號或密碼錯誤" in resp.text:
            print("[login]帳號或密碼錯誤")
            return 0
        print("[login]完成")
        self.saveCookies()


        return 1
    
    def devDumpAllPage(self):
        urlGraduation=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1004A'
        urlLaborApply=f'https://www.lhu.edu.tw/StudAp/C00/C4001/Apply/Labor_Apply.aspx'
        urlAbsendWarning=f'https://www.lhu.edu.tw/StudAp/C00/C2001/Absend_WarningQry.aspx'
        urlLaoZuo=f'https://www.lhu.edu.tw/StudAp/C00/C4001/Query/Labor_Query.aspx'
        urlScoreQuery=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1004B'
        urlCert=f'https://www.lhu.edu.tw/StudAp/C00/C0001/Personal_Interface1.aspx?Choice=8'
        urlServiceQuery=f'https://www.lhu.edu.tw/StudAp/C00/C1001/Query/Service_Query.aspx'
        urlSociety=f'https://www.lhu.edu.tw/StudAp/C00/C0001/Personal_Interface4.aspx?Choice=5'
        urlSpeechEvent=f'https://www.lhu.edu.tw/StudAp/C00/C0001/Personal_Interface4.aspx?Choice=6'
        urlSpeechEvent2=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1006'
        

        #tmp+="\n[url]\n"
        #tmp+=self.MainSession.get(url).text
        """
        tmp=""
        tmp+="\n[urlGraduation]\n"
        tmp+=
        tmp+="\n[urlLaborApply]\n"
        tmp+=self.MainSession.get(urlLaborApply).text
        tmp+="\n[urlAbsendWarning]\n"
        tmp+=self.MainSession.get(urlAbsendWarning).text
        tmp+="\n[urlLaoZuo]\n"
        tmp+=self.MainSession.get(urlLaoZuo).text
        tmp+="\n[urlScoreQuery]\n"
        tmp+=self.MainSession.get(urlScoreQuery).text
        tmp+="\n[urlCert]\n"
        tmp+=self.MainSession.get(urlCert).text
        tmp+="\n[urlServiceQuery]\n"
        tmp+=self.MainSession.get(urlServiceQuery).text
        tmp+="\n[urlSociety]\n"
        tmp+=self.MainSession.get(urlSociety).text
        tmp+="\n[urlSpeechEvent]\n"
        tmp+=self.MainSession.get(urlSpeechEvent).text

        """
        #with open("dump.bytes","w",encoding='utf-8') as f:
        #   f.write(tmp)

        with open("urlGraduation.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlGraduation).text)
        with open("urlLaborApply.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlLaborApply).text)
        with open("urlAbsendWarning.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlAbsendWarning).text)
        with open("urlLaoZuo.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlLaoZuo).text)
        with open("urlScoreQuery.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlScoreQuery).text)
        with open("urlCert.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlCert).text)
        with open("urlServiceQuery.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlServiceQuery).text)
        with open("urlSociety.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlSociety).text)
        with open("urlSpeechEvent.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlSpeechEvent).text)
        with open("urlSpeechEvent2.bytes","w",encoding='utf-8') as f:
           f.write(self.MainSession.get(urlSpeechEvent2).text)

        

    def getScoreQueryData(self): #學分
        return self.getPage_ScoreQuery()

        ScoreDataDict=self.getPage_ScoreQuery()
        #只算加總
        Score=0
        for key,val in ScoreDataDict.items():
            for i in val:
                Score+=int(float(i[3]))

    def getCertData(self): #證照
        
        certDataDict=self.getPage_Cert()
        for key,val in certDataDict.items(): #key:類型 , val:該類底下的dict
            print(key)
            print(f'證照數量:{len(val)}')
            for certNum in val:
                print(f' {val[certNum]["證照名稱Title"]} ,  {val[certNum]["證照等級Levels"]} ')

    def getPage_Graduation(self):
#        https://www.lhu.edu.tw/StudAp/B00/B1001/H_ScoreQuery.aspx
        urlGraduation=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1004A'
        r22 = self.MainSession.get(urlGraduation)
        return self.DT_Graduation(r22.text)
    
    def getPage_LaborApply(self):
        urlLaborApply=f'https://www.lhu.edu.tw/StudAp/C00/C4001/Apply/Labor_Apply.aspx'
        r22 = self.MainSession.get(urlLaborApply)
        return self.DT_LaborApply(r22.text)
    
    def getPage_LaborApply_D(self,url):
        r22 = self.MainSession.get(url)
        with open("web.html","w",encoding='utf-8') as f:
            f.write(r22.text)

        return self.DT_LaborApply_D(r22.text)
    
    def getPage_AbsendWarning(self):
        urlAbsendWarning=f'https://www.lhu.edu.tw/StudAp/C00/C2001/Absend_WarningQry.aspx'
        r22 = self.MainSession.get(urlAbsendWarning)
        return self.DT_AbsendWarning(r22.text)

    def getPage_LaoZuo(self):
        urlLaoZuo=f'https://www.lhu.edu.tw/StudAp/C00/C4001/Query/Labor_Query.aspx'
        r23= self.MainSession.get(urlLaoZuo)
        #with open("LaborRaw","w",encoding='utf-8') as f:
        #   f.write(r23.text)
        return self.DT_LaoZuo(r23.text)
    
    def LaborApplyReserve(self):
        pass
    

    def getPage_LaoZuo_Think(self):
        headerUrl = 'https://www.lhu.edu.tw/StudAp/C00/C4001/Think/'
        r23= self.MainSession.get(f"{headerUrl}mmenu.aspx")
        soup = BeautifulSoup(r23.text.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        
        ThinkAddUrl = f"{headerUrl}{soup.find('a', id='HL_ADD').get('href')}"
        ThinkQryUrl = f"{headerUrl}{soup.find('a', id='HL_Qry').get('href')}"
        return self.DT_LaoZuo_Think(ThinkAddUrl,ThinkQryUrl)

    def getPage_Cert(self):
        #轉到LTSS
        #self.MainSession.get('https://www.lhu.edu.tw/StudAp/Assota/ChangePage.aspx?FID=A1E06')

        urlCert=f'https://www.lhu.edu.tw/StudAp/C00/C0001/Personal_Interface1.aspx?Choice=8'
        r22 = self.MainSession.get(urlCert)
        return self.DT_Cert(r22.text)


    def getPage_FangYi(self):
        urlC4001=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=C4001'
        r22= self.MainSession.get(urlC4001)
        return self.DT_FangYi(r22.text)

    def getPage_ScoreQuery(self):
        urlScoreQuery=f'https://www.lhu.edu.tw/StudAp/B00/B1001/H_ScoreQuery.aspx'
        r22 = self.MainSession.get(urlScoreQuery)

        #提VIEWSTATE
        soup = BeautifulSoup(r22.text, 'html.parser')
        form = soup.find('form')
        __VIEWSTATE = form.find('input', {'name': '__VIEWSTATE'})['value']
        #提全學年option
        SYear=form.findAll('option')
        AllScoreDict={}
        print("[getPage_ScoreQuery]開始搜尋")
        for y in SYear:
            year=y.string
            print(f"[getPage_ScoreQuery]正在搜尋:{year}")
            data = {'__VIEWSTATE':__VIEWSTATE,'DropDownList1': year,'Button1': '查詢'}
            r22 = self.MainSession.post(urlScoreQuery, data=data)

            soup2 = BeautifulSoup(r22.text.replace('<br>',"").replace('<br/>',""), "html.parser")
            tableA = soup2.find('table', id="PanelA") #學期1
            tableB = soup2.find('table', id="PanelB") #學期2
            
            if tableA != None:
                AllScoreDict.update({f'{year}-1':self.DT_ScoreQuery(tableA,1)}) #{110-1:[]}
            if tableB != None:
                AllScoreDict.update({f'{year}-2':self.DT_ScoreQuery(tableB,2)})
        return AllScoreDict

    def getPage_ServiceQuery(self):
        urlServiceQuery=f'https://www.lhu.edu.tw/StudAp/C00/C1001/Query/Service_Query.aspx'
        r22 = self.MainSession.get(urlServiceQuery)
        return self.DT_ServiceQuery(r22.text)
    

    def getPage_ServiceQuery_Apply(self):
        urlServiceApply=f'https://www.lhu.edu.tw/StudAp/C00/C1001/Apply/Service_Apply.aspx'
        r22 = self.MainSession.get(urlServiceApply)
        return self.DT_ServiceQuery_Apply(r22.text)
    
    def getPage_ServiceQuery_Apply_D(self,url):
        r22 = self.MainSession.get(url)
        with open("web.html","w",encoding='utf-8') as f:
            f.write(r22.text)

        return self.DT_ServiceQuery_Apply_D(r22.text)

    def getPage_Society(self):
        urlSociety=f'https://www.lhu.edu.tw/StudAp/C00/C0001/Personal_Interface4.aspx?Choice=5'
        r22 = self.MainSession.get(urlSociety)
        return self.DT_Society(r22.text)
    def getPage_SpeechEvent(self):
        urlSpeechEvent=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1006'
        r22 = self.MainSession.get(urlSpeechEvent)
        return self.DT_SpeechEvent(r22.text)
    #--------------------------[Page處理]Begin--------------------------
    #防疫
    def DT_FangYi(self,data):
        re=data.replace('<br>',"").replace('<br/>',"")
        soup = BeautifulSoup(re)
        tables = soup.findAll("table")
        table = tables[0]
        rows = table.findAll("tr")
        dt=[]
        for row in rows:
            tds = row.findAll('td')
            dt2=[]
            for i in range(0,len(tds)):
                spans=tds[i].findAll('span')
                if spans ==[] :#外層
                    dt2.append(tds[i].string)
                else: #span,內層
                    dt2.append(spans[0].string)
            dt.append(dt2)
        return dt
    #歷史成績
    def DT_ScoreQuery(self,data,num=1):
        #['110', '1', '興趣與職涯探索', '尤昌筧', '78', '1.00', 'N']
        #[0]學年/學期/科目名/導師/成績/學分/未知
        #[ext]科目名/導師/成績/學分/未知
        td = data.find("td",id=f"UltraWebGrid{num}_mc")
        tbody = td.find("tbody")
        tr= tbody.findAll("tr")
    
        ScoreList=[] 
        for row in tr:
            tds = row.findAll('td')
            tempList=[]
    
            if len(tds) > 6: #如果是第一筆，前2會多[學年/學期] 
                #year=tds[0].string
                #semester=tds[1].string
                #ScoreList.append(tempList) 
                tds.pop(0)
                tds.pop(0)
                #初始化
                tempList=[]
    
            for i in range(len(tds)):
                tempList.append( (tds[i].string).replace('\xa0','') )
    
            ScoreList.append(tempList) 
        return ScoreList
    #證照 暫時dump to json
    def DT_Cert(self,webRaw):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

        td = soup.find("tr",id="_ctl0_tr_8_3")
        table = td.find("table",id="_ctl0_Panel8")
        tables = table.findAll("table")
        
        CertInfoDict={}

        #每個table=不同證照分類
        for t in tables:
            CertInfoMain={}
            trs = t.findAll("tr")
            #第一行 標題列
            titleList=trs[0].findAll("td") + trs[0].findAll("span")
            trs.pop(0)

            #[廢置]標題key統一化
#            for index, value in enumerate(titleList):
#                if '證照名稱' == value:
#                  titleList[index] = "title"
            CertCount=-1
            #其餘tr trs-1=證照數
            for tr in trs:
                CertInfo={}
                text=tr.findAll("td") + tr.findAll("span")
                index=0
                for tt in text:
                    if tt.string != None:
                        CertInfo.update({titleList[index].string:tt.string})
                    else:
                        index-=1
                    index+=1
                CertCount+=1
                CertInfoMain.update({CertCount : CertInfo})
            t.extract()
            CertInfoDict.update({table.findChild("span").string:CertInfoMain})
            table.findChild("span").extract()
            
        return(CertInfoDict)
    
    def DT_LaoZuo(self,webRaw):
        print("[DT_LaoZuo]開始處理")
        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        table = soup.find("table",id="Panel1") #None代表完全空白
        LaoZuoRecordDict={}

        if table is None:
            LaoZuoRecordDict.update({'iLastTime1':12,'bIsPracticed1':False,'bIsFeedbacked1':False,'szFeedbackedStatus1':"未填寫"})
            LaoZuoRecordDict.update({'iLastTime2':12,'bIsPracticed2':False,'bIsFeedbacked2':False,'szFeedbackedStatus2':"未填寫"})
            #print(f'勞作教育一：{(12,False,False)}')
            #print(f'勞作教育二：{(12,False,False)}')
            return LaoZuoRecordDict
        #tbody = table.find("tbody")
        tbodys = table.findAll("table") #全滿:本體1,勞一2,勞二3

        if len(tbodys) == 3 :
            v1=[x.string for x in tbodys[1].findAll('td') if x.string is not None]
            v2=[x.string for x in tbodys[2].findAll('td') if x.string is not None]
            #sz剩餘時數,b實作已完成,b心得已完成,sz心得已填/未填
            #print(f'勞作教育一：{self.DT_LaoZuo_Proc1(v1)}')
            #print(f'勞作教育二：{self.DT_LaoZuo_Proc1(v2)}')
            temp1=self.DT_LaoZuo_Proc1(v1)
            temp2=self.DT_LaoZuo_Proc1(v2)
            LaoZuoRecordDict.update({'iLastTime1':int(temp1[0]),'bIsPracticed1':temp1[1],'bIsFeedbacked1':temp1[2],'szFeedbackedStatus1':temp1[3]})
            LaoZuoRecordDict.update({'iLastTime2':int(temp2[0]),'bIsPracticed2':temp2[1],'bIsFeedbacked2':temp2[2],'szFeedbackedStatus2':temp2[3]})
            return LaoZuoRecordDict

        elif len(tbodys) == 2 :
            title=tbodys[0].find('td').string #勞作教育X 本體1,勞X2
            v1=[x.string for x in tbodys[1].findAll('td') if x.string is not None]
            temp1=self.DT_LaoZuo_Proc1(v1)
            #print(f'{title}：{self.DT_LaoZuo_Proc1(v1)}')

            #另一學期回傳(0,False,False)
            if title == '勞作教育一':
                LaoZuoRecordDict.update({'iLastTime1':int(temp1[0]),'bIsPracticed1':temp1[1],'bIsFeedbacked1':temp1[2],'szFeedbackedStatus1':temp1[3]})
                LaoZuoRecordDict.update({'iLastTime2':12,'bIsPracticed2':False,'bIsFeedbacked2':False,'szFeedbackedStatus2':"未填寫"})
                #print(f'勞作教育二：{(12,False,False)}')
            elif title == '勞作教育二':
                LaoZuoRecordDict.update({'iLastTime1':12,'bIsPracticed1':False,'bIsFeedbacked1':False,'szFeedbackedStatus1':"未填寫"})
                LaoZuoRecordDict.update({'iLastTime2':int(temp1[0]),'bIsPracticed2':temp1[1],'bIsFeedbacked2':temp1[2]})
                #print(f'勞作教育一：{(12,False,False)}')
            else:
                print(f'[Warning][DT_LaoZuo]未知title:{title}')
            return LaoZuoRecordDict

        else:
            print(f'[DT_LaoZuo]未知tbody數量：{len(tbodys)}')
            
        return 0
    
    def DT_LaoZuo_Proc1(self,tmpList):
        bIsPracticeComplete,bIsFeedbackComplete = False,False
        szFeedbackedStatus="未填寫"
        for i in range(int(len(tmpList) / 6)-1):
            for ii in range(6):
                title=tmpList[ii]
                val=tmpList[ (i * 6) + ii + 6 ]
                #print(f'{title}:{val}')
                if ii == 5:
                    szFeedbackedStatus=val
                    if val == '已填寫':
                        bIsFeedbackComplete = True
                    
        #print('v:',tmpList[-2],tmpList[-1])

        if tmpList[-1] == '0':
            bIsPracticeComplete = True

        return (tmpList[-1],bIsPracticeComplete,bIsFeedbackComplete,szFeedbackedStatus)
            
    def DT_LaoZuo_Think(self,ThinkAddUrl,ThinkQryUrl):
        r23= self.MainSession.get(ThinkAddUrl)
        soup = BeautifulSoup(r23.text.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

    

    def DT_AbsendWarning(self,webRaw,):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

        tables = soup.findAll("table")
        tds = tables[1].findAll("td") 
        MainDict={}
        #2.班級名稱	3.科目名稱	4.授課教師	5.週上課時數	6.缺曠總節數	7.課程預警
        for i in range(1, int(len(tds)/8) ): #從1開始 略過標題列
           # tds[i*8 +4 -1].string
            #print(tds[i*8 +3].string)
            #print(tds[i*8 +4].string)
            #print(tds[i*8 +5].string)
            #print(tds[i*8 +6].string)
            #print(tds[i*8 +7].string)


            tmpDict={}
            tmpDict.update({
                "szClassName":tds[i*8 +2].string , 
                "szSubjectName":tds[i*8 +3].string.replace(" ",""), 
                "szTeachName":tds[i*8 +4].string.replace("    ","") ,
                "iClassNumTime":int(tds[i*8 +5].string) ,
                "iAbsendNumTime":int(tds[i*8 +6].string) ,
                "szWarnText":tds[i*8 +7].string.replace('\xa0','') ,})
            MainDict.update({i-1:tmpDict})
        return MainDict

    #社團
    def DT_Society(self,webRaw):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

        td = soup.find("tr",id="_ctl0_tr_5_3")
        table = td.find("table",id="_ctl0_Panel5")
        tables = table.findAll("table")
        SocietyDict={}

        if len(tables) == 1:
            return False
        else:
            return True

    #演講
    def DT_SpeechEvent(self,webRaw):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        table = soup.find("table",id="GV_Informal")
        trs = table.findAll("tr")[1:]
        
        itemList=[]
        for tr in trs:
            tds = tr.findAll("td") 
            pass
        
            result = {}
            # 0規定代碼	1類別	2校內外要求	3.團隊要求	4.需繳交心得    5.備註	6.需求次數(可能是空的)	7.目前審過次數
            #for i in range(0,7):
            #    print(tds[i].string)
            if tds[7].string == '\xa0':
                i7 = '0'
            else:
                i7 = tds[7].string
            result.update({
                '類別':tds[1].string,
                '需求次數':tds[6].string,
                '目前審過次數':i7,
            })
            itemList.append(result)
        return(itemList)

        

    def DT_ServiceQuery(self,webRaw):
        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        table = soup.find("table",id="Panel2") #None代表完全空白
        ServiceQueryDict={}

        if table is None:
            ServiceQueryDict.update({'iCourse':0,'iAct':0,'iRef':0})
            ServiceQueryDict.update({'iCourseLast':2,'iActLast':16,'iRefLast':2})
            return ServiceQueryDict

        tbodys = table.findAll("table") #全滿:本體1,勞一2,勞二3

        v1=[x.string for x in tbodys[1].findAll('td')+tbodys[1].findAll('th') if x.string is not None]
        tmpL = v1[-8:] #取後8

        ServiceQueryDict.update({'iCourseLast':int(float(tmpL[1])),'iActLast':int(float(tmpL[2])),'iRefLast':int(float(tmpL[3]))})
        ServiceQueryDict.update({'iCourse':int(float(tmpL[5])),'iAct':int(float(tmpL[6])),'iRef':int(float(tmpL[7]))})
        
        return ServiceQueryDict

    def DT_ServiceQuery_Apply(self,webRaw,):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

        tables = soup.findAll("table")
        tds = tables[1].findAll("td") 
        
        layDict={}

        for i in range(1, int(len(tds)/8) ):
            if '課程演講' in tds[i*8 +1].string :
                szType='課程演講'
            else:
                szType='活動'

            tmpDict={}

            #抓報名btn文字
            szUrl="https://www.lhu.edu.tw/StudAp/C00/C1001/Apply/"+tds[i*8].find('a').get('href')
            szBtnText=""
            rtmp=self.MainSession.get(url=szUrl)
            soup2 = BeautifulSoup(rtmp.content, 'html.parser')
            btnText = soup2.find('input', {'name': 'Btn_Join'})

            if btnText:
                szBtnText = btnText['value']
            else:
                szBtnText=''
                print("Btn_Join not found")

            集合時間_地點 = soup2.find('span', {'id': 'L_Ass_Date'}).get_text()
            活動地點 = soup2.find('span', {'id': 'L_PlaceIn'}).get_text()
            服務內容 = soup2.find('textarea', {'id': 'TB_Content'}).get_text()
            服務時應注意事項 = soup2.find('textarea', {'id': 'TB_Notice'}).get_text()

            if tds[i*8 +7].string == '\xa0': #目前人數為0時的表現 暫定
                iCurrNum = 0
            else:
                iCurrNum = int(tds[i*8 +7].string)

            tmpDict.update({
                "szUrl":szUrl, 
                "szType":szType, 
                "szTitle":tds[i*8 +1].string , 
                "szStartApplyDate":tds[i*8 +3].string ,
                "szStopApplyDate":tds[i*8 +4].string ,
                "szHours":tds[i*8 +5].text.replace('\n','') ,
                "iMaxNum":int(tds[i*8 +6].string) ,
                "iCurrNum":iCurrNum ,
                "szBtnText":szBtnText,
                "集合時間_地點":集合時間_地點,
                "活動地點":活動地點,
                "服務內容":服務內容,
                "服務時應注意事項":服務時應注意事項,
                })
            print({i-1:tmpDict})
            layDict.update({i-1:tmpDict})
        return layDict
    def DT_ServiceQuery_Apply_D(self,webRaw):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        tables = soup.findAll("table")
        tds = tables[1].findAll("td") 
        
        layDict={}
        print(tds)
        for i in range(1, int(len(tds)/8) ):
            if '課程演講' in tds[i*8 +1].string :
                szType='課程演講'
            else:
                szType='活動'

            tmpDict={}
            
            tmpDict.update({
                "szUrl":"https://www.lhu.edu.tw/StudAp/C00/C1001/Apply/"+tds[i*8].find('a').get('href'), 
                "szType":szType, 
                "szTitle":tds[i*8 +1].string , 
                "szStartApplyDate":tds[i*8 +3].string ,
                "szStopApplyDate":tds[i*8 +4].string ,
                "szHours":tds[i*8 +5].text ,
                "iMaxNum":int(tds[i*8 +6].string) ,
                "iCurrNum":int(tds[i*8 +7].string) ,})

            layDict.update({i-1:tmpDict})
        return layDict



    def DT_Graduation(self,webRaw,):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        tables = soup.findAll("table")
        tds_data = tables[1].findAll("td") 
        ths_Title = tables[1].findAll("th")

        #標題層
        Title=[] 
        for i in range(len(ths_Title)):
            value = ths_Title[i].get_text(strip=True).replace('\u3000', '')
            Title.append(value)
        #DATA
        MainList = {}
        for i in range(len(Title)):
            key = Title[i]
            value = tds_data[i].get_text(strip=True)
            MainList[key] = value

        print(MainList)
        return MainList


    def DT_LaborApply(self,webRaw,):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')

        tables = soup.findAll("table")
        tds = tables[1].findAll("td") 
        
        layDict={}
        for i in range(1, int(len(tds)/8) ):
            if '中午' in tds[i*8 +1].string :
                szMTime='中午'
            elif '下午' in tds[i*8 +1].string :
                szMTime='下午'
            else:
                szMTime='其他'

            tmpDict={}

            #抓報名btn文字
            szUrl="https://www.lhu.edu.tw//StudAp/C00/C4001/Apply/"+tds[i*8].find('a').get('href')
            szBtnText=""
            rtmp=self.MainSession.get(url=szUrl)
            soup2 = BeautifulSoup(rtmp.content, 'html.parser')
            btnText = soup2.find('input', {'name': 'Btn_Join'})

            if btnText:
                szBtnText = btnText['value']
            else:
                szBtnText=''
                print("Btn_Join 文本 not found")

            集合時間_地點 = soup2.find('span', {'id': 'L_Ass_Date'}).get_text()
            活動地點 = soup2.find('span', {'id': 'L_Place'}).get_text()
            勞作教育內容 = soup2.find('textarea', {'id': 'TB_Content'}).get_text()
            勞作教育注意事項 = soup2.find('textarea', {'id': 'TB_Notice'}).get_text()

            if tds[i*8 +7].string == '\xa0': #目前人數為0時的表現 暫定
                iCurrNum = 0
            else:
                iCurrNum = int(tds[i*8 +7].string)

            tmpDict.update({
                "szUrl":szUrl, 
                "szMTime":szMTime, 
                "szTitle":tds[i*8 +1].string , 
                "szStartApplyDate":tds[i*8 +3].string ,
                "szStopApplyDate":tds[i*8 +4].string ,
                "szHours":tds[i*8 +5].text.replace('\n','') ,
                "iMaxNum":int(tds[i*8 +6].string) ,
                "iCurrNum":iCurrNum ,
                "szBtnText":szBtnText,
                "集合時間_地點":集合時間_地點,
                "活動地點":活動地點,
                "勞作教育內容":勞作教育內容,
                "勞作教育注意事項":勞作教育注意事項,
                })
            layDict.update({i-1:tmpDict})
        return layDict
    def DT_LaborApply_D(self,webRaw):

        soup = BeautifulSoup(webRaw.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        tables = soup.findAll("table")
        tds = tables[1].findAll("td") 
        
        layDict={}
        for i in range(1, int(len(tds)/8) ):
            if '中午' in tds[i*8 +1].string :
                szMTime='中午'
            elif '下午' in tds[i*8 +1].string :
                szMTime='下午'
            else:
                szMTime='其他'

            tmpDict={}

            tmpDict.update({
                "szUrl":"https://www.lhu.edu.tw//StudAp/C00/C4001/Apply/"+tds[i*8].find('a').get('href'), 
                "szMTime":szMTime, 
                "szTitle":tds[i*8 +1].string , 
                "szStartApplyDate":tds[i*8 +3].string ,
                "szStopApplyDate":tds[i*8 +4].string ,
                "szHours":tds[i*8 +5].text ,
                "iMaxNum":int(tds[i*8 +6].string) ,
                "iCurrNum":int(tds[i*8 +7].string) ,})

            layDict.update({i-1:tmpDict})
        return layDict
    
    def DT_ScoreQuery_V2(self):

        ScoreDataDict=self.getScoreQueryDataV2() 
        GlobalScoreData =self.getGlobalScoreData(self.stdInfo_Year)

        
        print("[DT_ScoreQuery_V2]getGlobalScoreData 結束")
        Score=0
        for data in ScoreDataDict:
            Score += data["學分"]
        # 初始化數據
        point1 = 0
        point1List=[]
        point2 = 0
        point2List=[]
        point3 = 0
        point3List=[]
        pointS1 = 0
        pointS1List=[]
        pointS1BlackList=[]
        FBIWarningText=''

        print("[DT_ScoreQuery_V2]比對開始")
        # 遍歷 學生ScoreData
        for i in ScoreDataDict:
            courseName = i['科目名稱']
            courseCode = i['課號']
            courseScore = i['學分']
            matched = False

            #遍歷配當表的所有val
            for key, val in GlobalScoreData.items():
                
                for course_info in val:
                    #課號
                    if courseCode == course_info['課號']:
                        if key in ['校選修', '校必修', '院訂必修', '校選擇性必修']:
                            point1 += courseScore
                            point1List.append(i)
                        elif key in ['系專業必修', '院專業必修']:
                            point2 += courseScore
                            point2List.append(i)
                        elif key == '系專業選修':
                            point3 += courseScore
                            point3List.append(i)


                        #通職 額外計算 通職課號(CS22E xxx 固定CS22 + A~F (表領域1-6))
                        if key in ['校選擇性必修'] :
                            if courseCode[4:5] not in pointS1BlackList:
                                pointS1 += 1
                                pointS1List.append(i)
                                pointS1BlackList.append(courseCode[4:5])
                            else:
                                FBIWarningText+=f"[FBI WARNING!!!]未匹配的課程: {courseName}|{courseCode}\n"
                                print(f'[DT_ScoreQuery_V2][FBI WARNING!!!][通職類檢測]:{courseName|courseCode} 通職包含重複課號類({courseCode[4:5]},當前名單:{pointS1BlackList})')
                        matched = True
                        break
                    #科目名稱
                    elif courseName in course_info['科目名稱'].split('|') :
                        if key in ['校選修', '校必修', '院訂必修', '校選擇性必修']:
                            point1 += courseScore
                            point1List.append(i)
                        elif key in ['系專業必修', '院專業必修']:
                            point2 += courseScore
                            point2List.append(i)
                        elif key == '系專業選修':
                            point3 += courseScore
                            point3List.append(i)

                        matched = True
                        break
                if matched:
                    continue

            #系專業選修 額外計算 self.Extra_T3WhiteList
            if courseCode in self.Extra_T3WhiteList: 
                if i not in point3List:
                    point3 += courseScore
                    point3List.append(i)
                    print(f'[DT_ScoreQuery_V2][31003][系專業選修]:{courseName}|{courseCode} 已強塞至系專業選修')
                    matched = True

            if not matched:
                print(f"[DT_ScoreQuery_V2][FBI WARNING!!!]未匹配的課程: {courseName}|{courseCode}")
                FBIWarningText+=f"未匹配的課程: {courseName}|{courseCode}\n"
        print("[DT_ScoreQuery_V2]比對結束")
        
        ScoreDataDict2={'校選修_校必修_院訂必修_校選擇性必修':point1List,
            '系專業必修_院專業必修':point2List,
            '系專業選修':point3List,
            }
        return {
            'GlobalScoreData':GlobalScoreData,
            'ScoreDataDict':ScoreDataDict,
            'ScoreDataDict2':ScoreDataDict2,
            'FBIWarningText':FBIWarningText,
            'Score':Score,
            'point1':point1,
            'point2':point2,
            'point3':point3,
            'pointS1':pointS1,
            'pointS1BlackList':pointS1BlackList,
                }



    def DT_ScoreQuery_V2_SQL(self):
        
        ScoreDataDict=self.getScoreQueryDataV2() 
        #GlobalScoreData =self.getGlobalScoreData()

        Score=0
        for data in ScoreDataDict:
            Score += data["學分"]
        # 初始化數據 S1:通職
        point1 = 0
        point1List=[]
        point2 = 0
        point2List=[]
        point3 = 0
        point3List=[]
        pointS1 = 0
        pointS1List=[]
        pointS1BlackList=[]
        FBIWarningText=''
        unPassList=[]
        #PreRetServerCmdText=""

        print("[DT_ScoreQuery_V2_SQL]比對開始")
        # 遍歷 學生ScoreData
        
        conn = sqlite3.connect('SQL/ScoreQuery_Global.db')
        
        with conn:
            cur = conn.cursor()

            try:
                stdInfo = self.getPage_Graduation()
                stdInfo_DeptName = stdInfo['系別名稱']

                cur.execute(f"SELECT DeptID FROM AllDeptInfo WHERE DeptName='{stdInfo_DeptName}';")
                DT_Rows = cur.fetchall()
                stdInfo_DeptID = DT_Rows[0][0]

            except Exception as e:
                print(f'尋找系別名稱失敗 {e} 將使用預設值IM')
                stdInfo_DeptName="IM"


            for i in ScoreDataDict:
                courseName = i['科目名稱']
                courseCode = i['課號']
                courseScore = i['學分']
                courseChengJi = i['成績']
                #i["學年-學期"]
                matched = False
                bIsPass = True

                #判定Pass狀態
                if courseChengJi < 60:
                    bIsPass = False
                    unPassList.append(i)

                #篩掉服務&勞作
                if courseName == '服務學習基礎課程' or courseName == '勞作教育(二)' or courseName == '勞作教育(一)':
                    continue    
                #依課號Select
                cur.execute(f"SELECT ClassType FROM {stdInfo_DeptID} WHERE ClassID='{courseCode}' AND Year = {self.stdInfo_Year};")
                DT_Rows = cur.fetchall()
                #print(courseCode,bool(DT_Rows))
                if DT_Rows:
                    #課號撞車提示 報錯但不中斷
                    if len(DT_Rows) != 1 :
                        FBIWarningText+=f'[DT_ScoreQuery_V2_SQL][FBI WARNING!!!]:查詢時出現重複課號({courseCode}),查詢解果:{DT_Rows})\n'
                        print(f'[DT_ScoreQuery_V2_SQL][FBI WARNING!!!]:查詢時出現重複課號({courseCode}),查詢解果:{DT_Rows})')
                    DT_clsType = DT_Rows[0][0]
                    if DT_clsType in ['校選修', '校必修', '院訂必修', '校選擇性必修']:
                        point1 += courseScore
                        point1List.append(i)
                        
                    elif DT_clsType in ['系專業必修', '院專業必修']:
                        point2 += courseScore
                        point2List.append(i)
                        
                    elif DT_clsType == '系專業選修':
                        point3 += courseScore
                        point3List.append(i)
                    else: #不該有這情況
                        print(DT_clsType)
                    #通職 額外計算 通職課號(CS22E xxx 固定CS22 + A~F (表領域1-6))
                    if DT_clsType in ['校選擇性必修'] :
                        if courseCode[4:5] not in pointS1BlackList:
                            pointS1 += 1
                            pointS1List.append(i)
                            pointS1BlackList.append(courseCode[4:5])
                            
                        else:
                            FBIWarningText+=f'[DT_ScoreQuery_V2_SQL][FBI WARNING!!!][通職類檢測]:{courseName|courseCode} 通職包含重複課號類({courseCode[4:5]},當前名單:{pointS1BlackList})\n'
                            print(f'[DT_ScoreQuery_V2_SQL][FBI WARNING!!!][通職類檢測]:{courseName|courseCode} 通職包含重複課號類({courseCode[4:5]},當前名單:{pointS1BlackList})')
                    continue
                    #matched = True

                print(f"[DT_ScoreQuery_V2_SQL][INFO]({courseCode})不存在 將使用名稱查詢")
                cur.execute(f"SELECT ClassType FROM {stdInfo_DeptID} WHERE ClassName LIKE '{courseName}|%' AND Year = {self.stdInfo_Year};")
                DT_Rows = cur.fetchall()
                #依科目名稱 (名稱查詢撞車率高 一定要先檢查DT行數是否=1)
                if DT_Rows:
                    DT_clsType = DT_Rows[0][0]
                    if len(DT_Rows) == 1:
                        if DT_clsType in ['校選修', '校必修', '院訂必修', '校選擇性必修']:
                            point1 += courseScore
                            point1List.append(i)
                        elif DT_clsType in ['系專業必修', '院專業必修']:
                            point2 += courseScore
                            point2List.append(i)
                        elif DT_clsType == '系專業選修':
                            point3 += courseScore
                            point3List.append(i)
                        matched = True
                    else:
                        WarningText=f'[DT_ScoreQuery_V2_SQL][FBI WARNING!!!]: 依課程名稱查詢時撞車，名稱：{courseName}, dt長度：{len(DT_Rows)}'
                        FBIWarningText+=f'{WarningText}\n'
                        print(WarningText)
                #皆無法匹配
                else:
                    #系專業選修 額外計算 self.Extra_T3WhiteList
                    if courseCode in self.Extra_T3WhiteList: 
                        if i not in point3List:
                            point3 += courseScore
                            point3List.append(i)
                            print(f'[DT_ScoreQuery_V2_SQL][31003][系專業選修]:{courseName}|{courseCode} 已塞至系專業選修')
                            matched = True
                    if not matched:
                        print(f"[DT_ScoreQuery_V2_SQL][FBI WARNING!!!]未匹配的課程: {courseName}|{courseCode}")
                        FBIWarningText+=f"未匹配的課程: {courseName}|{courseCode}\n"
                courseName = i['科目名稱']
                courseCode = i['課號']
                courseScore = i['學分']
                courseChengJi = i['成績']
                
        print("[DT_ScoreQuery_V2_SQL]比對結束")
        
        ScoreDataDict2={'校選修_校必修_院訂必修_校選擇性必修':point1List,
            '系專業必修_院專業必修':point2List,
            '系專業選修':point3List,
            '未通過':unPassList
            }
        return {
            'GlobalScoreData':'hi',
            'ScoreDataDict':ScoreDataDict,
            'ScoreDataDict2':ScoreDataDict2,
            'FBIWarningText':FBIWarningText,
            'Score':Score,
            'point1':point1,
            'point2':point2,
            'point3':point3,
            'pointS1':pointS1,
            'pointS1BlackList':pointS1BlackList,
                }


    #--------------------------[Page處理]End--------------------------
    def getScoreQueryDataV2(self):
        self.Extra_T3WhiteList = []

        urlScoreQuery=f'https://www.lhu.edu.tw/StudAp/Nlhu/ChangePage.aspx?FID=B1004B'
        r = self.MainSession.get(urlScoreQuery)
        data=r.text
        #f = open('學分.html','r',encoding='utf8')
        #data=f.read()

        soup = BeautifulSoup(data.replace('<br>',"").replace('<br/>',"").replace('<BR>',""), 'html.parser')
        tables = soup.find_all('fieldset')
        ScoreData = []

        for table in tables:
            legend = table.find('legend')
            if legend and ("必修學分" in legend.text or "選修學分" in legend.text):
                rows = table.find('table').find_all('tr')[1:]  # 砍掉標題
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) == 6:  # 只提6欄的table數據
                        學年 = columns[0].text.strip()
                        學期 = columns[1].text.strip()
                        課號 = columns[2].text.strip()
                        科目名稱 = columns[3].text.strip()
                        學分 = columns[4].text.strip().split('/')[0].strip()  #'1.00 / 2.00' -> 1
                        學分 = int(float(學分))  
                        成績 = columns[5].text.strip()
                        if 成績 == '' or 成績 == '不通過' or 成績 == '撤選':
                            成績 = 0
                        elif  成績 == '通過':
                            成績 = 100
                        else:
                            try:
                                成績 = int(float(成績))
                            except:
                                print(f'[FBIWARNING!!!][40326]成績轉換錯誤：{成績}')
                                成績 = 0
                        if 科目名稱 == '服務學習基礎課程' or 科目名稱 == '勞作教育(二)' or 科目名稱 == '勞作教育(一)':
                            continue

                        #學期 = f"{學年}-{學期}" 
                        ScoreData.append({
                            "學期" : 學期,
                            "學年-學期": f"{學年}-{學期}" ,
                            "課號": 課號,
                            "科目名稱": 科目名稱,
                            "學分": 學分,
                            "成績": 成績
                        })
                        if "選修學分" in legend.text:
                            self.Extra_T3WhiteList.append(columns[2].text.strip())

        return(ScoreData)
    

    def getGlobalScoreData(self,year):
        #if os.path.exists('ScoreQuery_Global.json'):
        #    with open('ScoreQuery_Global.json' , 'r',encoding='utf-8') as f:
        #        GlobalScoreData = json.load(f)
        #        return GlobalScoreData
        host = 'https://www.lhu.edu.tw/oapx/lhuplan/Subject/'
        #學年,系所名,學制,配當表類別
        param=(year,310,'D24','A')
        url = f'{host}/ASubject_QryD.aspx?TYear={param[0]}&TDept={param[1]}&TSchoolSys={param[2]}&TASubKind={param[3]}'
        #html = 
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        #zlib.crc32(source_file.read())

        table = soup.find('table')
        data = []
        skiprows_Main = 3

        def getDataByTable(url2,szType):
            soup = BeautifulSoup(requests.get(url2).content, 'html.parser')
            table = soup.find('table')
            data = []
            skip_rows = 3
            for row in table.find_all('tr'):
                if skip_rows > 0:
                    skip_rows -= 1
                    continue
                row_dataList = []
                cells = row.find_all(['td', 'th'])
                #row_dataList 按格遍歷&append
                for cell in cells:
                    rowspan = int(cell.get('rowspan', 1))
                    cellRaw = str(cell).replace('<br/>', '|')
                    cellText = BeautifulSoup(cellRaw, 'html.parser').get_text(strip=True)

                    #篩掉最底下兩格
                    if cellText == '注意事項' or cellText == '異動記錄':
                        break
                    for i in range(rowspan): 
                        if i == 0:
                            row_dataList.append(cellText)
                if row_dataList:
                    if row_dataList[0] == '小計': 
                        continue
                    if row_dataList and row_dataList[0] != szType:
                        row_dataList.insert(0, szType)
                    data.append(row_dataList)
            return data
        
        for row in table.find_all('tr'):
            if skiprows_Main > 0:
                skiprows_Main -= 1
                continue

            row_dataList = []
            extraDT = []
            cells = row.find_all(['td', 'th'])
            bTemp = True #注意事項 提取標記
            #row_dataList 按格遍歷&append
            for cell in cells:
                rowspan = int(cell.get('rowspan', 1))

                cellRaw = str(cell).replace('<br/>', '|')
                cellText = BeautifulSoup(cellRaw, 'html.parser').get_text(strip=True)
                        
                if rowspan > 1:
                    szType = cellText
                    
                #最底下兩格 特殊處理
                if cellText == '注意事項' :
                    bTemp = False
                    continue
                if cellText == '異動記錄':
                    break


                if bTemp:
                    for i in range(rowspan): 
                        if i == 0:
                            row_dataList.append(cellText)
                else:
                    pass
                    #print(cellText)

                if '詳見通識中心' in cellRaw:
                    link = cell.find('a')
                    extracted_url = host+link.get('href')
                    extraDT=getDataByTable(extracted_url,szType)

            if row_dataList:
                if row_dataList[0] == '小計': 
                    continue
                if row_dataList and row_dataList[0] != szType:
                    row_dataList.insert(0, szType)
                data.append(row_dataList)
            if extraDT:
                data=extraDT+data
        #print(extraDT)
        resultList = []
        for row in data:
            resultList.append({
                "類別": row[0],
                "課號": row[1],
                "科目名稱": row[2],
                "學分": row[3],
#                "Term1_1":row[4], "Term1_2":row[4], "Term2_1":row[4], "Term2_2":row[4], 
#                "Term3_1":row[4], "ermT3_2":row[4], "Term4_1":row[4], "Term4_2":row[4], 
#                "備註": row[14],
            })
        #額外追加
        #if param==(110,310,'D24','A'):
        extraList = self.getGlobalScoreData_TongZhi(param[0])
        for Litem in extraList:
            contains_cs = any(Litem["課號"] in d.values() for d in resultList)           
            if contains_cs:
                pass
            else:
                resultList.append(Litem)
            
        #resultList.append({
        #    "類別": '校必修',
        #    "課號": 'CS21N002',
        #    "科目名稱": '簡報技巧|溝通表達領域(任選一門)',
        #    "學分": '2', })

        resultDict = {}
        #按類別分割
        for item in resultList:
            category = item["類別"]
            if category not in resultDict:
                resultDict[category] = []
            resultDict[category].append(item)
        #測試用
        with open('ScoreQuery_Global.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(resultDict, ensure_ascii=False, indent=4))
        return resultDict

    def getGlobalScoreData_TongZhi(self,year):
        url=f'https://www.lhu.edu.tw/oapx/lhuplan/query/course_qry.aspx'
        r22 = self.MainSession.get(url)
#        print(r22.text)
        #提VIEWSTATE
        soup = BeautifulSoup(r22.text, 'html.parser')
        form = soup.find('form')
        __VIEWSTATE = form.find('input', {'name': '__VIEWSTATE'})['value']
        __EVENTVALIDATION = form.find('input', {'name': '__EVENTVALIDATION'})['value']
        data = {
            '__VIEWSTATE': __VIEWSTATE,
            "__EVENTVALIDATION":__EVENTVALIDATION,
            'TB_TYear': str(year),
            'TB_TTerm': '1',
            'DDL_Dept': 'B40',
            'TB_SubName': '',
            'TB_TeaName': '',
            'TB_Room': '',
            'Btn_Qry': '開始查詢'
        }

        r = self.MainSession.post(url, data=data)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.findAll('table')[2]
        resultList = []
        skip_rows = 1
        for row in table.find_all('tr'):
            if skip_rows > 0:
                skip_rows -= 1
                continue
            row_dataList = []
            cells = row.find_all(['td', 'th'])
            #row_dataList 按格遍歷&append
#            for cell in cells:
#                rowspan = int(cell.get('rowspan', 1))
#                cellRaw = str(cell).replace('<br/>', '|')
#                cellText = BeautifulSoup(cellRaw, 'html.parser').get_text(strip=True)
#            print(cells[3].get_text(strip=True)) #.split('|')
            clsType = cells[4].get_text(strip=True)
            clsNum = os.path.splitext(os.path.basename(cells[1].find('a').get('href')))[0]
            clsName = cells[3].get_text(strip=True)
            if clsType == "選擇性必修":
                clsType = "校選擇性必修"

            elif clsType == "必修":
                clsType = "校必修"
            else:
                continue
            #elif clsType == "選修":
            #    clsType = ""
            if clsName == "學生時間":
                break
            tmp = {
                "類別": clsType,
                "課號": clsNum,
                "科目名稱": clsName,
                "學分": cells[5].get_text(strip=True).split('-')[2] }
            if tmp not in resultList:
                resultList.append(tmp)
#        print(resultList)

        return resultList


if __name__ == '__main__':
    
    lhuAuth=lhuFunc()
    lhuAuth.login("0","0")
    print(lhuAuth.getPage_SpeechEvent())
