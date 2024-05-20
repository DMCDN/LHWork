# 畢業門檻查詢&amp;輔助程式

#### 使用語言：Python
#### UI：PyQt6
#### 打包工具：Nuitka


## 首頁

<img src="https://github.com/DMCDN/LHWork/assets/128150279/2996341d-3e70-4079-94a0-df42a4421426" width="300" height="300">

## 門檻總覽
* 列出所有畢業門檻的通過狀態，以及通過所需/剩餘條件

<img src="https://github.com/DMCDN/LHWork/assets/128150279/f89f3d9a-dc7e-4aa5-803d-d647d07db922" width="500" height="300">

## 應修學分查詢
* 提取該學生的修課資訊、所屬科系與學年後，在依[課程配當表](https://www.lhu.edu.tw/oapx/lhuplan/Subject/ASubject_Qry.htm)的資料做分類

* 分類出選修、必修、通識、專業選修四種學分的完成度，免去學生手動一個個比對的麻煩

* 課程配當表資料先使用爬蟲提取、處理，最後使用SQLite資料庫保存


<img src="https://github.com/DMCDN/LHWork/assets/128150279/cc3fa286-30ac-41f6-88d8-804186a11e3e" width="600" height="500">

## 勞作教育查詢/報名
* 即時爬取所有現可報名的活動後，在依學生要求做時間分類(上午、下午)
  
* 點擊即可查看詳情，在點擊確認即可報名，並同步至校網登記報名
  
https://github.com/DMCDN/LHWork/assets/128150279/1fe423a3-616f-4af0-87fc-8e69d5e8ae28

## 服務學習查詢/報名
* 功能同上(勞作教育查詢/報名)
  
* 可篩選出兩種活動類型
<img src="https://github.com/DMCDN/LHWork/assets/128150279/4671308b-a924-4734-837a-e0995de61e29" width="800" height="500">


### 已滿活動預定
* 紀錄欲報名卻已滿的活動
  
* 每10分鐘查詢一次列表中的活動是否有人退選，若有則自動報名，反之再等待10分鐘查詢，以此循環

  
https://github.com/DMCDN/LHWork/assets/128150279/4eafa9ee-56ed-404c-afc1-b14b6d6f6a61



## 證照|非正式課程查詢
* 目前僅支持查詢與完成所需條件提示

<img src="https://github.com/DMCDN/LHWork/assets/128150279/7724a03a-e332-4124-a5cc-93d21c564ba5" width="600" height="300">

## 缺曠情況查詢
* 列出該學生的缺曠情況
  
* 若曠課次數高於(節數*6)，學生會被扣考，在接近此數值時警告學生

<img src="https://github.com/DMCDN/LHWork/assets/128150279/931c8a4f-7974-4906-ac45-a5b1056a3603" width="500" height="300">


# 更新與啟用狀態驗證程式

根據專題軟體的打包方式所設計的更新程式

同樣使用PyQt6製作UI，文件壓縮使用Zstd與LZMA

## 特點：
* 盡可能地縮短更新所需總時間
* 文件均經壓縮處理，並僅須下載差異文件
* 使用多線程下載&解壓
* 配製簡易(一份版本訊息、兩份patch包)
        
 ## 打包：
#### 將指定目錄下的所有文件打包成兩份文件
* patch.res (所有文件經處理&合併後的資源包)
* patch.resdiff  (紀錄文件，紀錄所有文件的：路徑、crc32值、Offset、Size)

## patch.res
#### 考量到時間成本(解壓+下載時間總長)
* 預設情況使用Zstd壓縮，某些特殊文件使用AES加密

* 以下情況使用lzma壓縮：
  
    文件大於100mb
    
    壓縮比不小於0.9
  
* 以下情況不做壓縮：
  
    文件小於1kb
    
    壓縮比小於0.9

* 最後將該文件的壓縮/加密方法標記於頭部後，再拼入Patch包的後方

#### 自建文件結構
* File Signature(2bytes)
* 加密方法 (1byte)
* 壓縮方法 (1byte)
* 文件原始大小 (4bytes)
* 其餘則為加密/壓縮處理後資料

 ![螢幕擷取畫面 2024-05-03 184810](https://github.com/DMCDN/QTUpdate/assets/128150279/6bb7267d-d009-4fec-a619-31fbcdb1c0a8)
 
## patch.resdiff
![image](https://github.com/DMCDN/QTUpdate/assets/128150279/6f70f552-7dab-4378-a40b-56b8f7c5a42e)
* 紀錄每個文件在patch.res中的訊息
* 根據紀錄文件提供的路徑、Offset與size 開始創建下載程序
* requests header的參數則為 ({"Range": "bytes={offset}-{offset+size-1}"})
  
## 更新
* 下載前，比對VersionConfig與軟體紀載的版本是否相同
* 若不匹配，開始分析本地的所有文件與記錄文件(patch.resdiff)的crc32值
* 接著下載&解壓差異文件

## 實機畫面
https://github.com/DMCDN/QTUpdate/assets/128150279/fc788936-c14f-48de-9668-670f0414a4e5

## 檢查軟體啟用狀態

網頁使用Flask與SQLite製作一個檢查序號用的API

首次使用有1小時試用時間，到期則會要求將程式顯示的序號，輸入至網站的啟用頁面

透過進入 https://lwork.pythonanywhere.com 購買啟用權限輸入

https://github.com/DMCDN/QTUpdate/assets/128150279/cb95f7f4-4fb5-471c-a339-59f108c79881



#### 軟體介紹/下載/啟用網站(開發中) [https://lwork.pythonanywhere.com/]

目前已實際完成的功能：

- 註冊與登入
  
  ![image](https://github.com/DMCDN/LHWork/assets/128150279/dbeaea47-aa0e-4dbc-aab4-719d8edccbac)

- 信箱驗證功能
  
    ![image](https://github.com/DMCDN/LHWork/assets/128150279/edcfe31e-2c58-4984-b8ee-e9558eebd85e)

- 產品啟用功能
  
      設計一個API，給軟體的啟用狀態檢測系統使用
  
    ![image](https://github.com/DMCDN/LHWork/assets/128150279/fa29b6ba-05f6-4292-a604-cbbc52e52cb4)
  

- 各科通過率
  
  ![image](https://github.com/DMCDN/LHWork/assets/128150279/3bd440d0-ec49-4178-8b1f-e97e5084437f)


