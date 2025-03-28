import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    c = int(input())
    coins.append(c)

prev = [0] * (k + 1)
cur = [0] * (k + 1)

for i in range(k + 1):
    if i % coins[0] == 0:
        prev[i] = 1

for i in range(1, n):
    for j in range(k + 1):
        cur[j] = prev[j]
        if j >= coins[i]:
            cur[j] += cur[j - coins[i]]
        
    prev = cur

print(prev[k])