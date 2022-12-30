def sum(l):
    sum = 0
    for i in range(l):
        sum += i
    return sum


def check_answer(n, l, sum):
    if l > 100 or n - sum < 0:  # 범위 벗어남
        print(-1)
        return 1
    elif (n - sum) % l == 0:  # 정답
        quotient = int((n - sum) / l)
        for i in range(l):
            print(quotient + i, end=" ")
        return 1
    else:
        return 0


n, l = map(int, input().split())
while check_answer(n, l, sum(l)) == 0:
    l += 1
