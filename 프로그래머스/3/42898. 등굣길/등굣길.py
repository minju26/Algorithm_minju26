def solution(m, n, puddles):
    mod = 10**9 + 7
    route = [[0] * m for _ in range(n)]
    route[0][0] = 1

    for x, y in puddles:
        route[y - 1][x - 1] = -1

    for i in range(1, m):
        if route[0][i] == -1:
            break
        route[0][i] = route[0][i - 1]

    for i in range(1, n):
        if route[i][0] == -1:
            break
        route[i][0] = route[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if route[i][j] == -1:
                continue
                
            if route[i - 1][j] != -1:
                route[i][j] += route[i - 1][j]
            if route[i][j - 1] != -1:
                route[i][j] += route[i][j - 1]
                
            route[i][j] %= mod

    return route[n - 1][m - 1]
