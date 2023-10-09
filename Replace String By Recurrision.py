def recursionReplace(s,a,b):

    if len(s)==0:
        return s

    change=recursionReplace(s[1:],a,b)
    
    if s[0]==a:
        return b+change
    else:
        
        return  s[0]+ change 

print(recursionReplace("dmcxcdf","c","x"))
