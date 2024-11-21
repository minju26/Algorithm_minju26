# boj 10819 :: 차이를 최대로 :: silv.2
# 가능한 모든 순서의 배열에서 합을 구해본다.

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

max_diff_sum = 0
for p in permutations(numbers, n):
    diff_sum = 0
    for i in range(n-1):
        diff_sum += abs(p[i] - p[i+1])
    
    max_diff_sum = max(max_diff_sum, diff_sum)

print(max_diff_sum)