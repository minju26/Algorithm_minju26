import sys
input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

q = int(input())
for _ in range(q):
    option, k = map(int, input().split())
    k -= 1

    # 단절점
    if option == 1:
        if len(adj[k]) == 1:
            print("no")
        else:
            print("yes")

    # 단절선
    if option == 2:
        print("yes")