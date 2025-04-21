def solution(progresses, speeds):    
    ans = []
    n = len(progresses)

    start = 0
    while True:
        if start > n - 1: return ans

        for i in range(start, n):
            progresses[i] += speeds[i]
        
        cnt = 0
        while start < n and progresses[start] >= 100:
            cnt += 1
            start += 1
        
        if cnt != 0:
            ans.append(cnt)