def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    
    def sum(num, i, s):
        nonlocal cnt
        num += numbers[i] * s

        if i == (n - 1):
            if num == target: cnt += 1
            return
        
        sum(num, i + 1, 1)
        sum(num, i + 1, -1)
    
    sum(0, 0, 1)
    sum(0, 0, -1)
    return cnt