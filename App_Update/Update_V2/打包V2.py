import os
import json
import zlib
from resDReader import respdb

from databin import BinaryStream

resPath = "outPut/Main.dist"
resData = "outPut/patch.res"
resDataDiff = "outPut/patch.resdiff"
resDataDiffJson = "outPut/patch.json"

diffData = []

Decoder=respdb().DecodeFile_f
Encoder=respdb().EncodeFile

with open(resData, "wb") as pdb:
    for root, _, files in os.walk(resPath):
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
            if os.path.getsize(fPath) < 1024 :
                bCompress = b'\x00'
            elif os.path.getsize(fPath) < 1024000000 : #lzma 小於1000mb 
                bCompress = b'\x02'
            else :# lz4
                bCompress = b'\x01'
            print(os.path.getsize(fPath),bCompress)


            data = Encoder(data,bEncrypt,bCompress)
            #pdb.write(header)

            tmpDiffInfo = {
                "szPath": os.path.relpath(fPath, resPath),
                "dwOffset": pdb.tell(),
                "dwSize": len(data),
                "dwCrc": crc_value
            }
            diffData.append(tmpDiffInfo)
            
            pdb.write(data)

with open(resDataDiffJson, "w") as fJson:
    json.dump(diffData, fJson, indent=2)

with open(resDataDiff, "wb") as f:
    diffBytes = BinaryStream(f)
    diffBytes.writeUInt32(len(diffData))
    for i in diffData:
        diffBytes.writeString16(i["szPath"])
        diffBytes.writeUInt32(i["dwOffset"])
        diffBytes.writeUInt32(i["dwSize"])
        diffBytes.writeUInt32(i["dwCrc"])
    
