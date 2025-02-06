import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
adj = [[] for _ in range(v)]
visited = [False] * v

for _ in range(e):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

dfs(0)

ans = 0
for i in range(1, v):
    if visited[i]:
        ans += 1

print(ans)