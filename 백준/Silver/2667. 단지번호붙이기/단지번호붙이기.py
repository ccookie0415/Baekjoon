N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
ans = []
di = [1,0,-1,0]
dj = [0,1,0,-1]
queue = []
def bfs(i,j):
    count = 1
    queue = []
    queue.append((i,j))

    while queue:
        r,c = queue.pop(0)
        for k in range(4):
            ni = r + di[k]
            nj = c + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                queue.append((ni,nj))
                arr[ni][nj] = 0
                count += 1

    return count

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
print('\n'.join(map(str,ans)))