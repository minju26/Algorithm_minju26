def solution(id_list, report, k):
    
    member = len(id_list)
    reporting = [[] for _ in range(member)]
    reported = [0]*member
    suspension = []
    answer = [0]*member
    
    for i in report:
        x, y = i.split()
        if y not in reporting[id_list.index(x)]:
            #신고 한 목록
            reporting[id_list.index(x)].append(y)
            #신고 당한 수
            reported[id_list.index(y)] += 1
    
    for i in range(member):
        if reported[i] >= k: suspension.append(id_list[i])
    
    for s in suspension:
        for i in range(member):
            if s in reporting[i]: answer[i] += 1
    
    return answer