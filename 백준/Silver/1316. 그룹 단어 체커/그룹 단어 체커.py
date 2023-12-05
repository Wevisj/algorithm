# 그룹 단어 체커

n = int(input())
res = 0

for _ in range(n):
    visited = [False for i in range(26)]
    flag = False
    word = input()
    current_letter = word[0]
    for c in word:
        if visited[ord(c) - 97] and current_letter != c:
            flag = True
            break
        else:
            visited[ord(c) - 97] = True
            current_letter = c
    if not flag:
        res += 1

print(res)
