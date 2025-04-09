def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)

    for i in range(n):
        if citations[i] < i + 1:
            return i
    
    # [3, 3, 3]
    return n
