# boj 2521 :: 예산 :: silv.2

import sys
input = sys.stdin.readline

n = int(input())
jibang = list(map(int, input().split()))
budget =int(input())

ans = -1
start = 0
end = max(jibang)

while(start <= end):

    mid = (start + end) // 2
    sum = 0

    for price in jibang:
        # if price > mid:
        #     sum += mid
        # else:
        #     sum += price
        sum += min(mid, price)

    if sum <= budget:
        ans = mid   # 답이 될 수 있으므로 기록해둔다
        start = mid + 1
    else:
        end = mid - 1

print(ans)