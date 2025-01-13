# boj 1946 :: 신입 사원 :: silv.1

import sys
input = sys.stdin.readline

t = int(input().strip())
ans = []

for _ in range(t):
    result = 0
    
    n = int(input().strip())
    rank = []

    for _ in range(n):
        i, j = map(int, input().strip().split())
        rank.append((i, j))

    rank.sort()
    min_rank = rank[0][1]

    for i in range(n):

        if min_rank >= rank[i][1]:
            result += 1
            min_rank = rank[i][1]

    ans.append(result)

for result in ans:
    print(result)