import sys
input = sys.stdin.readline

n = int(input())

cnt5 = 0
cnt2 = 0

if n == 1 or n == 3:
    print("-1")
else:
    if n % 5== 0:
        cnt5 = n // 5
    elif (n % 5) % 2 == 0:
        cnt5 = n // 5
        cnt2 = (n % 5) // 2
    else:
        cnt5 = n // 5 - 1
        cnt2 = (n - 5 * cnt5) // 2

    print(cnt5 + cnt2)