def isRotated(str1,str2):

   '''
    l1=[]
    l2=[]
    for i in str1:
        l1.append(i)
        print(l1)
    
    l1.pop()
    l1.pop()
    print(l1)
    for j in l1:
        "".join(l1)
    
        
        print(j,end="")
   '''
   a=str1[2:] + str1[:2]
   b=str2[2:] + str2[:2]
   
   if a==str1 or b==str2:
       return 1
   
str1="fsbcnuvqhffbsaqxwp"
str2="wpfsbcnuvqhffbsaqx"
print(isRotated(str1,str2))
