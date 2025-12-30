e = input("Cipher text: ")
k = input("Key text: ")
d = ""
for i in range(len(e)):
    dc = (ord(e[i]) - ord(k[i])) % 26 + ord('A')
    d += chr(dc)
du = d.upper()
dl = d.lower()
print("Flag: picoCTF{" + du + "}")
print("or")
print("Flag: picoCTF{" + dl + "}")