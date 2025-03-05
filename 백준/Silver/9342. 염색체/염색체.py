import sys
input = sys.stdin.readline

t = int(input())
rule = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(t):
    str = input().strip()

    if str[0] not in rule or len(str) < 3:
        print('Good')
        continue

    g = str[0]
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            continue
        else:
            g += str[i]
    
    if len(g) == 3:
        if g == "AFC": print("Infected!")
        else: print("Good")
    
    elif len(g) == 4:
        if g[0 : 3] == "AFC" and g[-1] in rule:
            print("Infected!")
        elif g[1 : 4] == "AFC" and g[0] in rule:
            print("Infected!")
        else:
            print("Good")
    
    elif len(g) == 5:
        if g[0] in rule and g[-1] in rule and g[1 : 4] == "AFC":
            print("Infected!")
        else:
            print("Good")
    
    else:
        print("Good")