import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

world = [[0] * w for _ in range(h)]

# 블럭 표시
for i in range(w):
    for j in range(blocks[i]):
        world[h - 1 - j][i] = 1

ans = 0
for i in range(h):
    for j in range(w):
        # 블럭 존재
        if world[i][j] == 1:
            continue
        
        # 빈 공간
        k = j

        # 왼쪽 벽 확인
        while k >= 0:
            if world[i][k] == 1:
                break
            k -= 1

        # 왼쪽벽 없음
        if k == -1:
            continue
        
        # 오른쪽 벽 확인
        k = j
        while k < w:
            if world[i][k] == 1:
                break
            k += 1
        
        # 오른쪽 벽 없음
        if k == w:
            continue

        ans += 1

print(ans)