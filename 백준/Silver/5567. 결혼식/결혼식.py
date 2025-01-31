import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

inv = []

for i in adj[1]:
    if i not in inv:
        inv.append(i)
    for j in adj[i]:
        if j not in inv and j != 1:
            inv.append(j)

print(len(inv))