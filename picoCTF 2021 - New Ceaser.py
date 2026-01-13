import string
import re

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

encrypted_flag = "fegdeogdgecoeocgcgchcfcffccfca"

key = ALPHABET

def deshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

def b16_dencode(chipher):
    dec = ""
    for i in range(0, len(chipher), 2):
        ch = chipher[i:i+2]
        a = ord(ch[0]) - LOWERCASE_OFFSET
        b = ord(ch[1]) - LOWERCASE_OFFSET
        c = (a << 4) | b
        dec += chr(c)
    return dec

deshifted = []
for k in key:
    a = ""
    for i, c in enumerate(encrypted_flag):
        a += deshift(c, k)
    deshifted.append(a)

decoded = []
for d in deshifted:
    decoded.append(b16_dencode(d))
pattern = rf"^[a-zA-Z0-9{re.escape(string.punctuation)}]+$"
for s in decoded:
    if re.match(pattern, s):
        print(s)