def operate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b

def solution(arr):
    n = (len(arr) + 1) // 2

    min_dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    max_dp = [[float('-inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        val = int(arr[i * 2])
        min_dp[i][i] = val
        max_dp[i][i] = val

    for step in range(1, n):
        for i in range(n - step):
            j = i + step

            for k in range(i, j):
                op = arr[k * 2 + 1]

                max_candi = [
                    operate(max_dp[i][k], max_dp[k + 1][j], op),
                    operate(max_dp[i][k], min_dp[k + 1][j], op),
                    operate(min_dp[i][k], max_dp[k + 1][j], op),
                    operate(min_dp[i][k], min_dp[k + 1][j], op),
                ]
                
                max_dp[i][j] = max(max_dp[i][j], *max_candi)
                min_dp[i][j] = min(min_dp[i][j], *max_candi)

    return max_dp[0][n - 1]
