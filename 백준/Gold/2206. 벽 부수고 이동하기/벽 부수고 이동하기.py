import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

#[row][col][벽 부숨 여부]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
drow, dcol = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    q = deque([(0, 0, 0)])  #row, col, 벽 부숨 여부
    visited[0][0][0] = 1  # 시작 위치 방문 처리 (거리 1부터 시작)

    while q:
        row, col, broken = q.popleft()

        if row == n - 1 and col == m - 1:
            return visited[row][col][broken]

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if 0 <= nrow < n and 0 <= ncol < m:
                if graph[nrow][ncol] == 0 and visited[nrow][ncol][broken] == 0:
                    visited[nrow][ncol][broken] = visited[row][col][broken] + 1
                    q.append((nrow, ncol, broken))

                if graph[nrow][ncol] == 1 and broken == 0:
                    visited[nrow][ncol][1] = visited[row][col][broken] + 1
                    q.append((nrow, ncol, 1))

    return -1

print(bfs())
