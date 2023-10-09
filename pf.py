def pfact(s):
    temp=1
    a="a"
    for i in range(len(s),1,-1):
        if len(a)==1:
            temp=temp*i
        else:
            temp=temp*(i-1)
    return temp * s
s="AAB"
print(pfact(s))
