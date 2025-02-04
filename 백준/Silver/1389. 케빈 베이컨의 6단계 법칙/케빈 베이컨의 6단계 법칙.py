import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
distance = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for i in range(n):
    for j in range(n):
        if i == j:
            distance[i][j] = 0
        else:
            distance[i][j] = -1

def bfs(graph, start, visited, distance):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                distance[i] = distance[v] + 1
                visited[i] = True

for i in range(n):
    bfs(adj, i, visited[i], distance[i])

ans = float('inf')
cur = sum(distance[0])
for i in range(n):
    new = sum(distance[i])
    if cur > new:
        ans = i
        cur = new
    elif cur == new:
        ans = min(ans, i)
        cur = new

print(ans+1)
    