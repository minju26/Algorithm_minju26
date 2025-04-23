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
            if len(max_q) * len(min_q) == 0: continue
            
            if data == -1:
                while min_q:
                    num, numid = heapq.heappop(min_q)
                    if numid not in removed:
                        removed.add(numid)
                        break
            else:
                while max_q:
                    num, numid = heapq.heappop(max_q)
                    if numid not in removed:
                        removed.add(numid)
                        break
    
    ans = []
    for num in min_q:
        if num[1] not in removed:
            ans.append(num[0])                    
    
    if ans == []:
        return [0, 0]
    
    return [max(ans), min(ans)]