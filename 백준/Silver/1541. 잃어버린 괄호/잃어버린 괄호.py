import sys
from collections import deque

input = sys.stdin.readline

formula = input().rstrip()

n = formula[0]
minus = False

result = 0

for i in range(1, len(formula)):
    if minus:
        if formula[i] == '-':
            result -= int(n)
            n = ""
        elif formula[i] == '+':
            result -= int(n)
            n = ""
        else:
            n += formula[i]
    else:
        if formula[i] == '-':
            minus = True
            result += int(n)
            n = ""
        elif formula[i] == '+':
            result += int(n)
            n = ""
        else:
            n += formula[i]
if minus:
    result -= int(n)
else:
    result += int(n)

print(result)
