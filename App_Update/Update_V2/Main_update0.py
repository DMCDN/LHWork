import sys
import os

from resDReader import respdb
import atexit

mainAppPath=os.path.dirname(sys.argv[0]) 

Decoder=respdb().DecodeFile
for i in sys.argv[1:]:

    with open(i, "rb") as r:
        with open(i[:-5], "wb") as f:
            f.write(Decoder(r.read(),fname=i[:-5]))
    os.remove(i)


atexit.register(os.execl, f'{mainAppPath}/Main_update.exe', f'{mainAppPath}/Main_update.exe')