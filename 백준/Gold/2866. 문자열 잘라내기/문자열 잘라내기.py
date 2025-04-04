import sys
input = sys.stdin.readline

r, c = map(int, input().split())
table = [list(input().strip()) for _ in range(r)]
strings = []

for i in range(c):
    s = ''
    for j in range(r):
        s += table[j][i]
    strings.append(s)

start = 0
found = False
while start <= r:
    dic = {}
    for i in range(c):
        if strings[i][start : r] in dic:
            found = True
            break
        dic[strings[i][start : r]] = 1
    
    if found:
        start -= 1
        break
    else:
        start += 1

print(start)