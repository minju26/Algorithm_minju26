# boj 1753 :: 파티 :: gld.3

import sys
from queue import PriorityQueue

input = sys.stdin.readline

# 입력
n, m, x = map(int, input().split())
x -=1 

adj = [[] for _ in range(n)]
rev_adj = [[] for _ in range(n)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adj[s - 1].append((e - 1, w))
    rev_adj[e - 1].append((s - 1, w))

def dijkstra(graph, dist):
    pq = PriorityQueue()
    pq.put((dist[x], x))

    while pq.qsize() != 0:
        d, v = pq.get()

        if d != dist[v]:
            continue

        for u, w in graph[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                pq.put((dist[u], u))

dist = [1e9] * n
dist[x] = 0

rev_dist = [1e9] * n
rev_dist[x] = 0

dijkstra(adj, dist)
dijkstra(rev_adj, rev_dist)

for i in range(n):
    dist[i] += rev_dist[i]

print(max(dist))