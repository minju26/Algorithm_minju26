import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
target = int(input())
ans = 0

# 루트 노드 찾기
for i in range(n):
    if parent[i] == -1:
        root = i
        break

# 사라지는 노드 색칠 -> target노드와 target노드를 부모/조상 노드로 가지는 자식 노드를 칠한다
black = [0] * n
for i in range(n):
    u = i
    while True:
        if u == target:
            black[i] = 1
            break

        if u == root:
            break

        u = parent[u]

# 리프 노드가 아닌(=자식이 있는 노드) 색칠 -> 자식의 부모 노드를 칠한다
red = [0] * n
for i in range(n):
    # 사라진 노드면 패스
    if black[i] == 1:
        continue

    if i == root:
        continue

    red[parent[i]] = 1

for i in range(n):
    if black[i] == 1 or red[i] == 1:
        continue

    ans += 1

print(ans)