import sys
from collections import deque

input = sys.stdin.readline

stack = deque()

T = int(input())

for _ in range(T):
    fn = input().rstrip()
    if "push" in fn:
        stack.append(fn.split()[-1])
    elif fn == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.popleft())
    elif fn == "size":
        print(len(stack))
    elif fn == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif fn == "front":
        if not stack:
            print(-1)
        else:
            print(stack[0])
    elif fn == "back":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
