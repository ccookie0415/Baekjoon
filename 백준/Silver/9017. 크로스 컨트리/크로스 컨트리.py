T = int(input())

for tc in range(T):
    dic = {}
    N = int(input())
    run = list(map(int,input().split()))
    score = {}
    check = []

    for i in range(N):
        if run[i] not in dic:
            dic[run[i]] = 1

        else:
            dic[run[i]] += 1

    for key,value in dic.items():
        if value == 6:
            check.append(key)
            score[key] = []


    current = 1

    for j in range(N):
        if run[j] in check:
            score[run[j]].append(current)
            current += 1
        else:
            pass

    min_score = 1e9
    for key,value in score.items():
        if sum(value[:4]) < min_score:
            check_value = value
            min_score = sum(value[:4])
            answer = key

        elif sum(value[:4]) == min_score:
            if check_value[4] > value[4]:
                check_value = value
                answer = key

    print(answer)



