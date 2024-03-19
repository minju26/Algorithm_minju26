def solution(data, ext, val_ext, sort_by):
    answer = []
    tmp = ["code", "date", "maximum", "remain"]
    ext = tmp.index(ext)
    sort = tmp.index(sort_by)
    
    for d in data:
        if d[ext] < val_ext:answer.append(d)
    
    answer.sort(key= lambda data:data[sort])
    return answer