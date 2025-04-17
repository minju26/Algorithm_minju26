def solution(numbers, target):
    stack = [(0, 0)]
    count = 0
    
    while stack:
        cur, idx = stack.pop()
        
        if idx == len(numbers):
            if cur == target:
                count += 1
        else:
            stack.append((cur + numbers[idx], idx + 1))
            stack.append((cur - numbers[idx], idx + 1))
    
    return count
