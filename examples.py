l1=["sachin","Virat","Rahul","aaa","RAJ","YAsh"]
l=[]
for x in l1:
    for y in range(0,len(x)):
        name=0
        if l1[y].isupper():
            name+=1
    if name%2==0:
        l.append(x)
    
print(len(l))

sachin=0
Virat=1
Rahul=1
aaa=0
YAsh=2
