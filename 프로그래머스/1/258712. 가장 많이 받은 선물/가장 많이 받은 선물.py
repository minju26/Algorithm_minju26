def solution(friends, gifts):
    
    print(friends)
    print(gifts)
    
    f = len(friends)
    
    #주고받음을 저장
    state = [[0]*f for _ in range(f)]
    
    rate = [0]*f
    ntake = [0]*f
    
    for g in gifts:
        give, take = map(str,g.split())
        state[friends.index(give)][friends.index(take)] += 1
    
    for i in range(f):
        g = 0
        t = 0
        for j in range(f):
            g = g + state[i][j]
            t = t + state[j][i]
        rate[i] = g - t
    
    for i in range(f):
        for j in range(i+1, f):            
            if state[i][j] == state[j][i]:
                if rate[i] > rate[j]:
                    ntake[i] += 1
                elif rate[i] < rate[j]:
                    ntake[j] += 1
            elif state[i][j] < state[j][i]:
                ntake[j] += 1
            else: ntake[i] += 1
                
    
    answer = max(ntake)
    return answer