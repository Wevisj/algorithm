import sys

input = sys.stdin.readline

n, m = map(int, input().split())

non_heard = {}
non_heard_seen = []

for _ in range(n):
    name = input().rstrip()
    non_heard[name] = True
for _ in range(m):
    name = input().rstrip()
    try:
        if non_heard[name]:
            non_heard_seen.append(name)
    except:
        pass
print(len(non_heard_seen), *sorted(non_heard_seen), sep="\n")
