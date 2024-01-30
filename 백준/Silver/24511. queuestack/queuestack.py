# 큐스택

n = int(input())
structure_type = list(map(int, input().split()))
element = list(map(int, input().split()))
m = int(input())
insertion = list(map(int, input().split()))

queue = []
k = 0

for i in range(n):
    if structure_type[i] == 0:
        queue.append(element[i])

for i in range(m):
    if not queue:
        print(insertion[k], end=" ")
        k += 1
    else:
        print(queue.pop(), end=" ")
