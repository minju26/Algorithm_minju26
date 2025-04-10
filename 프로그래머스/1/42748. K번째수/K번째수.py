def solution(array, commands):
    ans = []

    for c in commands:
        i, j, k = c
        ans.append(sorted(array[i - 1 : j])[k - 1])
        
    return ans