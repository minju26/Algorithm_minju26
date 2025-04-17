from collections import deque

def comp(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    if cnt == 1: 
        return True
    else:
        return False

def solution(begin, target, words):
    n = len(words)
    
    tindex = -1
    for i in range(n):
        if words[i] == target:
            tindex = i
    if tindex == -1: return 0

    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if comp(words[i], words[j]):
                adj[i].append(j)
                adj[j].append(i)

    visited = [False] * n
    dist = [0] * n
    q = deque([])
    for i in range(n):
        if comp(begin, words[i]):
            q.append(i)
            visited[i] = True
            dist[i] = 1
    
    while q:
        i = q.popleft()
        
        for j in adj[i]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
                dist[j] = dist[i] + 1

    return dist[tindex]