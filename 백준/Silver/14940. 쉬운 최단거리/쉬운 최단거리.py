import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 거리를 기록
dist = [[0] * m for _ in range(n)]

# 목표점 찾기
trow = tcol = 0
for row in range(n):
    for col in range(m):
        if graph[row][col] == 2:
            trow = row
            tcol = col
            dist[trow][tcol] = 0

# bfs
visitied = [[False] * m for _ in range(n)]
drow, dcol = [1, -1, 0, 0], [0, 0, 1, -1]

q = deque([])
q.append((trow, tcol))
visitied[trow][tcol] = True

while len(q) != 0:
    row, col = q.popleft()

    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]

        if nrow < 0 or n - 1 < nrow or ncol < 0 or m - 1 < ncol:
            continue
        
        if graph[nrow][ncol] == 0:
            continue
        
        if graph[nrow][ncol] == 1 and not visitied[nrow][ncol]:
            visitied[nrow][ncol] = True
            dist[nrow][ncol] = dist[row][col] + 1
            q.append((nrow, ncol))
        

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visitied[i][j]:
            dist[i][j] = -1


for i in range(n):
    print(*dist[i])