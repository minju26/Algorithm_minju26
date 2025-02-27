import sys
from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())
alphabets = list(input().strip().split())
alphabets.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
ans = []

# 만들어진 암호가 조건을 만족하는지 확인(모음 1개 이상, 자음 2개 이상)
for combination in combinations(alphabets, l):
    v = 0
    c = 0
    for i in range(len(combination)):
        if combination[i] in vowel:
            v += 1
        else:
            c += 1
    
    if v >= 1 and c >= 2:
        ans.append(combination)

for result in ans:
    print("".join(result))