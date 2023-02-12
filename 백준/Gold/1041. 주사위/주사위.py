import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(sum(num_list) - max(num_list))
else:
    min_list = [min(num_list[0], num_list[5])
            , min(num_list[1], num_list[4])
            , min(num_list[2], num_list[3])]

    min_list.sort()

    s1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    s2 = 4*(n-1) + 4*(n-2)
    s3 = 4

    ans = s1*min_list[0] + s2*(min_list[0] + min_list[1]) + s3*(sum(min_list))

    print(ans)