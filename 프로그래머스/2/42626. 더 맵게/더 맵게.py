import heapq as hq

def solution(scoville, k):
    if k == 0:
        return 0

    hq.heapify(scoville)
    
    cnt = 0
    while True:
        fst = hq.heappop(scoville)

        if not scoville and fst < k:
            return -1
        
        if fst >= k:
            return cnt

        scnd = hq.heappop(scoville)
        new = fst + (scnd * 2)
        hq.heappush(scoville, new)
        cnt += 1