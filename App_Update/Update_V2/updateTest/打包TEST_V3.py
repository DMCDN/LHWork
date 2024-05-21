import os
import json
import zlib
from resDReader import respdb

from databin import BinaryStream

resPath = "outPut/Main.dist/"
resData = "outPut/patch.res"
resDataDiff = "outPut/patch.resdiff"
resDataDiffJson = f"outPut/patch_New.bytes"
appVersion = "1.0.0"
resVersion = 2

diffData = {"Version" : appVersion ,
            "resVersion":resVersion,
            "AllVersionResInfo":{} }

Decoder=respdb().DecodeFile_f
Encoder=respdb().EncodeFile

"""
with open(f'patch.bytes','rb') as fJson:
    oldDiff = json.loads(Decoder(fJson).decode('utf-8'))

if appVersion == oldDiff["Version"]:
    #AllVersionResInfo疊加
    oldDiff["AllVersionResInfo"][1]
else:
    #AllVersionResInfo清空
    pass
"""
#bFileType 0:文件 1:資料夾 2:壓縮包
rList = []
dwOffsetStart = 0
dwOffsetEnd = 0
with open(resData, "wb") as pdb:
    for root, dirs, files in os.walk(resPath):
        # 文件夹
        for dir_name in dirs:
            tmpDiffInfo = {
                "szPath": os.path.join(root, dir_name).replace(f'{resPath}',''),
                "dwOffset": 0,
                "dwSize": 0,
                "dwCrc": 0,
                "bFileType": 1
            }
            rList.append(tmpDiffInfo)
        for file in files:
            fPath = os.path.join(root, file)
            
            # CRC32
            with open(fPath, "rb") as f:
                crc_value = zlib.crc32(f.read())

            #結構 初始化
            bEncrypt = b'\x00'
            bCompress = b'\x00'

            with open(fPath, "rb") as fSource:
                data = fSource.read()

            #小於1kb不壓縮 其餘全壓
            if os.path.getsize(fPath) < 1024 : #小於10kb
                bCompress = b'\x00'

            elif os.path.getsize(fPath) < 1024000000 : #lzma 小於1000mb 
                bCompress = b'\x02'
            else :# lz4
                bCompress = b'\x01'
            #print(os.path.getsize(fPath),bCompress)


            data = Encoder(data,bEncrypt,bCompress)
            #pdb.write(header)

            tmpDiffInfo = {
                "szPath": os.path.relpath(fPath, resPath),
                "dwOffset": pdb.tell(),
                "dwSize": len(data),
                "dwCrc": crc_value,
                "bFileType":0
            }
            dwOffsetEnd += len(data)
            rList.append(tmpDiffInfo)
            pdb.write(data)

rtems = {resVersion:rList}
diffData.update({
"AllVersionResInfo": {resVersion : {"dwOffsetStart": dwOffsetStart,
                    "dwOffsetEnd": dwOffsetEnd,
                    "iResCount":len(rList),
                    "ResInfoList":rList}}
                      })

with open(resDataDiffJson, "wb") as fJson:
    #json.dumps(fJson, indent=2)
    jsonStrData = json.dumps(diffData, indent=2)
    fJson.write(Encoder(jsonStrData.encode('utf-8'),b'\x00',b'\x00')) #暫時用lz4 dw data多壓縮意義不大
"""
with open(resDataDiff, "wb") as f:
    diffBytes = BinaryStream(f)
    diffBytes.writeUInt32(len(diffData))
    for i in diffData:
        diffBytes.writeString16(i["szPath"])
        diffBytes.writeUInt32(i["dwOffset"])
        diffBytes.writeUInt32(i["dwSize"])
        diffBytes.writeUInt32(i["dwCrc"])
        diffBytes.writeByte(i["bFileType"])
"""
    
