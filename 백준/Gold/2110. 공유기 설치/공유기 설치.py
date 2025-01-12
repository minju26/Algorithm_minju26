# boj 2110 :: 공유기 설치 :: gld.4

import sys

input = sys.stdin.readline

home = []

n, c = map(int, input().split())
for _ in range(n):
    home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]
ans = -1

while start <= end:
    mid = (start + end) // 2
    cur_c = 1
    cur_home = home[0]
    # nxt_home = -1  => 굳이 이전 집을 계속 기억할 필요가 없다

    for i in range(1, n):
        '''
        if home[i] - cur_home <= mid:
            nxt_home = home[i]
        else:
            ans = min(ans, cur_home - nxt_home)  => distance를 따로 계산할 필요가 없다. (탐색중인 mid 값으로 답을 결정할 것이므로.)
            cur_c += 1
            cur_home = nxt_home
            nxt_home = home[i]
        '''
        
        # cur_home과 현재 좌표 거리가 mid 보다 같거나 길다면 cur_c 증가
        # (mid보다 길면 이전 좌표에 공유기 설치/mid보다 같다면 현재 좌표에 공유기 설치 , cur_home을 현재 좌표로 수정)
        if home[i] - cur_home >= mid:
            cur_c += 1
            cur_home = home [i]
        
    # 모든 집 탐색 후 사용된 공유기의 수가 c 보다 크다면 거리 늘이고(start를 수정)
    # 작거나 같다면 ans로 기록하고 거리를 줄여봄(end를 수정)
    if cur_c < c:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
        # cur_c == c 의 경우도 여기에 포함되는 이유는, ans에 기록해두기 때문에 기록해두고 업데이트 해보면됨 => 최적을 찾는 것이므로

print(ans)



        