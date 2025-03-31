import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

for r in range(n):
    for c in range(m):
        if graph[r][c] == 1:
            q.append((r, c))
            dist[r][c] = 0
            visited[r][c] = True

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

while len(q) != 0:
    r, c = q.popleft()

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or n <= nr or nc < 0 or m <= nc:
            continue

        if not visited[nr][nc]:
            q.append((nr, nc))
            dist[nr][nc] = dist[r][c] + 1
            visited[nr][nc] = True

print(max([max(dist[i]) for i in range(n)]))