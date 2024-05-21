import os
import json
import requests
import zlib
from resDReader import respdb
from databin import BinaryStream
from io import BytesIO
Decoder=respdb().DecodeFile

def expand_short_url(url):
    r = requests.head(url, allow_redirects=False)
    r.raise_for_status()
    if 300 < r.status_code < 400:
        url = r.headers.get('Location', url)
    return url


resDir = "outPut/Main.dist"
#diffData = "diff.json"

print("下載完畢 解壓資源")
serverDiffData = expand_short_url("https://github.com/DMCDN/assets/releases/download/1/res.pdiff")
rawDataUrl = expand_short_url("https://github.com/DMCDN/assets/releases/download/1/res.pdb")

# 下载diff.json文件
diffBytes = requests.get(serverDiffData).content
diffBytes = BinaryStream(BytesIO(diffBytes))

serverDiff=[]
diffLen = diffBytes.readUInt32()
for i in range(diffLen):
    serverDiff.append({"szPath":diffBytes.readString16(),
                    "dwOffset":diffBytes.readUInt32(),
                    "dwSize":diffBytes.readUInt32(),
                    "dwCrc":diffBytes.readUInt32(),})


filesDataDict = {}

print("init")
for svDiff in serverDiff:
    crc = int(svDiff["dwCrc"])
    offset = int(svDiff["dwOffset"])
    size = int(svDiff["dwSize"])
    path = svDiff["szPath"]

    local_fpathFull = os.path.join(resDir, path)

    local_crc=0
    # 检查CRC是否匹配
    if os.path.exists(local_fpathFull):
        local_crc = zlib.crc32(open(local_fpathFull, "rb").read())

    if local_crc != crc:     

        print("正在下載",path)
        r = requests.get(rawDataUrl, headers={"Range": f"bytes={offset}-{offset+size-1}"})

        if r.status_code == 206:
            
            filesDataDict[path] = r.content
        else:
            print(f"not 206：{path}")



print("下載完畢 解壓資源")
# 移除本地多餘path
"""
with open(diffData, "r") as local_diff:
    local_diff_data = json.load(local_diff)
for local_file in local_diff_data:
    if local_file["path"] not in [svDiff["path"] for svDiff in serverDiff]:
        # 删除本地文件
        local_file_path = os.path.join(resDir, local_file["path"])
        os.remove(local_file_path)
"""

for path, data in filesDataDict.items():
    local_fpath = os.path.join(resDir, path)
    if not os.path.exists(os.path.dirname(local_fpath)):
        os.makedirs(os.path.dirname(local_fpath))
    print("解壓",local_fpath)
    with open(local_fpath, "wb") as local_file:
        local_file.write(Decoder(data))
        

print("更新完成。")
