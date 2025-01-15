# boj 2847 :: 게임을 만든 동준이 :: silv.4

import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]

ans = 0

for i in range(n-1, 0, -1):

    if score[i] <= score[i-1]:
        gap = score[i-1] - score[i] + 1
        ans += gap
        score[i-1] -= gap

print(ans)