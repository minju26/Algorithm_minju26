# boj 2559 :: 수열 :: silv.3

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
days = list(map(int, input().split()))

start = 0
end = k-1

ans = sum(days[start:end+1])
new = ans

while True:
    if end == n-1: break
    end += 1
    new = new - days[start] + days[end]
    ans = max(ans, new)
    start += 1


print(ans)