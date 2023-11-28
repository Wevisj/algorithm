# 과제 안 내신 분?

students = [str(i) for i in range(1, 31)]

for i in range(28):
    n = input()
    students.remove(n)

print(" ".join(students))
