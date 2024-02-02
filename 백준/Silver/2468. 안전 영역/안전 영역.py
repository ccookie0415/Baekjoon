import sys
sys.setrecursionlimit(100000)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, visited):
    visited[i][j] = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] >= max_:
            dfs(ni, nj, visited)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = set()
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] not in check:
            check.add(arr[i][j])

check = list(check)

for l in range(len(check)):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    max_ = check[l]

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= max_ and visited[i][j] == 0:
                dfs(i, j, visited)
                cnt += 1

    ans.append(cnt)
print(max(ans))