from copy import deepcopy

T = int(input())
friends = [list(input()) for _ in range(T)]  # NNY와 같은 문자열이 리스트의 형태로 입력되는 리스트
maxnum = 0  # Y개수의 최댓값
insider = 0  # 친구가 가장 많은 사람
friend_index = []  # NYY가 입력되었다 하면, 1,2 와 같이 인덱스 번호가 저장됨
count_friend = []
for i in range(T):
    friend_index.append([k for k in range(len(friends[i])) if friends[i][k] == 'Y'])
    #print(friend_index[i])
else:
    for i in range(T):
        sum = 0
        count_friend.append(deepcopy(friend_index[i]))
        for j in range(friends[i].count('Y')):
            count_friend[i].extend(friend_index[friend_index[i][j]])
            #print(count_friend[i])
        try:
            sum += len(set(count_friend[i])) - 1
        except IndexError as sum:  # 입력된 값이 모두 N일 경우
            print(maxnum)
            exit()  # 0을 출력하고 프로그램을 종료함
        else:  # 아닐 경우 계속해서 진행
            if sum > maxnum:
                maxnum = sum
    print(maxnum)
