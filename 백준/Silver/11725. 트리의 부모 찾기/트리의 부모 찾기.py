# boj 11725 :: 트리의 부모 찾기 :: silv.2

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
adj_list = [[] for _ in range(n+1)]
ans_parent = [0]*(n+1)

# 인접 리스트 생성
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)


# 정점 v의 부모가 par, v의 children을 찾는 함수 
def dfs(v, par):
    for node in adj_list[v]:
        if (node == par): continue
        ans_parent[node] = v    # 자식 노드(node)의 부모(v) 표시
        dfs(node, v)    # 자식 노드의 자식 노드 찾기


def print_ans(ans):
    for i in range(2, n+1):
        print(ans[i])

# 1의 parent를 -1로 표시
dfs(1, -1)
print_ans(ans_parent)
