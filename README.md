# 畢業門檻查詢&amp;輔助程式 (開發中)

#### 使用語言：Python
#### UI：PyQt6
#### 打包工具：Nuitka


# 首頁

<img src="https://github.com/DMCDN/LHWork/assets/128150279/2996341d-3e70-4079-94a0-df42a4421426" width="300" height="300">

# 門檻總覽
* 列出所有畢業門檻的通過狀態，以及通過所需/剩餘條件

<img src="https://github.com/DMCDN/LHWork/assets/128150279/f89f3d9a-dc7e-4aa5-803d-d647d07db922" width="500" height="300">

# 應修學分查詢
* 提取該學生的修課資訊、所屬科系與學年後，在依[課程配當表](https://www.lhu.edu.tw/oapx/lhuplan/Subject/ASubject_Qry.htm)的資料做分類

* 分類出選修、必修、通識、專業選修四種學分的完成度，免去學生手動一個個比對的麻煩

* 課程配當表資料先使用爬蟲提取、處理，最後使用SQLite資料庫保存


<img src="https://github.com/DMCDN/LHWork/assets/128150279/cc3fa286-30ac-41f6-88d8-804186a11e3e" width="600" height="500">

# 勞作教育查詢/報名
* 即時爬取所有現可報名的活動後，在依學生要求做時間分類(上午、下午)
  
* 點擊即可查看詳情，在點擊確認即可報名，並同步至校網登記報名
  
https://github.com/DMCDN/LHWork/assets/128150279/1fe423a3-616f-4af0-87fc-8e69d5e8ae28

# 服務學習查詢/報名
* 功能同上(勞作教育查詢/報名)
  
* 可篩選出兩種活動類型
<img src="https://github.com/DMCDN/LHWork/assets/128150279/4671308b-a924-4734-837a-e0995de61e29" width="800" height="500">


## 已滿活動預定
* 紀錄欲報名卻已滿的活動
  
* 每10分鐘查詢一次列表中的活動是否有人退選，若有則自動報名，反之再等待10分鐘查詢，以此循環

  
https://github.com/DMCDN/LHWork/assets/128150279/4eafa9ee-56ed-404c-afc1-b14b6d6f6a61



# 證照|非正式課程查詢
* 目前僅支持查詢與完成所需條件提示

<img src="https://github.com/DMCDN/LHWork/assets/128150279/7724a03a-e332-4124-a5cc-93d21c564ba5" width="600" height="300">

# 缺曠情況查詢
* 列出該學生的缺曠情況
  
* 若曠課次數高於(節數*6)，學生會被扣考，在接近此數值時警告學生

<img src="https://github.com/DMCDN/LHWork/assets/128150279/931c8a4f-7974-4906-ac45-a5b1056a3603" width="500" height="300">


# 附加作品

###### 軟體更新/啟用驗證程式 (https://github.com/DMCDN/QTUpdate)

###### 軟體介紹/下載/啟用網站 (https://lwork.pythonanywhere.com/)
