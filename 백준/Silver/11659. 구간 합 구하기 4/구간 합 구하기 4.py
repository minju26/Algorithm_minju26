import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

psum = [0] * n
psum[0] = nums[0]

for i in range(1, n):
    psum[i] = psum[i-1] + nums[i]


for _ in range(m):
    i, j = map(int, input().split())
    
    if i == 1: 
        ans.append(psum[j-1])
    else:
        ans.append(psum[j-1] - psum[i-2])

for result in ans:
    print(result)