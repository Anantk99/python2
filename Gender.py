gender=input("M or F: " )
marrige= input("Yes or No: ")
age=int(input("Enter your age: "))
if gender =="F":
    print("Women should work in Urbal area ")

if gender== "M" and age<=20 or age<40:
    print(f"Male {age} should work in Rural area ")

elif gender== "M" and age<=40 or age<=60:
    print(f"Males {age} Should work in Urban area")

else :
    print("Error")
