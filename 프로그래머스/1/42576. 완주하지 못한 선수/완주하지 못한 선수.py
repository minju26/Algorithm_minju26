def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    pos = 0
    while pos < len(completion):
        if participant[pos] != completion[pos]:
            break
        pos += 1
    
    answer = participant[pos]
    return answer