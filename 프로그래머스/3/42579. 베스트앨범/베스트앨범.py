from collections import defaultdict

def solution(genres, plays):
    ans = []
    
    p_dict = defaultdict(list)
    totalp_dict = defaultdict(int)
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        p_dict[genre].append((play, index))
        totalp_dict[genre] += play
    
    for key in p_dict:
        p_dict[key] = sorted(p_dict[key], key=lambda x: (-x[0], x[1]))
    
    s_totalp = sorted(totalp_dict.items(), key=lambda item: item[1], reverse = True)
    
    for genre, total in s_totalp:
        for i in range(min(2, len(p_dict[genre]))):
            ans.append(p_dict[genre][i][1])
    
    return ans