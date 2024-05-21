from struct import *
 
class BinaryStream:
    def __init__(self, base_stream):
        self.base_stream = base_stream

    def readRest(self):
        return self.base_stream.read()

    def readByte(self):
        dt = self.base_stream.read(1)
        
        return int.from_bytes(dt, byteorder='little') 

    def readByteArray(self):
        lens = self.unpack('i', 4)
        return self.base_stream.read(lens)

    def readBytes(self, length):
        return self.base_stream.read(length)

    def readChar(self):
        return self.unpack('b')

    def readUChar(self):
        return self.unpack('B')

    def readBool(self):
        return self.unpack('?')

    def readInt16(self):
        return self.unpack('h', 2)

    def readUInt16(self):
        return self.unpack('H', 2)

    def readInt32(self):
        return self.unpack('i', 4)

    def readInt32Array(self):
        lens = self.unpack('i', 4)
        arr = []
        for i in range(lens):
            arr.append(self.unpack('i', 4))
        return arr

    def readUInt32(self):
        return self.unpack('I', 4)

    def readInt64(self):
        return self.unpack('q', 8)

    def readUInt64(self):
        return self.unpack('Q', 8)

    def readFloat(self):
        return self.unpack('f', 4)

    def readDouble(self):
        return self.unpack('d', 8)

    def readString(self,noNull=False):
        length = self.readUInt32()
        if noNull:
            return self.unpack(str(length) + 's', length).decode('utf-8')
        else:
            return self.unpack(str(length) + 's', length)[:-1].decode('utf-8')

    def readString16(self,noNull=False):
        length = self.readUInt16()
        if noNull:
            return self.unpack(str(length) + 's', length).decode('utf-8')
        else:
            return self.unpack(str(length) + 's', length)[:-1].decode('utf-8')

    """
    def readByteArray(self):
        length = self.readUInt32()
        if length == 0 :
            return b''
        else:
            return self.base_stream.read(length)
    """


    def writeBytes(self, value):
        self.base_stream.write(value)

    def writeChar(self, value):
        self.pack('c', value)

    def writeUChar(self, value):
        self.pack('C', value)

    def writeBool(self, value):
        self.pack('?', value)

    def writeInt16(self, value):
        self.pack('h', value)

    def writeUInt16(self, value):
        self.pack('H', value)

    def writeInt32(self, value):
        self.pack('i', value)

    def writeUInt32(self, value):
        self.pack('I', value)

    def writeInt64(self, value):
        self.pack('q', value)

    def writeUInt64(self, value):
        self.pack('Q', value)

    def writeFloat(self, value):
        self.pack('f', value)

    def writeDouble(self, value):
        self.pack('d', value)

    def writeString(self, value , NoNull=False):
        value=value.encode()
        if NoNull:
            length = len(value)
            self.writeUInt32(length)
            self.pack(f'{length}s', value)
        else:
            length = len(value)+1
            self.writeUInt32(length)
            self.pack(f'{length}s', value)
#            self.base_stream.write(b'\x00')

    def writeString16(self, value):
        value=value.encode()
        length = len(value)+1
        self.writeUInt16(length)
        self.pack(f'{length}s', value)


    def writeByteArray(self, value):
#        length = len(value)
#        self.writeUInt32(length)
        #arraySize=0直接pass
#        if length == 0:
#            pass
#        else:
            self.base_stream.write(value)

    def pack(self, fmt, data):
        return self.writeBytes(pack(fmt, data))

    def unpack(self, fmt, length = 1):
        return unpack(fmt, self.readBytes(length))[0]


