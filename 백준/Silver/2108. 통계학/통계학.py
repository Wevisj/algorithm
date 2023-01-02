from collections import Counter


def modefinder(numbers):
    c = Counter(numbers)
    mode = c.most_common()
    if mode[0][1] == mode[1][1]:
        return mode[1][0]
    else:
        return mode[0][0]


T = int(input())
numbers = []
ans = []
for _ in range(T):
    numbers.append(int(input()))
if T > 1:
    ans.append(round(sum(numbers) / T))
    numbers.sort()
    ans.append(numbers[int(T / 2)])
    ans.append(modefinder(numbers))
    ans.append(numbers[T - 1] - numbers[0])
else:
    ans.append(numbers[0])
    ans.append(numbers[0])
    ans.append(numbers[0])
    ans.append(0)
for i in range(4):
    print(ans[i])
