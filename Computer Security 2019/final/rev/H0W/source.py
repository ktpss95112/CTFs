# Python bytecode 3.7 (3394)
# Embedded file name: H0W.py
# Size of source mod 2**32: 387 bytes
# Decompiled by https://python-decompiler.com
import sys, struct
from terrynini import *
if len(sys.argv) != 2:
    print('Usage: python3 H0W.py filename')
    exit(0)
nini3() # fopen
f = open(sys.argv[1], 'rb').read()
if len(f) % 4 != 0:
    f += (4 - len(f) % 4) * '\x00'
nini1() # time
nini4() # srand
for i in range(0, len(f), 4):
    nini6( # fwrite
        nini5(struct.unpack('<i', f[i:i + 4])[0]) # rand
        # struct.unpack('<i', f[i:i + 4])[0]  --->  u32(f[i:i+4])
    )

for i in list(map(ord, nini2())): # gmtime
    nini6(i) # fwrite

print('Complete')
