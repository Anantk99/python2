Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def  divide (x,y):
    return x/y

print("Select Operation ")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Division")

choice=input("enter choice (1/2/3/4):")
if choice in ('1','2','3','4'):
    num1=int(input("enter a Number"))
    num2=int(input('enter a number'))

    if choice=='1':
        print(num1,'+',num2,"=",add(num1,num2))
    elif choice=="2":
        print(num1,"-",num2,"-",substraction(num1,num2))
    elif choice=="3:":
        print(num1,"*",num2,"=",multiplication(num1,num2))
    elif choice=="4":
        print(num1,"/",num2,"=",divide(num1,num2))
    else:
        print('Envalid Outpout')