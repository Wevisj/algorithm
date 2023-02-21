import sys
from itertools import permutations

input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(N)]

functions = list(map(int, input().split()))

for i in functions:
    if i == 1:
        arr = arr[::-1]
    elif i == 2:
        arr = list(map(lambda x: x[::-1], arr))
    elif i == 3:
        arr = list(zip(*arr[::-1]))
        N, M = M, N  # 행, 열 사이즈 스왑
    elif i == 4:
        arr = list(zip(*arr))[::-1]
        N, M = M, N  # 행, 열 사이즈 스왑
    else:
        arr1 = map(lambda x: x[:M // 2], arr[:N // 2])  # 1사분면
        arr2 = map(lambda x: x[M // 2:], arr[:N // 2])  # 2사분면
        arr3 = map(lambda x: x[:M // 2], arr[N // 2:])  # 3사분면
        arr4 = map(lambda x: x[M // 2:], arr[N // 2:])  # 4사분면
        if i == 5:  # 시계 방향 사분면 회전
            arr = list(zip(arr3, arr1)) + list(zip(arr4, arr2))
        elif i == 6:  # 반시계 방향 사분면 회전
            arr = list(zip(arr2, arr4)) + list(zip(arr1, arr3))
        arr = list(map(lambda x: x[0] + x[1], arr))

for row in arr:
    print(*row)
