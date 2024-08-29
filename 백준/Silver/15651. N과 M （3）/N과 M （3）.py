# boj 15651 :: N과 M(3) :: silv.3

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ans = []
selected = []

def recur(k):
    if (k == m):
        ans.append(' '.join(map(str, selected)))
        return
    else:
        for i in range(1, n+1):
            selected.append(i)
            recur(k+1)
            selected.pop()

recur(0)
print('\n'.join(ans))