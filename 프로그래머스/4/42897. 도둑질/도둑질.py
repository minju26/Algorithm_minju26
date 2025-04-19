def solution(money):
    
    n = len(money)
    a = [0] * n
    b = [0] * n
    
    a[0] = money[0]
    
    for i in range(1, n):
        if i < n - 1:
            a[i] = max(money[i] + a[i - 2], a[i - 1])
        
        b[i] = max(money[i] + b[i - 2], b[i - 1])
    
    return max(a[n - 2], b[n - 1])