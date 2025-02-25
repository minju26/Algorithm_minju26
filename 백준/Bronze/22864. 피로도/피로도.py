import sys
input = sys.stdin.readline
a, b, c, m = map(int, input().split())

h = 0
w = 0
p = 0

while h < 24:

    # 일을 하려고 봤더니, 일을 하고 난 후 피로(p + a)가 m을 넘는 경우 => 휴식
    if p + a > m :
        while p > (m - a):
            if h >= 24: break
            h += 1
            p -= c
        if p < 0:
            p = 0
    else:
        # 일 진행
        h += 1
        w += b
        p += a

print(w)