def fab(N):
    f=[0,1]
    for i in range(2,N+1):
        f.append(f[i-1]+f[i-2])
    return f[N]
inp=int(input("Enter a intiger: "))
print(fab(inp))
