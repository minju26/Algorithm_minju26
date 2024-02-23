from collections import defaultdict

def solution(N, number):
    dp = defaultdict(set)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0: dp[i].add(n1 // n2) 

        if number in dp[i]: return i 

    return -1 