# boj 1806 :: 부분합 :: gold.4

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

main = 0
sub = 0

sum = nums[main]
ans = n

while main <= sub:

    if sum < s: 
        sub += 1
        if sub < n:
            sum += nums[sub]
        else: break
    else:
        ans = min(ans, sub-main + 1)
        sum -= nums[main]
        main += 1

    

if ans == 10000: print(0)
else: print(ans)