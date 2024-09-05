# boj 2003 :: 수들의 합 2 :: silv.5

# 합이 M이상 되는 순간 시작 점 이동
# 시작점을 이동 한 후 현재 끝점+1 부터 합 연산 시작

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = 0
sum = a[0]

ans = 0
while True:
    if sum == m:
        ans += 1
    
    if sum >= m:
        sum -= a[start]
        start += 1
    else:
        if end == n - 1: break

        end += 1
        sum += a[end]

print(ans)