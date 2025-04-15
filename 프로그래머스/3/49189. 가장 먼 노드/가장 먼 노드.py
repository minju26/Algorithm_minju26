from collections import deque

def solution(n, edge):
    adj = [[] for _ in range(n)]
    dist = [0] * n
    
    for e in edge:
        a, b = e
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    
    visited = [False] * n
    q = deque([0])
    visited[0] = True
    
    while q:
        v = q.popleft()
        
        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                dist[w] = dist[v] + 1
                q.append(w)
            
    answer = dist.count(max(dist))
    return answer