import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]

dresult = []
bresult = []

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1):
    graph[i].sort()


dvisited = [False]*(n+1)
def dfs(graph, visited, s):
    visited[s] = True
    dresult.append(s)

    for i in graph[s]:
        if not visited[i]:
            dfs(graph, visited, i)



def bfs(graph, s):
    visited = [False]*(n+1)
    queue = [s]
    visited[s] = True
    bresult.append(s)

    while queue:
        v = queue.pop(0)
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
                bresult.append(i)


dfs(graph, dvisited, s)
bfs(graph, s)

print(*dresult)
print(*bresult)