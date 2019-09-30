from os import urandom
from ctypes import CDLL
import string
import hashlib
import itertools
from itertools import permutations
perm_iterator = itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 5)
hextext=[]
flag=""
key = ""
flag=""
k=0
ciphertext = "05181c2638270301601329023a203c2324072229230401273f2a1b0b02252b071e243e2313262923352411332336031b2f2d27191602383f07062e0827041725092e161e2d2f281017092f34123b321e2e12342d2b210c0b0e3f191f33370f1935000e2123392d132f163213152308302d0a0f3f282a0e183b"
while hashlib.md5(flag).digest().encode("hex") != "d444d1ac3799a86d31f34b4a8a3243c6":
    for m in perm_iterator:
        m=''.join(m)
        hex_key = m.encode("hex")
        key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
        hextext=ciphertext.decode("hex")
        for i in range(0,len(hextext)):
            flag += chr(ord(hextext[i])^int(key_list[i%5], 16))
        flag = "\\'{\\'"+flag+"\\'}\\'"
print flag
