# 금메달 수 많은 나라
# 금메달 수 같으면 은메달
# 금 은 같으면 동메달

N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)]
dic = {}

for i in range(len(medal)):
    dic[medal[i][0]] = medal[i][1:4]

sorted_dic = sorted(dic.items(), key=lambda x:(x[1][0],x[1][1],x[1][2]), reverse=True)

for i in range(len(sorted_dic)):
    if sorted_dic[i][0]==K:
        print(i)
