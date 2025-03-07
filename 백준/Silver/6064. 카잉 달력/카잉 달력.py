import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    # m >= n 설정
    if m < n:
        m, n = n, m
        x, y = y, x
    
    f = False
    # y일 = <y, y>
    x_ = y
    for i in range(m):
        if x_ == x:
            print(y + i * n)
            f = True
            break
        
        x_ += n
        if x_ > m:
            x_ -= m
    
    if not f:
        print(-1)