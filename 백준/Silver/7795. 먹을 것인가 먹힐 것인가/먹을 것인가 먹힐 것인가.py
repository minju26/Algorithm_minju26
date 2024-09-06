# boj 7795 :: 먹을 것인가 먹힐 것인가 :: silv.3

import sys
input = sys.stdin.readline

caseNum = int(input().strip())

for _ in range(caseNum):    
    # input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # sort
    a.sort()
    b.sort()

    # pointers
    main = 0
    sub = 0

    count = 0

    while main < n:

        if sub == m:
            count += sub
            main += 1
        else:
            if a[main] > b[sub]:
                sub += 1
            else:
                count += sub
                main += 1
    
    print(count)