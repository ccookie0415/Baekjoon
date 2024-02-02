N,NEW,P = map(int,input().split())


if N == 0:
    print(1)
else:
    scores = list(map(int,input().split()))
    scores.append(NEW)
    scores.sort(reverse=True)

    if N == P and scores[-1] >= NEW:
        print(-1)

    else:
        current = N + 1

        for i in range(len(scores)):
            if scores[i] <= NEW:
                current = i + 1
                break

        print(current)