def romanToDecimal(S): 

        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000
        p=[]
        l1=[]
        for vals in S:
            p.append(vals)
            print(p)
        for char in range(0,len(S)):
            
            if p[char]=="X":
                l1.append(1)
            if p[char]=="V":
                l1.append(5)
            if p[char]=="X":
                l1.append(10)
            if p[char]=="L":
                l1.append(50)
            if p[char]=="C":
                l1.append(100)
            if p[char]=="D":
                l1.append(500)
            if p[char]=="M":
                l1.append(1000)
        return sum(l1)
S="XXIII"
print(romanToDecimal(S))
