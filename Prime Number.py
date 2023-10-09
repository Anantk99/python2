Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n= int(input(": "))
if n<2:
    print("Not Prime")
for i in range(2,n):
    if n%i==0:
        print('Not Prime ')
        break
else:
    print("Prime ")