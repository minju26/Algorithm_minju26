import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

visited = [False] * 100001
dist = [0] * 100001

q = deque([])
q.append(n)
visited[n] = True

ans = 0
while len(q) != 0:
    x = q.popleft()

    if x == k:
        ans = dist[k]
        break

    for i in [x * 2, x - 1, x + 1]:
        if 0 <= i <= 100000 and not visited[i]:
            if i == x * 2:
                dist[i] = dist[x]
                q.appendleft(i)
            else:
                dist[i] = dist[x] + 1
                q.append(i)
            visited[i] = True

print(ans)