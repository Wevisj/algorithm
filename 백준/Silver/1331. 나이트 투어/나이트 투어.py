# 나이트 투어 / 기존 나이트 투어 문제인 백트래킹 알고리즘이 아닌 단순 검사하는 문제

import sys

input = sys.stdin.readline


def check_valid(now, target):
    if abs(ord(now[0]) - ord(target[0])) == 1 and abs(int(now[1]) - int(target[1])) == 2:
        return True
    elif abs(ord(now[0]) - ord(target[0])) == 2 and abs(int(now[1]) - int(target[1])) == 1:
        return True
    else:
        return False


count = 0
visited = []
now = input()
count += 1
visited.append(now)

for i in range(35):
    target = input()
    visited.append(target)
    if check_valid(now, target):
        count += 1
        now = target
    else:
        break

if count == 36 and len(set(visited)) == 36 and check_valid(visited[0], visited[-1]):
    print("Valid")
else:
    print("Invalid")
