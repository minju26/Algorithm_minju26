import sys
input = sys.stdin.readline

s = input().strip()

nk = nr = 0
for i in range(len(s)):
    if s[i] == "K":
        nk += 1
    if s[i] == "R":
        nr += 1

start = -1
end = len(s)

ans = 0
for i in range(nk // 2 + 1):
    if nr == 0:
        break

    ans = max(ans, 2 * i + nr)

    start += 1
    end -= 1
    while start < end and s[start] != "K":
        start += 1
        nr -= 1
    
    while start < end and s[end] != "K":
        end -= 1
        nr -= 1

print(ans)
