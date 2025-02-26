import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
ary = list(map(int, input().split()))
sub_ary = []

ans = 0
for size in range(1, n + 1):
    sub = list(combinations(ary, size))
    sub_ary.append(sub)

for sub in sub_ary:
    for i in range(len(sub)):
        if sum(sub[i]) == s:
            ans += 1

print(ans)
