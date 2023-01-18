fibo_count_zero = {}
fibo_count_one = {}

fibo_count_zero[0] = 1
fibo_count_one[0] = 0

fibo_count_zero[1] = 0
fibo_count_one[1] = 1

for i in range(2, 41):
    fibo_count_zero[i] = fibo_count_zero[i-1] + fibo_count_zero[i-2]
    fibo_count_one[i] = fibo_count_one[i-1] + fibo_count_one[i-2]

for _ in range(int(input())):
    n = int(input())
    print(fibo_count_zero[n], fibo_count_one[n])