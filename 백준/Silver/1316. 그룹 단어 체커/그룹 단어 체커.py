import sys

input = sys.stdin.readline

n = int(input())
ans = 0

for _ in range(n):
    word = input().strip()
    visited = [False] * 28

    now = word[0]
    index = ord(word[0]) - ord('a')
    visited[index] = True

    found = True
    for i in range(1, len(word)):
        index = ord(word[i]) - ord('a')

        if word[i] == now:
            now = word[i]
        
        else:
            if not visited[index]:
                visited[index] = True
                now = word[i]
            else:
                found = False
                break
    
    if found:
        ans += 1

print(ans)
