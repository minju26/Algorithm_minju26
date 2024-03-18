def solution(bandage, health, attacks):

    t = bandage[0]  #시전 시간
    x = bandage[1]  #초당 회복량
    y = bandage[2]  #추가 회복량
    maxHealth = health
    
    lastAttack = attacks[len(attacks)-1][0]
    cnt = 0
    curTime = 0
    
    while health > 0 and curTime <= lastAttack:
        flag = 'X'
        for attack in attacks:
            if attack[0] == curTime:
                cnt = 0
                health -= attack[1]
                flag = 'O'
        if flag == 'X' and health < maxHealth and health > 0:
            health += x
            health = min(health, maxHealth) #
        
        if cnt == t:
            health += y
            health = min(health, maxHealth)
            cnt = 0
        print(curTime, health, cnt, flag)
        
        curTime += 1
        cnt += 1
        
        if health <= 0: return -1
    
    return health