from collections import defaultdict

def solution(clothes):
    dclothes = defaultdict(int)
    
    for name, kind in clothes:
        dclothes[kind] += 1
    
    ans = 1
    for c in dclothes.values():
        ans *= (c + 1)
    
    return ans - 1