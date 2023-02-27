import sys

input = sys.stdin.readline

yose_seq = []
i = 1
j = 0

n, k = map(int, input().split())

people = [i for i in range(1, n + 1)]

while True:
    if len(people) == 1:
        yose_seq.append(people.pop(0))
        break
    if j >= len(people):
        j = 0
    if i % k == 0:
        yose_seq.append(people.pop(j))
        j -= 1
    j += 1
    i += 1

print("<", end="")
print(*yose_seq, sep=", ", end="")
print(">")
