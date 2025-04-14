def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        prev = 0
        for rock in rocks:
            dist = rock - prev

            if dist < mid:
                cnt += 1
                
                if cnt > n:
                    break
            else:
                prev = rock
                
        if cnt > n:
            end = mid -1
        else:
            answer = mid
            start = mid + 1

    return answer