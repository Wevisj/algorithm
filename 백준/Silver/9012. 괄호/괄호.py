import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    brackets = []
    flag = True

    line = input().rstrip()

    for word in line:
        if word == '(':
            brackets.append('(')
        if word == ')':
            try:
                if brackets[len(brackets) - 1] == '(':
                    brackets.pop()
                else:
                    print("NO")
                    flag = False
                    break
            except IndexError:
                print("NO")
                flag = False
                break
    if flag:
        if not brackets:
            print("YES")
        else:
            print("NO")
