from queue import PriorityQueue

def solution(scoville, k):
    if k == 0:
        return 0

    pq = PriorityQueue()
    for s in scoville:
        pq.put(s)
    
    cnt = 0
    while True:
        fst = pq.get()
        
        if pq.qsize() == 0 and fst < k:
            return -1
        
        if fst >= k:
            return cnt
        
        scnd = pq.get()
        new = fst + (scnd * 2)
        pq.put(new)
        cnt += 1
        