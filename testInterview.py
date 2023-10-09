def test(l):
    l3=[]
    s=set(l)
    for i in s:
        l3.append([i,l.count(i)])
    return l3


l=[11,2,3,3,3,4,5,4,12,10,2,11]
print(test(l))
"""
l=[10,8,3,1,7,5,3,2,1,4,6,2,7,9,4,0,-3]
k=7
"""
