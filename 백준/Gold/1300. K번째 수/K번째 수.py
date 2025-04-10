import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = n * n
ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, (mid - 1) // i)
    
    if cnt < k:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)