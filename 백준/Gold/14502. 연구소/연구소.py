import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

loc = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            loc.append((i, j))

ans = 0
for com in combinations(loc, 3):

    # 벽 생성
    for row, col in com:
        lab[row][col] = 1
    
    # bfs
    visited = [[False] * m for _ in range(n)]
    q = deque([])

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i, j))
    
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]

    while len(q) != 0:
        row, col = q.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if nrow < 0 or n <= nrow or ncol < 0 or m <= ncol:
                continue
            if lab[nrow][ncol] == 1:
                continue
            if not visited[nrow][ncol]:
                q.append((nrow, ncol))
                visited[nrow][ncol] = True

    safe = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 and not visited[i][j]:
                safe += 1

    if safe > ans:
        ans = safe

    # 벽 제거
    for row, col in com:
        lab[row][col] = 0


print(ans)