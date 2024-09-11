# boj 1644 :: 소수의 연속 합 :: gold.3

import sys
input = sys.stdin.readline

n = int(input())

def findPrimeNum(num):
    prime = [True for _ in range(num+1)]
    prime[0] = prime[1] = False

    i = 2
    while i*i <= num:
        if prime[i]:
            prime[i*i::i] = [False] * ((num - i*i)//i + 1)
        i += 1
    
    primes = []
    for i in range(len(prime)):
        if prime[i]: primes.append(i)
    
    return primes


# 2부터 n까지의 소수 찾기
primes = findPrimeNum(n)

# pointers
main = 0
sub = 0

ans = 0
if n == 1:
    sum = 0
    end = 1
else:
    sum = primes[main]
    end = len(primes)

while True:
    if sum <= n:
        if sum == n: ans += 1
        sub += 1
        if sub == end: break
        sum += primes[sub]
    else:
        sum -= primes[main]
        main += 1

print(ans)
