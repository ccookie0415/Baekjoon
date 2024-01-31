def dfs(computers, visited, start):
    visited[start] = True
    
    for i in range(len(computers)):
        if computers[i][start] == 1:
            if visited[i] == False:
                dfs(computers, visited, i)
    

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            dfs(computers, visited, i)
            answer += 1
            
            
    return answer