for _ in range(int(input())):
    k = int(input())
    words = []
    running = True
    for i in range(k):
        words.append(list(input()))
    for i in range(k):
        for j in range(k):
            if j == i:
                continue
            else:
                combine_word = words[i] + words[j]
            ans = True
            if len(combine_word) % 2 == 0:
                for u in range(len(combine_word) // 2):
                    if combine_word[u] != combine_word[len(combine_word) - 1 - u]:
                        ans = False
                        break
                if ans:
                    print("".join(combine_word))
                    running = False
                    break
            else:
                for u in range(len(combine_word) // 2):
                    if combine_word[u] != combine_word[len(combine_word) - 1 - u]:
                        ans = False
                        break
                if ans:
                    print("".join(combine_word))
                    running = False
                    break
            if not running:
                break
        if not running:
            break
    if not running:
        continue
    else:
        print(0)
