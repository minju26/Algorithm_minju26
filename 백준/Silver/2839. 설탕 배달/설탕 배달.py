import sys
input = sys.stdin.readline

n = int(input())

dp = [-1]*(n+1)
dp[3] = 1

if n > 3:
    for i in range(4, n+1):
        if i == 4: 
            dp[i] = -1
            continue
        if i == 5: 
            dp[5] = 1
            continue
        if(dp[i-3] == -1) and (dp[i-5] == -1): dp[i] = -1
        elif dp[i-3] == -1: dp[i] = dp[i-5] + 1
        elif dp[i-5] == -1: dp[i] = dp[i-3] + 1
        else: dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[n])