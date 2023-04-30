import sys

input = sys.stdin.readline

''' 초기화 '''
n, m = map(int, input().split())    # n:node , m:edge
A_list = [[] for _ in range(n+1)]   # Adjacency list
visited = [False] * (n+1)   # visited node check
cnt = 0

''' DFS '''
def dfs(v):
    visited[v] = True
    for i in A_list[v]:
        if not visited[i]:
            dfs(i)

''' input '''
for _ in range(m):
    start, end = map(int, input().split())
    A_list[start].append(end)
    A_list[end].append(start)   # undirected graph


for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)