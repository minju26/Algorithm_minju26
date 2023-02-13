import sys

n, m = map(int, sys.stdin.readline().split())
loc = list(map(int, sys.stdin.readline().split()))
maxloc = 0
ploc = []
mloc = []

for i in (loc):
    maxloc = max(abs(i), maxloc)
    if i < 0:
        mloc.append(-i)
    else:
        ploc.append(i)

ploc.sort(reverse=True)
mloc.sort(reverse=True)

result = 0

for i in range(0, len(ploc), m):
    result += ploc[i]*2
for i in range(0, len(mloc), m):
    result += mloc[i]*2
    
print(result-maxloc)