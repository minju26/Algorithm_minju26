import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = -1

for p in permutations(a, n):
    p = list(p)
    temp = 0

    for i in range(n-1):
        temp += abs(p[i] - p[i+1])
    
    ans = max(ans, temp)

print(ans)