"""low=int(input("First: "))
high=int(input("Second: "))
for i in range(low,high+1):
    if i>1:
        for j in range(2, i):
            if (i%j)==0:
                break
        else:
            print(i)"""


low=int(input("First: "))
if low>1:
    for j in range(2, low):
        if (low%j)==0:
            print("Not Prime")
            break
    else:
        print(low,"Prime Number")
