# 크로아티아 알파벳

alpahbet = ["c=", "c-", "z=", "dz=", "d-", "lj", "nj", "s="]

line = input()
res = len(line)
flag = False

for c in alpahbet:
    n = line.count(c)
    if n != 0:
        if c == "z=":
            flag = True
        if c == "dz=" and flag == True:
            res += line.count("dz=")
        res += (1 - len(c)) * line.count(c)

print(res)
