# boj 5525 :: IOIO :: silv.1

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

# 해쉬 값을 계산하기 위한 준비
mod = 1e9 + 7   # 커지는 숫자의 범위를 제한하기 위한 아주 큰 수(나머지를 이용할것임)
po = [0] * m    # 31의 거듭제곱을 저장 할 배열 -> 한번에 계산해두고 가져와서 사용
po[0] = 1   
for i in range(1, m):
    po[i] = po[i-1] * 31 % mod

# Pn 만들기
pn = 'I'
for i in range(n):
    pn += 'OI'

k = len(pn)

# Pn의 해시값 계산 (롤링 해시 방식)
pn_hash = 0
for i in range(k):
    pn_hash *= 31
    pn_hash %= mod

    pn_hash += ord(pn[i]) - ord('A') + 1 # 'A' = 1로 뒀음
    pn_hash %= mod

# s[0:len(pn)]의 해시 값 계산(s문자열에서 pn과 같은 길이의 첫번째 부분 문자열)
s_hash = 0
for i in range(k):
    s_hash *= 31
    s_hash %= mod
    
    s_hash += ord(s[i]) - ord('A') + 1
    s_hash %= mod

ans = 0
# s의 부분 문자열들의 해시 값 계산
for i in range(0, m - k + 1):
    if s_hash == pn_hash:
        ans += 1
    
    # s_hash 갱신
    # 맨 앞 문자 제거 & 자리 올림림
    largest = ord(s[i]) - ord('A') + 1
    s_hash += mod - largest * po[k - 1] % mod   # 뺄샘 과정에서 s_hash 음수 방지를 위해 mod를 더함함
    s_hash %= mod

    s_hash *= 31
    s_hash %= mod
    # 맨 뒤 문자 추가(제일 마지막 부분 문자열 제외)
    if i + k < m: 
        s_hash += ord(s[i + k]) - ord('A') + 1
        s_hash %= mod

print(ans)


