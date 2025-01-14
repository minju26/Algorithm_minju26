# boj 2108 :: 통계학 :: silv.3
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = []
ans = []

for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()

# 산술 평균
mean = round(sum(nums) / n)
print(mean)

# 중앙값
mid = nums[n // 2]
print(mid)

# 최빈값
freq_counter = Counter(nums)
max_freq = max(freq_counter.values())

modes = [num for num, freq in freq_counter.items() if freq == max_freq]
modes.sort()

freq = modes[1] if len(modes) > 1 else modes[0]
print(freq)

# 범위
range = nums[-1] - nums[0]
print(range)