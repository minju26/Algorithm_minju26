import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
field = [""] * m
for i in range(m):
    field[i] = input().strip()

def bfs(color):
    visited = [[False] * n for _ in range(m)]
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    result = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] != color:
                continue

            if not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt = 1

                while len(q) != 0:
                    r, c = q.popleft()

                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]

                        if nr < 0 or m <= nr or nc < 0 or n <= nc:
                            continue
                        if field[nr][nc] != color:
                            continue

                        if not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            cnt += 1

                result += cnt * cnt
    return result

print(bfs('W'), bfs('B'))