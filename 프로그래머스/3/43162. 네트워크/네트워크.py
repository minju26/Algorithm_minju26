def solution(n, computers):
    
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                adj[i].append(j)
                adj[j].append(i)
    
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for w in adj[v]:
            if not visited[w]:
                dfs(w)
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
            
    return cnt