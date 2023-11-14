# 명령 프롬프트

n = int(input())

filename = list(input())

for i in range(n - 1):
    s = input()
    for c in range(len(filename)):
        if filename[c] != s[c]:
            filename[c] = '?'

print(''.join(filename))
