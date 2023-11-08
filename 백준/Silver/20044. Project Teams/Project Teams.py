#  ProjectTeams

import sys

input = sys.stdin.readline

n = int(input())

students = list(map(int, input().split()))
students.sort()
teams = [0 for i in range(n)]

for i in range(n):
    teams[i] = students[i] + students[len(students) - 1 - i]

print(min(teams))
