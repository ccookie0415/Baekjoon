import sys
input = sys.stdin.readline

N,K = map(int,input().split())
temp = list(map(int,input().split()))
result = [sum(temp[0:0+K])]

for i in range(K,len(temp)):
    answer = (result[-1] + temp[i] - temp[i-K])
    result.append(answer)

print(max(result))
