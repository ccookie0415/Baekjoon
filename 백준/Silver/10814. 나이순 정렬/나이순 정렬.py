N = int(input())
lst = []

for tc in range(N):
    age, name = input().split()
    lst.append([int(age),name,tc])

sorted_lst = sorted(lst, key=lambda x:(x[0],x[2]))

for j in sorted_lst:
    print(j[0],j[1])