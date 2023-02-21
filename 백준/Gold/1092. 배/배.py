import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

cnt = 0

if box[0] > crane[0]:
    print(-1)
else:
    while len(box) > 0:
        cnt += 1
        for i in crane:
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
    print(cnt)