from collections import Counter

alpha = input().upper()
cnt = Counter(alpha)
sorted_cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)

if len(sorted_cnt) != 1 and sorted_cnt[0][1] == sorted_cnt[1][1]:
    answer = '?'

else:
    answer = sorted_cnt[0][0]

print(answer)


