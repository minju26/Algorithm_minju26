# boj 2343 :: 기타 레슨 :: silv.1

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lec = list(map(int, input().split()))

start = max(lec)
end = sum(lec)
ans = -1

while (start <= end):

    mid = (start + end) // 2
    
    # 현재 블루레이 넘버
    num = 1
    # 용량 확인
    remain = mid

    for i in range(n):
        if remain < lec[i]:
            num += 1
            remain = mid

        remain -= lec[i]
    
    if num <= m:
        ans = mid   # m보다 적게 사용하는 경우는 용량이 큰 경우이므로, 최적의 용량을 찾기 위해서는 m개를 모두 사용해야 함.
        end = mid - 1
    else:
        start = mid + 1

print(ans)