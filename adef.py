def RedOrGreen(N,S):
    
        #code here
    if len(S)==1:
        return S
    v=0
        
    S=list(S)
    d=len(S)+1
    for i in range(d):
        if i==len(S):
            break
        if S[i]!=S[i+1]:
            v=v+1
                
    return v
S="RGRGR"
N=5

print(RedOrGreen(N,S))
