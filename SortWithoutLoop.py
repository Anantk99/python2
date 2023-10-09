def sot(s):
    l=[]
    for x in range(0,len(s)):
        for  y in range(x+1,len(s)):
            if s[x] >= s[y]:
                s[x],s[y]=s[y],s[x]
    return s
s=[2,73,58,64,27,18,9]
print(sot(s))
