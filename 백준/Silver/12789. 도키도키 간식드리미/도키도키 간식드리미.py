# 도키도키 간식드리미

num = 1
min = 10000

students = int(input())
order = list(map(int, input().split()))

waiting_lines = []

while True:
    # 정답 처리
    if num == students + 1:
        print('Nice')
        break

    # 학생 선택
    if waiting_lines:
        if waiting_lines[-1] == num:
            student = waiting_lines.pop()
            if not waiting_lines:
                min = 10000
            else:
                min = waiting_lines[-1]
        else:
            student = order.pop(0)
    else:
        student = order.pop(0)

    if student != num:
        if min < student:
            print('Sad')
            break
        else:
            min = student
            waiting_lines.append(student)
    else:
        num += 1
