def solution(nums):
    n = len(nums) // 2
    snums = set(nums)
    
    if len(snums) >= n:
        return n
    else: return len(snums)