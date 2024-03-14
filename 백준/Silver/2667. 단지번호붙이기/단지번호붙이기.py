import sys
input = sys.stdin.readline

n = int(input())
result = []
graph = []

#상/하/좌/우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(j, i):
    cnt = 0
    queue = [(i, j)]

    while queue:
        x, y = queue.pop(0)
        graph[y][x] = 0
        cnt += 1

        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]

            if nx < 0 or nx > (n-1) or ny < 0 or ny > (n-1): continue
            else:
                if graph[ny][nx] == 1:
                    queue.append((nx, ny))
                    graph[ny][nx] = 0
    
    result.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i)
