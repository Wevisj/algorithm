import sys

input = sys.stdin.readline

stack = []

T = int(input())

for _ in range(T):
    fn = input().rstrip()
    if "push" in fn:
        stack.append(fn.split()[-1])
    elif fn == "pop":
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif fn == "size":
        print(len(stack))
    elif fn == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif fn == "top":
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
