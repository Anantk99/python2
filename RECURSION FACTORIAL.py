
y=int (input())

def power(y):
    if y==1:
        return 1
    else:
        return(y*power(y-1))

z=power(y)
print("version",z)
