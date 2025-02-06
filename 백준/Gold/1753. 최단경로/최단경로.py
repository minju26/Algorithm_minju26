import sys
from queue import PriorityQueue
input = sys.stdin.readline

# 입력
v, e = map(int, input().split())
k = int(input()) - 1
adj = [[] for _ in range(v)]
for _ in range(e):
    #(a, b, w) : a -w-> b
    a, b, w = map(int, input().split())
    adj[a - 1].append((b - 1, w))

# 다익스트라
pq = PriorityQueue()
pq.put((0, k))

min_dist = [1e9] * v
min_dist[k] = 0

while pq.qsize() != 0:
    d, u = pq.get()

    if d != min_dist[u]:
        continue

    for i, w in adj[u]:
        if min_dist[i] > min_dist[u] + w:
            min_dist[i] = min_dist[u] + w
            pq.put((min_dist[i], i))


for i in range(v):
    if min_dist[i] == 1e9:
        print('INF')
    else:
        print(min_dist[i])