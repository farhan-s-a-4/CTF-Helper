import subprocess

cmd = (
    "python3 -c 'print(\"a\"*49968); print(\"a\"*32); print(\"\\n\")' | "
    "nc wily-courier.picoctf.net 50511 | "
    "sed -n '3p;9p'"
)
subprocess.run(
    ["wsl", "bash", "-lc", cmd],
    check=False
)

hex1 = 0x6161616161616161616161616161616161616161616161616161616161616161
hex2 = int(input("paste the first line here: "), 16)
hex3 = int(input("paste the second line here: "), 16)
flag = hex(hex1 ^ hex2 ^ hex3)
flag = bytes.fromhex(flag[2:]).decode("utf-8")
print(flag)