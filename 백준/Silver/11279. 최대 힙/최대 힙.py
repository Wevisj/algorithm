# 최대 힙
# 출처 : https://mong9data.tistory.com/101
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x, x))  # 튜플은 앞의 원소를 기준으로 정렬하고, 최소 힙이기 때문에 큰 값일수록 -값이 크다는 점을 이용하여 최대힙으로 재구성함.
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])  # 튜플을 원소로 주었기 때문에, x를 반환하려면 두 번째 요소를 반환해야 하기 때문에 [1]을 붙임
        else:
            print(0)