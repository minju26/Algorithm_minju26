import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = []
ans = -1

for _ in range(n):
    home.append(int(input()))

home.sort()

start = 1
end = home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    cur_home = home[0]
    c_cnt = 1

    for i in range(n):

        if home[i] - cur_home >= mid:
            c_cnt += 1
            cur_home = home[i]
    
    # c_cnt가 c보다 작으면 간격이 너무 길다는 뜻 -> mid를 줄여야 함
    if c_cnt < c:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)