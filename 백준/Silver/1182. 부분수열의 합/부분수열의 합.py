import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
ary = list(map(int, input().split()))
sub_ary = []

ans = 0
for size in range(1, n + 1):
    for combination in combinations(ary, size):
        if sum(combination) == s:
            ans += 1

print(ans)
