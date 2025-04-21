def solution(parenthesis):
    s = '('
    e = ')'
    
    stack = []
    for p in parenthesis:
        if p == s:
            stack.append(p)
        if p == e:
            if stack == []:
                return False
            stack.pop()
    
    if stack == []:
        return True
    else:
        return False
