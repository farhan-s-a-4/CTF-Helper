o = "EVANSDALE FARMHOUSE BRIE"
c = "PGLYDOLWPEQLCXSZFDPEMCTP"
possible_a = [x for x in range(1, 26, 2) if x != 13]
ov = [ord(ch) - ord('A') for ch in o]
cv = [ord(ch) - ord('A') for ch in c]
for a in possible_a:
    b = (cv[0] - (a * ov[0])%26) % 26
    if all((a * ov[i] + b) % 26 == cv[i] for i in range(len(ov))):
        print(f"Found key: a={a}, b={b}")
        break
else:
    print("No key found")