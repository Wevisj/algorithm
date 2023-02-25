import sys

input = sys.stdin.readline

while True:
    flag = True
    num = input().rstrip()
    if num == "0":
        break
    start = 0
    end = len(num) - 1
    while start < end:
        if num[start] != num[end]:
            flag = False
            print("no")
            break
        else:
            start += 1
            end -= 1
    if flag:
        print("yes")
