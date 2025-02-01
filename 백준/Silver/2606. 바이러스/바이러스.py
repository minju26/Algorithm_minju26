import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

v = [0] * n
v[0] = 1

while True:
    new = False # 새로운 감염이 발생하지 않을 때 까지 진행해야 하므로, flag 역할

    for i in range(n):
        if v[i] == 0:
            continue

        for j in adj[i]:
            if v[j] == 0:
                v[j] = 1
                new = True
    
    if not new:
        break

print(sum(v) - 1)