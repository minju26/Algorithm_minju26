import heapq

def solution(operations):
    max_q = []
    min_q = []
    removed = set()
    
    i = 0
    for op in operations:
        operation, data = op.split()
        data = int(data)
        
        if operation == 'I':
            heapq.heappush(min_q, (data, i))
            heapq.heappush(max_q, (data * (-1), i))
            i += 1
        
        if operation == 'D':
            if not max_q or not min_q: continue
            
            q = min_q if data == -1 else max_q
            
            while q:
                num, numid = heapq.heappop(q)
                if numid not in removed:
                    removed.add(numid)
                    break

    max_val = None
    while max_q:
        val, idx = heapq.heappop(max_q)
        if idx not in removed:
            max_val = -val
            break

    min_val = None
    while min_q:
        val, idx = heapq.heappop(min_q)
        if idx not in removed:
            min_val = val
            break

    if max_val is None or min_val is None:
        return [0, 0]

    return [max_val, min_val]
