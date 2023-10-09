N=int (input())
rev=0
x=N

while N>0:
    rev=(rev*10)+N%10
    N=N//10
if (x==rev):
    print("Palindrom")
else:
    print("Not Palindrom")
