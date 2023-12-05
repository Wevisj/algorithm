# 팰린드롬인지 확인하기
import sys

input = sys.stdin.readline

flag = True
word = input().rstrip()
start = 0
end = len(word) - 1
while start < end:
    if word[start] != word[end]:
        flag = False
        print(0)
        break
    else:
        start += 1
        end -= 1
if flag:
    print(1)
