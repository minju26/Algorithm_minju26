import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())

lights = [1] * n
psum = [0] * n
psum[0] = lights[0]

for _ in range(b):
    i = int(input())
    lights[i-1] = 0

for i in range(1, n):
    psum[i] = psum[i-1] + lights[i]

max_psum = -1
for i in range(k-1, n):
    cur_psum = -1

    if i == (k - 1):
        cur_psum = psum[i]
    else:
        cur_psum = psum[i] - psum[i - k]
    
    max_psum = max(max_psum, cur_psum)

print(k - max_psum)