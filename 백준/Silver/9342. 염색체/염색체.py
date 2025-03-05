import sys
input = sys.stdin.readline

t = int(input())
rule = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(t):
    str = input().strip()

    if len(str) < 3:
        print("Good")
        continue

    if str[0] != "A":
        if str[0] not in rule:
            print("Good")
            continue
        str = str[1:]
    
    if str[-1] != "C":
        if str[-1] not in rule:
            print("Good")
            continue
        str = str[:-1]
    
    g = str[0]
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            continue
        else:
            g += str[i]
    
    if g == "AFC":
        print("Infected!")
    else:
        print("Good")
