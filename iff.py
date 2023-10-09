name=float(input("Weight: "))
we=input("(L)bs or (W)g ")
if we.upper()=="L":
    converter = name * 0.45
    print(f"you are {converter} kilos: ")
else:
    converter=name /0.45
    print(f"you are {converter} pounds ")
