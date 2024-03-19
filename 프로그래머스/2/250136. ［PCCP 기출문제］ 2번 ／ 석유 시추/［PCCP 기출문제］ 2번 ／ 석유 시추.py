from collections import deque

def bfs(graph, i, j):
    queue = deque([(i, j)])
    graph[i][j] = 0
    
    cnt = 0
    indexs = set([j])
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    
           
    while queue:
        cnt += 1
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0<= ni < len(graph) and 0 <= nj < len(graph[0]):
                if graph[ni][nj] == 1:
                    queue.append((ni, nj))
                    graph[ni][nj] = 0
                    indexs.add(nj)
    return indexs, cnt


def solution(land):
    
    row = len(land)
    col = len(land[0])
    
    tjrdb = []
    result = [0]*col
    
    for j in range(col):
        for i in range(row):
            if land[i][j] == 1:
                indexs, cnt = bfs(land, i, j)
                tjrdb.append((cnt, list(indexs)))
    
    for val, index in tjrdb:
        for i in index:
            result[i] += val
    
    return max(result)

