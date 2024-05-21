import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
#import codecs
import lz4.block
import lzma
import zstandard as zstd
#import hashlib

ZipAlgorithms = {
    "zstd": (zstd.ZstdCompressor(level=10), zstd.ZstdDecompressor(max_window_size=2147483648)),
}
#"zlib": (zlib.compressobj(), zlib.decompressobj())




class respdb:
    class respdbError(Exception):
        def __init__(self, message):
            super().__init__(message)
            self.message = message

    def __init__(self ):
        self.HeaderKey=b'\xE3\x05\x62\x14\xD6\x0A\x20\x25\x36\x96\x1B\x07\x74\xDC\x24\x02'
        self.HeaderIV=b'\x1D\x6E\xEB\x4C\x86\xA9\x45\x44\x45\x72\x12\x21\x2B\x43\x25\x2F'
  
    def DecodeFile_f(self,f,fname=""):
        header = f.read(2)
        bEncryptType = int.from_bytes(f.read(1), byteorder='little') 
        #1=lz4 2=lzma
        bCompressType = int.from_bytes(f.read(1), byteorder='little') 
        rawSize = f.read(4)
        data = f.read()
        #解密→解壓
        if bEncryptType:
            pass
        if bCompressType == 1:
            data = self.decompress_lz4(data,rawSize)
        elif bCompressType == 2:
            data = lzma.decompress(data,format=lzma.FORMAT_ALONE)
        elif bCompressType == 3:
            data = ZipAlgorithms['zstd'][1].decompress(data)
        return data

    def DecodeFile(self,data,fname=""):
    
        header = data[0:8]
        bEncryptType = int.from_bytes(header[2:3], byteorder='little') 
        #1=lz4 2=lzma
        bCompressType = int.from_bytes(header[3:4], byteorder='little') 
        rawSize = int.from_bytes(header[4:8], byteorder='little') 

        data = data[8::]

        print(self.GetBasenameFromPath(fname),bEncryptType,bCompressType,)

        #解密
        if bEncryptType == 0:
            pass
        elif bEncryptType == 1:
            data = self.decryptRaw(self.GetBasenameFromPath(fname),data)
        else:
            raise self.respdbError(f"未知的加密格式：{bEncryptType}")

        #解壓
        if bCompressType == 0:
            pass
        elif bCompressType == 1:
            data = self.decompress_lz4(data,rawSize)
        elif bCompressType == 2:
            data = lzma.decompress(data,format=lzma.FORMAT_ALONE)
        elif bCompressType == 3:
            data = ZipAlgorithms['zstd'][1].decompress(data)
        else:
            raise self.respdbError(f"未知的壓縮格式：{bCompressType}")

        return data

    def EncodeFile(self,data, bEncrypt,bCompress ,fname=""):

        mMagic = b'PH'
        rawSize=len(data).to_bytes(4, 'little')  
        
        header = mMagic+bEncrypt+bCompress+rawSize


        if bCompress == b'\x01':
            data = self.compress_lz4(data)
        if bCompress == b'\x02':
            data = lzma.compress(data,format=lzma.FORMAT_ALONE)
        if bCompress == b'\x03':
            data = ZipAlgorithms['zstd'][0].compress(data)

        if bEncrypt == b'\x01':
            data = self.encryptRaw(self.GetBasenameFromPath(fname),data)
            
#            data=self.AES_CBC_encrypt(data, self.GetMixedKey()
        return (header + data)


    #def Encode_Compress(self,data,bCompressType):
    #    if bEncryptType:
    #        pass
    #    return data

    #
    def GetBasenameFromPath(self,fpath):
        fnameWithoutEXT =  os.path.splitext(os.path.basename(fpath))[0]
        return fnameWithoutEXT

    def decryptRaw(self,resName,data):
        return self.AES_CBC_decrypt(data, self.GetMixedKey(self.GetBasenameFromPath(resName),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), bytearray(16))
    def encryptRaw(self,resName,data):
        return self.AES_CBC_encrypt(data, key=self.GetMixedKey(self.GetBasenameFromPath(resName),bytes.fromhex("50CC9BCCB7CDA275D289D289CCB7D289")), iv=bytearray(16))

    #LZ4
    def decompress_lz4(self,data: bytes, uncompressed_size: int) -> bytes:  # LZ4M/LZ4HC
        return lz4.block.decompress(data, uncompressed_size)
    def compress_lz4(self,data: bytes) -> bytes:  # LZ4M/LZ4HC
        return lz4.block.compress(
            data, mode="high_compression", compression=9, store_size=False
        )
    
    #AES
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
        return encrypt_data
    
        if len(data) % 16 == 0:
            return encrypt_data[0:len(data)]
        else:
            return encrypt_data


    #key二層處理 
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
    

if __name__ == '__main__':
    
    #with open('builder.pyd1','rb') as fff:
    #    dt=fff.read()
    #with open('builder.pyd2','wb') as fff:
    #    #fff.write(respdb().EncodeFile(dt, b'\x01',b'\x03' ,fname="builder.pyd"))
    #    fff.write(respdb().encryptRaw(data=dt,resName="builder.pyd"))
        
    with open('builder.pyd2','rb') as fff:
        dt=fff.read()
    with open('builder.pyd3','wb') as fff:
        fff.write(respdb().decryptRaw(data=dt,resName="builder.pyd"))

    #with open('builder.pyd2','rb') as fff:
    #    dt=fff.read()
    #with open('builder.pyd3','wb') as ff:
    #    dataa=ZipAlgorithms['zstd'][1].decompress(dt)
    #    ff.write()
