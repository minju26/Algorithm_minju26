# boj 2309 :: 일곱 난쟁이 :: brz.1

import sys
from itertools import combinations

input = sys.stdin.readline

heights = []
for _ in range(9):
    heights.append(int(input()))

for a in combinations(heights, 7): 
    if sum(a) == 100:
        a = list(a)
        a.sort()
        for x in a:
            print(x)
        break