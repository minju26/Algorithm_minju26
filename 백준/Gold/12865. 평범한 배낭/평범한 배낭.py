import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
obj = [(0,0)]

for _ in range(n):
    obj.append(tuple(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        kg = obj[i][0]
        val = obj[i][1]

        if j < kg:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(val + dp[i-1][j-kg], dp[i-1][j])

print(dp[n][k])