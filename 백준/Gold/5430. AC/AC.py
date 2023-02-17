import sys
import re

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    flag = True
    is_reverse = False
    fn = input()
    n = int(input())
    array = input().rstrip()
    array = re.split('[\[,\]]', array)
    array = list(filter(None, array))
    for i in fn:
        if i == 'R':
            is_reverse = not is_reverse
        elif i == 'D':
            if is_reverse:
                try:
                    array.pop()
                except IndexError:
                    print("error")
                    flag = False
                    break
            else:
                try:
                    del (array[0])
                except IndexError:
                    if not array:
                        print("error")
                        flag = False
                        break
    if flag:
        if is_reverse:
            array.reverse()
        print("[", end="")
        print(*array, sep=",", end="")
        print("]")
