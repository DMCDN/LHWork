import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
#import codecs
import lz4.block
import lzma
import io
import tarfile
import json


class respkg:
    def __init__(self ):
        self.HeaderKey=b'\xE3\x05\x62\x14\xD6\x0A\x20\x25\x36\x96\x1B\x07\x74\xDC\x24\x02'
        self.HeaderIV=b'\x1D\x6E\xEB\x4C\x86\xA9\x45\x44\x45\x72\x12\x21\x2B\x43\x25\x2F'


    def decryptResWithPath(self,resName,bIsInUserProfile=True):
        if bIsInUserProfile:
            resName=os.path.join(os.environ['USERPROFILE'], resName)
        with open(resName, "rb") as f:
            data=f.read()
            data=self.AES_CBC_decrypt(data, self.GetMixedKey(os.path.basename(resName),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), bytearray(16))
        return data
    
    def decryptRaw(self,resName,data):
        return self.AES_CBC_decrypt(data, self.GetMixedKey(os.path.basename(resName),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), bytearray(16))
    def encryptRaw(self,resName,data):
        return self.AES_CBC_encrypt(data.encode(), key=self.GetMixedKey(os.path.basename(resName),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), iv=bytearray(16))


    def AES_CBC_decrypt(self,data,key=b'\xE3\x05\x62\x14\xD6\x0A\x20\x25\x36\x96\x1B\x07\x74\xDC\x24\x02',iv=b'\x1D\x6E\xEB\x4C\x86\xA9\x45\x44\x45\x72\x12\x21\x2B\x43\x25\x2F'):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypt_data = cipher.decrypt(data)
        try:
            decrypt_data=unpad(decrypt_data,16,'pkcs7')
        except:
            pass
        return decrypt_data
    
    def AES_CBC_encrypt(self,data,key=b'\xE3\x05\x62\x14\xD6\x0A\x20\x25\x36\x96\x1B\x07\x74\xDC\x24\x02',iv=b'\x1D\x6E\xEB\x4C\x86\xA9\x45\x44\x45\x72\x12\x21\x2B\x43\x25\x2F'):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padding=pad(data,16,style='pkcs7')
        encrypt_data = cipher.encrypt(padding)
        #return encrypt_data
        if len(data) % 16 == 0:
            return encrypt_data[0:len(data)]
        else:
            return encrypt_data

    def GetMixedKey(self,resName,mRawKeys=None):
        if mRawKeys is None:
            mRawKeys = bytearray(bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289"))
        else:
            mRawKeys =bytearray(mRawKeys)
        mIV=bytearray(16)
        v8 = int(self.GetStrUpperHash(resName))
        v10=len(mRawKeys)
        if (v10 << 32) >=1:
            v11=0
            v12=0
            while (v12<v10):
                v13=v8>>(v11&0x18)
                v11+=8
                mRawKeys[v12] ^= v13 & 0xff
                v12+=1
                if v12 >=v10:
                    return mRawKeys
        return mRawKeys
    
    def GetStrUpperHash(self,inAssetName: str):
        v2=len(inAssetName)
        if v2 < 1:
            return 0
        v4=0
        v5=0
        v6=0
        while v2 != v6:
            v6=v5+1
            v7=ord(inAssetName[v5].upper())
            v8=v7
            v4=31*v4+v8
            v5=v6
        return v4
    
    def checkJS(self,jsonList):
        for jsName in jsonList:
            userInfoPath = os.path.join(os.environ['USERPROFILE'], jsName)
            #加密版json初始化文件 
            try:
                open(userInfoPath)
                print("checkEncryptedJson_OK")
            except:
               with open(userInfoPath, "w") as outfile:
                   json.dump({}, outfile, ensure_ascii=False, indent=4)
               with open(userInfoPath, "wb") as f:
                   dictInfo=json.dumps({})
                   data=self.AES_CBC_encrypt(dictInfo.encode(), self.GetMixedKey(os.path.basename(userInfoPath),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), bytearray(16))
                   f.write(data)



if __name__ == '__main__':
    #respkg().EncryptPkg('res')
    pass