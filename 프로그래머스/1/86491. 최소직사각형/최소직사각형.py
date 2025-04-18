def solution(sizes):
    w = -1
    h = -1
    
    for x, y in sizes:
        w = max(w, (max(x, y)))
        h = max(h, (min(x, y)))

    return w * h
