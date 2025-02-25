import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
ans = 0

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for tree in trees:
        if tree >= mid:
            sum += (tree - mid)
    
    if sum < m:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)