import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
visited = [False]*(v+1)

for i in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(graph, visited, s):
    visited[s] = True

    for i in graph[s]:
        if not visited[i]:
            dfs(graph, visited, i)

dfs(graph, visited, 1)

print(visited.count(True) -1)