import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
field = [input().strip() for _ in range(m)]

def bfs(color):
    visited = [[False] * n for _ in range(m)]
    q = deque()
    result = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] != color or visited[i][j]:
                continue

            q.append((i, j))
            visited[i][j] = True
            cnt = 1

            while q:
                r, c = q.popleft()

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if not visited[nr][nc] and field[nr][nc] == color:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            cnt += 1

            result += cnt * cnt
    return result

print(bfs('W'), bfs('B'))
