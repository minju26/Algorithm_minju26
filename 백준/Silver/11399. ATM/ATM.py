# boj 11399 :: ATM :: silv.4

import sys
input = sys.stdin.readline

ans_time = []

n = int(input())
time = list(map(int, input().split()))

time.sort()
ans_time.append(time[0])

for i in range(1, n):
    ans_time.append(ans_time[i-1] + time[i])

ans = sum(ans_time)

print(ans)