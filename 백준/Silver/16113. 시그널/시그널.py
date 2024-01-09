# 시그널

result = ''
count = 0
n = int(input()) // 5

signal = input().rstrip()

for j in range(n):
    if count < 0:
        count += 1
        continue
    if signal[j] == '#':
        if j > n - 3:  # 끝을 기준으로 2번째 이상일 경우. 무조건 1임
            result += '1'
        else:
            if signal[j + 1] == signal[j + 2] == '#':  # 1, 4를 제외한 숫자
                count = -2
                if signal[j + n] == '.':  # 2, 3, 7
                    if signal[j + (n * 2)] == '.':  # 7
                        result += '7'
                    else:  # 2, 3
                        if signal[j + (n * 3)] == '.':  # 3
                            result += '3'
                        else:  # 2
                            result += '2'
                else:  # 0, 5, 6, 8, 9
                    if signal[j + n + 2] == '.':  # 5, 6
                        if signal[j + (n * 3)] == '.':  # 5
                            result += '5'
                        else:
                            result += '6'
                    else:  # 0, 8, 9
                        if signal[j + (n * 2) + 1] == '.':  # 0
                            result += '0'
                        else:
                            if signal[j + (n * 3)] == '.':  # 9
                                result += '9'
                            else:  # 8
                                result += '8'
            elif signal[j + 2] == '#':
                if signal[j + (n * 2) + 1] == '#':  # 4
                    result += '4'
                    count = -2
                else:  # 1이 두개 붙어있음
                    result += '1'
            else:  # 1인 경우
                result += '1'

print(result)
