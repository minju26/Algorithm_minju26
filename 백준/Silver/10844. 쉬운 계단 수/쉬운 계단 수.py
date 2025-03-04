import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000000
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    if i == 0: 
        dp[1][i] = 0
    else:
        dp[1][i] = 1

for x in range(2, n + 1):
    for d in range(10):
        if d == 0:
            dp[x][d] = dp[x - 1][d + 1]
        elif d == 9:
            dp[x][d] = dp[x - 1][d - 1]
        else:
            dp[x][d] = dp[x - 1][d - 1] + dp[x - 1][d + 1]

print(sum(dp[n])% mod)