import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

queue = deque([(0, 0)])
visited[0][0] = True
dist[0][0] = 0

while len(queue) != 0:
    row, col = queue.popleft()

    # 위
    if row > 0 and map[row -1][col] == 1 and not visited[row - 1][col]:
        queue.append((row - 1, col))
        visited[row - 1][col] = True
        dist[row - 1][col] = dist[row][col] + 1
    
    # 아래
    if row < n - 1 and map[row + 1][col] == 1 and not visited[row + 1][col]:
        queue.append((row + 1, col))
        visited[row + 1][col] = True
        dist[row + 1][col] = dist[row][col] + 1
    
    # 오
    if col < m - 1 and map[row][col + 1] == 1 and not visited[row][col + 1]:
        queue.append((row, col + 1))
        visited[row][col + 1] = True
        dist[row][col + 1] = dist[row][col] + 1
    
    # 왼
    if col > 0 and map[row][col - 1] == 1 and not visited[row][col - 1]:
        queue.append((row, col - 1))
        visited[row][col - 1] = True
        dist[row][col - 1] = dist[row][col] + 1

print(dist[n - 1][m - 1] + 1)