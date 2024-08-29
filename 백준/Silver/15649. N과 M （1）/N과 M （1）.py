# boj 15649 :: N과 M(1) :: silv.3

# 만약 M개를 전부 골랐다면, 조건에 맞는 탐색을 한 가지 성공한 것.
# 아직 M개를 고르지 않았다면, k번째부터 M번째 원소를 조건에 맞게 고르는 모든 방법 시도

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ans = []
selected = []
used = [False]*(n+1)

def recur(k):
    # m개를 모두 고른 경우
    if (k == m):
    	# 숫자 사이에 공백을 둔 문자열로 저장
        ans.append(' '.join(map(str, selected)))
        return
    else:
        for i in range(1, n+1):
            # 중복 제거를 위한 조건
            if(used[i] == True): continue

            selected.append(i)
            used[i] = True
            recur(k+1)
            selected.pop()	# 마지막 원소 제거
            used[i] = False

recur(0)
print('\n'.join(ans))