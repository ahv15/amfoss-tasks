import string
upper=string.ascii_uppercase
lower=string.ascii_lowercase
digits=string.digits
hex_text=[]
hex_detext=[]
realtext=[]
hex_text=bytearray.fromhex("667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268").decode()
for i in range(0,len(hex_text)):
    hex_detext.append(chr((ord(hex_text[i]))^10))
for i in range (0,len(hex_detext)):
    if hex_detext[i].isupper() is True:
        realtext.append(upper[(upper.index(hex_detext[i])-3)%26])
    if hex_detext[i].islower() is True:
        realtext.append(lower[(lower.index(hex_detext[i])-3)%26])
    if hex_detext[i].isdigit() is True:
        realtext.append(digits[(digits.index(hex_detext[i])-3)%26])

realtexts = ''.join(realtext)
print(realtexts)
