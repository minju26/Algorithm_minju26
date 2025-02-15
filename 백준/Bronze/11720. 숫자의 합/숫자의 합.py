import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

ans = 0
for i in range(n):
    ans += int(s[i])

print(ans)