S= ["RaHuL","Virat","sachin","dhoni","Kapil"]
l=[]
for x in S:
    count=0
    for y in x:
        if y.isupper():
            count+=1
    l.append(count)
print(l)
