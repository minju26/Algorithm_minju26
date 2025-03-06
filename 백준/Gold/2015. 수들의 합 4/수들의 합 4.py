import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

psum = [0] * n
psum[0] = a[0]
for i in range(1, n):
    psum[i] = psum[i - 1] + a[i]

ans = 0
cnt = {}
for i in range(n):
    g = psum[i] - k

    if g == 0:
        ans += 1
    if g in cnt:
        ans += cnt[g]

    if psum[i] not in cnt:
        cnt[psum[i]] = 0

    cnt[psum[i]] += 1

print(ans)