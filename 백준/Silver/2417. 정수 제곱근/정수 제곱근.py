# q^2 >= n 인 q값 찾기
import sys

input = sys.stdin.readline

n = int(input())

start = 0
end = 2 ** 63

ans = 0
while start <= end:
    mid = (start + end) // 2

    if (mid ** 2) >= n:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
