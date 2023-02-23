result = 1
ans = [0] * 10

for _ in range(3):
    result *= int(input())
    
result = str(result)

for i in range(len(result)):
    ans[int(result[i])] += 1
    
print(*ans, sep="\n")
