import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    time, total, i = 0, 0, 0
    hq = []
    
    while i < n or hq:
        
        while i < n and jobs[i][0] <= time:
            req, dur = jobs[i]
            heapq.heappush(hq, (dur, req))
            i += 1
        
        if hq:
            dur, req = heapq.heappop(hq)
            time += dur
            total += time - req
        else:
            time = jobs[i][0]
    
    return total // n
