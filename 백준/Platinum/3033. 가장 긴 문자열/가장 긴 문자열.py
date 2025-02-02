# boj 3033 :: 가장 긴 문자열 :: plt.3

import sys
input = sys.stdin.readline

l = int(input())
s = input()
ans = 0

# 해시 값을 위한 준비물
mod = 1e9 + 7
po = [0] * l    # po[i] = 31**i
po[0] = 1
for i in range(1, l):
    po[i] = po[i - 1] * 31 % mod

# 이분 탐색(부분 문자열 길이)
start = 1
end = l - 1

while start <= end:
    mid = (start + end) // 2

    # 길이가 mid인 부분 문자열 중에 2번 이상 등장하는 것이 있는지 판단
    found = False   # 찾았음을 표시하는 flag

    hash = 0
    # 처음 해시 값 계산
    for i in range(mid):
        hash *= 31
        hash %= mod
        hash += ord(s[i]) - ord('a') + 1
        hash %= mod
        
    check = {}
    # mid 길이의 슬라이딩 윈도우
    for i in range(0, l - mid + 1):
        # s[i:i+mid] 문자열의 해시 값 체크
        if hash in check:
            # found = True
            # break
            for j in check[hash]:
                if s[j : mid + j] == s[i : i + mid]:    # 실제로 문자열이 같은지 정확하게 확인
                    found = True
                    break
            check[hash].append(i)
            
            if found:
                break
        else:
            check[hash] = [i]

        # 해시 값 갱신
        largest = ord(s[i]) - ord('a') + 1
        hash += mod - largest * po[mid - 1]
        hash %= mod

        hash *= 31
        hash %= mod

        if i + mid < l:
            hash += ord(s[mid + i]) - ord('a') + 1
            hash %= mod

    if found:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)