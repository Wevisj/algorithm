import sys
from collections import deque

input = sys.stdin.readline

seq = []
stack = deque()
arr = []
ans = []

n = int(input())

for i in range(n):
    stack.append(i + 1)
    seq.append(int(input()))

while True:
    if not stack:
        if arr[-1] != seq[0]:
            print("NO")
            break
        else:
            arr.pop()
            del seq[0]
            ans.append("-")
            if not seq:
                for k in ans:
                    print(k)
                break
    elif stack[0] == seq[0]:
        del seq[0]
        del stack[0]
        ans.append("+")
        ans.append("-")
        if not seq:
            for k in ans:
                print(k)
            break
    else:
        if stack[0] > seq[0]:
            if arr[-1] != seq[0]:
                print("NO")
                break
            else:
                arr.pop()
                del seq[0]
                ans.append("-")
        else:
            arr.append(stack.popleft())
            ans.append("+")
