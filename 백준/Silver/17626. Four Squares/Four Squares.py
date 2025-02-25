import sys
input = sys.stdin.readline

n = int(input())
dp = [4] * (n + 1) # 최악의 경우 4개의 자연수의 제곱수로 표현할 수 있으므로

for i in range(1, n + 1):
    # i가 제곱수인 경우 => 1가지 자연수의 제곱수로 표현 가능
    if (i ** 0.5).is_integer():
        dp[i] = 1
        continue
    
    for j in range(1, int(i ** 0.5) + 1):
        if j * j > i:
            break

        dp[i] = min(dp[i], 1 + dp[i - j * j])

print(dp[n])