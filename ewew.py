N=int(input("Enter a intiger"))
for i in range(N):
    for j in range(N,-i,-1):
        print("",end="")
    for j in range(i,-1,-1):
        print(i+1,end="")
    print()
