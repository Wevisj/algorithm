import sys

input = sys.stdin.readline


while True:
    brackets = []
    flag = True

    line = input().rstrip()

    if line == '.':
        break
    else:
        for word in line:
            if word == '(':
                brackets.append('(')
            elif word == '[':
                brackets.append('[')
            if word == ')':
                try:
                    if brackets[len(brackets) - 1] == '(':
                        brackets.pop()
                    else:
                        print("no")
                        flag = False
                        break
                except IndexError:
                    print("no")
                    flag = False
                    break
            elif word == ']':
                try:
                    if brackets[len(brackets) - 1] == '[':
                        brackets.pop()
                    else:
                        print("no")
                        flag = False
                        break
                except IndexError:
                    print("no")
                    flag = False
                    break
        if flag:
            if not brackets:
                print("yes")
            else:
                print("no")
