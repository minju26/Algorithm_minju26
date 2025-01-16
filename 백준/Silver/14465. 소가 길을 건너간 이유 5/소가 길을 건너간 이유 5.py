import sys
input = sys.stdin.readline

n, k, b = list(map(int, input().split()))

check = [0] * n

for _ in range(b):
    id = int(input())
    check[id -1] = 1

psum = [0] * n
psum[0] = check[0]

for i in range(1, n):
    psum[i] = psum[i - 1] + check[i]

need = []
for i in range(0, n - k + 1):
    if i == 0:
        num = psum[i + k - 1]
    else:
        num = psum[i + k - 1] - psum[i - 1]
    
    need.append(num)

print(min(need))