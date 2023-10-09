year= int(input("Enter year of services: "))

if year < 5:
    print("Soon")


elif year >=5 :
    salary = float(input("Enetr your salary: "))

    bonus= (salary * 0.05)
    print(f"your ${bonus} is ")

else :
    print("Keep working")
    
