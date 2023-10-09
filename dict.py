arr=[1,2,2,3,4]
d={}
l1=[]
l2=[]
l3={}
for i in range(len(arr)):
    if i not in arr:
        l1.append(i)
    elif i not in l2:
        l2.append(i)
        l3[i]=arr.count(i)
print(max(list(l3.values()),key=list(l3.values()).count))
