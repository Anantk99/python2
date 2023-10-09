x=int(input("Enter a number"))
s=0
while(x):
    r=x%10
    s=s+r
    x=x//10
    print("Sum of digits is",s)
    s=s+1
