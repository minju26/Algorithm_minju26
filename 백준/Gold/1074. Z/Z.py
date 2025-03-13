import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
ans = 0

while n != 0:
    
    n -= 1
    mid = 2 ** n
    end = 2 ** (n + 1)

    # 왼쪽상단
    if (0 <= r < mid) and (0 <= c < mid):
        ans += (mid ** 2) * 0
    
     # 오른쪽상단
    if (0 <= r < mid) and (mid <= c < end):
        ans += (mid ** 2) * 1
        c -= mid
    
    # 왼쪽하단
    if (mid <= r < end) and (0 <= c < mid):
        ans += (mid ** 2) * 2
        r -= mid
    
    # 오른쪽하단
    if (mid <= r < end) and (mid <= c < end):
        ans += (mid ** 2) * 3
        r -= mid
        c -= mid
    
print(ans)
