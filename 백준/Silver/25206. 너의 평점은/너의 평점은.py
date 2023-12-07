# 너의 평점은

score = []
res = 0
sum_avg = 0
i = 0

for _ in range(20):
    s = list(map(str, input().split()))
    if s[2] == 'A+':
        score.append(4.5)
    elif s[2] == 'A0':
        score.append(4.0)
    elif s[2] == 'B+':
        score.append(3.5)
    elif s[2] == 'B0':
        score.append(3.0)
    elif s[2] == 'C+':
        score.append(2.5)
    elif s[2] == 'C0':
        score.append(2.0)
    elif s[2] == 'D+':
        score.append(1.5)
    elif s[2] == 'D0':
        score.append(1.0)
    elif s[2] == 'P':
        continue
    else:
        score.append(0)
    res += float(s[1]) * score[i]
    i += 1
    sum_avg += float(s[1])

res /= sum_avg

print(res)
