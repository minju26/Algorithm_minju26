while True:
    try:
        s, t = input().split()
        
        pos = 0
        g = True
        for i in range(len(s)):
            while pos < len(t) and t[pos] != s[i]:
                pos += 1
                
            if pos < len(t):
                pos += 1
            else:
                g = False
                break
        if g:
            print("Yes")
        else:
            print("No")
    except:
        break