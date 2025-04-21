def solution(arr):
    ans = []
    cur = arr[0]
    ans.append(cur)
    
    for i in range(1, len(arr)):
        if cur != arr[i]:
            ans.append(arr[i])
            cur = arr[i]
            
    return ans