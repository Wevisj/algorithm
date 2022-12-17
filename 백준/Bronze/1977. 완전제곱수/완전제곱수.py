def square(a):
    return a * a


a = 1

squareNums = {}

minNum = 0

sum = 0

while True:
    squareNums[square(a)] = 1
    a += 1
    if square(a) > 10000:
        break

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i in squareNums:
        if minNum == 0:
            minNum = i
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(minNum)
