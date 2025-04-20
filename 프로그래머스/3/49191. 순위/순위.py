def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for w, l in results:
        graph[w][l] = 1
        graph[l][w] = -1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1

    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] != 0:
                cnt += 1
        if cnt == n - 1:
            ans += 1

    return ans
