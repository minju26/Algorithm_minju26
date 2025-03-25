import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
m = int(input())

# 노선 정보
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append((b - 1, c))


def dijkstra(cost, i):
    pq = PriorityQueue()
    pq.put((cost[i], i))

    while pq.qsize() != 0:
        c, v = pq.get()

        if c != cost[v]:
            continue

        for j, w in adj[v]:
            if cost[j] > cost[v] + w:
                cost[j] = cost[v] + w
                pq.put((cost[j], j))
    
    return cost

ans = []
for i in range(n):
    cost = [1e9] * n
    cost[i] = 0
    result = [0 if x == 1e9 else x for x in dijkstra(cost, i)]
    ans.append(result)
    

for row in ans:
    print(*row)