import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
c = [[] for _ in range(n)]

for i in range(n):
    c[i] = list(map(int, input().split()))

ans = 1e9
for combination in combinations(list(range(n)), n // 2):
    team_a = combination
    team_b = []
    for i in range(n):
        if i not in team_a:
            team_b.append(i)
    
    p_a = 0
    p_b = 0

    for x in team_a:
        for y in team_a:
            p_a += c[x][y]

    for x in team_b:
        for y in team_b:
            p_b += c[x][y]
    
    diff = abs(p_a - p_b)
    if ans > diff:
        ans = diff

print(ans)

