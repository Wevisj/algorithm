n = int(input())
score = list(map(int, input().split()))
score.sort()
print(sum(score) * 100 / (n * score[n - 1]))
