def solution(participant, completion):
    hash_loser = sum([hash(a) for a in participant])-sum([hash(a) for a in completion])
    
    for a in participant:
        if hash(a) == hash_loser:
            return a