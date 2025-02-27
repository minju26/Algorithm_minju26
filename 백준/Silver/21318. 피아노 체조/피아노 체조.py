import sys
input = sys.stdin.readline

n = int(input())
lv = list(map(int, input().split()))
q = int(input())
ans = []

#전체 lv 배열에서 실수 여부를 저장하는 배열 생성
miss = [0] * n
for i in range(n - 1):
    if lv[i + 1] < lv[i]:
        miss[i] = 1

psum = [0] * n
psum[0] = miss[0]
for i in range(1, n):
    psum[i] = psum[i - 1] + miss[i]

for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    if x == y:
        print(0)
        continue
    
    # x 부터 y - 1 까지의 psum
    cnt = psum[y - 1]
    if x > 0:
        cnt -= psum[x - 1]
    
    print(cnt)

