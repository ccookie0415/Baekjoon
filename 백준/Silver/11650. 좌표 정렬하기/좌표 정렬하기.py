N = int(input())
lst = []

for _ in range(N):
    A,B = map(int,input().split())
    lst.append([A,B])

sorted_lst = sorted(lst, key=lambda x:(x[0],x[1]))

for point in sorted_lst:
    print(point[0], point[1])