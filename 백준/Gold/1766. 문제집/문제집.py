import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
pre = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    pre[b - 1] += 1

q = PriorityQueue()
for i in range(n):
    if pre[i] == 0:
        q.put(i)

ans = []
while q.qsize() != 0:
    u = q.get()
    ans.append(u)

    for v in adj[u]:
        pre[v] -= 1
        if pre[v] == 0:
            q.put(v)


for i in range(n):
    print(ans[i] + 1, end=" ")