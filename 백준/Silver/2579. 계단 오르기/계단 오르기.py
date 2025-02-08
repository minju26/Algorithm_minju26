# boj 2579 :: 계단 오르기 :: silv.3

import sys
input = sys.stdin.readline

# 입력 (n 계단수, stair 계단 점수)
n = int(input())
s = [0] * n
for i in range(n):
    s[i] = int(input())

a = [0] * n
b = [0] * n

a[0] = b[0] = s[0]

for i in range(1, n):
    if i >= 2:
        a[i] = s[i] + max(a[i - 2], b[i - 2])
    else:
        a[i] = s[i]
    
    if i >= 3:
        b[i] = s[i] + s[i - 1] + max(a[i - 3], b[i - 3])
    else:
        b[i] = s[i] + s[i - 1]

print(max(a[n - 1], b[n - 1]))