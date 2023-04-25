import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            next_a = a + dx[i]
            next_b = b + dy[i]

            if 0 <= next_a < n and 0 <= next_b < m and maze[next_a][next_b] == 1:
                queue.append([next_a, next_b])
                maze[next_a][next_b] = maze[a][b] + 1

    return maze[n-1][m-1]

print(bfs(0,0))