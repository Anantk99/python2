N=int (input())
sum=0
dum=0
while N>0:
    d=N%10
    if d%2==0:
        sum=sum+d
    else:
        dum=dum+d
    N=N//10
print(sum,dum)
