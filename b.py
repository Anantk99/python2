def missingNumber(array,n):
        # code here
        l1=0
        array=sorted(array)
        for i in range(1,n+1) :
            if n != array[-1]:
                return n
            elif i not in array:

                return i

array=[1,2,3,5]
n=5
print(missingNumber(array,n))
