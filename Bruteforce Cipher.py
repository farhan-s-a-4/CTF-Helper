encr = input("Enter the encrypted message: ")
al = "abcdefghijklmnopqrstuvwxyz"
l = len(encr)
print("Here are all possible decryptions:")
for shift in range(26):
    decrypted_message = ""
    for c in encr:
        if c in al:
            new_char = chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
            decrypted_message += new_char
        else:
            decrypted_message += c
    print(f"Shift {shift}: {decrypted_message}")