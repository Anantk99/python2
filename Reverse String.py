s=input()
def xyz(s,n):
    if n==0:
        print(s[0])
    else:
        print(s[n],end="")
        xyz(s,n-1)
xyz(s,len(s)-1)
