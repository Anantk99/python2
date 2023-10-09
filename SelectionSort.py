Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> arr1=[3,5,7,6,1,9,19]
arr2=len(arr1)
count=0
for i in range(arr2):

    for j in range(arr2-1):
        if arr1[j]>arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
            count=count+1
print(arr1)