import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
visited = [False] * n
cc = [-1] * n

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a -1)

def bfs(adj, visited, start, cnt):
    q = deque([start])
    visited[start] = True
    cc[start] = cnt
    while q:
        v = q.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = True
                cc[i] = cnt
                q.append(i)

cnt = 0
for i in range(n):
    if not visited[i]:
        cnt += 1
        bfs(adj, visited, i, cnt)

print(max(cc))