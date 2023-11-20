# 다음수 구하기

n = int(input())

for _ in range(n):
    num = list(input())
    i = len(num) - 2
    while True:
        if i == -1:
            print("BIGGEST")
            break
        else:
            if int(num[i]) < int(num[i + 1]):
                for j in range(len(num) - 1, i, -1):
                    if int(num[j]) > int(num[i]):
                        temp = num[j]
                        num[j] = num[i]
                        num[i] = temp
                        break
                sorted_list = sorted(num[i + 1:len(num)])
                num[i + 1:len(num)] = sorted_list
                print("".join(i for i in num))
                break
            else:
                i -= 1
