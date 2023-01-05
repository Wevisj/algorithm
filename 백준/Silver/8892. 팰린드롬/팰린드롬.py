for _ in range(int(input())):
    k = int(input())
    words = []
    flag = True
    for i in range(k):
        words.append(list(input()))
    for i in range(k):
        for j in range(k):
            if j == i:
                continue
            else:
                combine_word = words[i] + words[j]
            ans = True
            left = 0
            right = len(combine_word) - 1
            while left < right:
                if combine_word[left] != combine_word[right]:
                    ans = False
                    break
                left += 1
                right -= 1
            if ans:
                print("".join(combine_word))
                flag = False
                break
        if not flag:
            break
    if not flag:
        continue
    else:
        print(0)
