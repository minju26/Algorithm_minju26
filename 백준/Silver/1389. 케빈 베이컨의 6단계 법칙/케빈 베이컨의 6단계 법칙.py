
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

min_kevin_bacon = 1e9
min_person = -1
for i in range(n):
    visit = [False] * n
    distance = [-1] * n

    q = deque([i])
    visit[i] = True
    distance[i] = 0

    while len(q) != 0:
        u = q.popleft()

        for v in adj[u]:
            if not visit[v]:
                q.append(v)
                visit[v] = True
                distance[v] = distance[u] + 1
    
    kevin_bacon = sum(distance)

    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_person = i

print(min_person + 1)