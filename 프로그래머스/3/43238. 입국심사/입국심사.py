def solution(n, times):
    ans = 0
    
    start = 1
    end = min(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for time in times:
            cnt += mid // time
            
            if cnt >= n: break
        
        if cnt < n:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    
    return ans