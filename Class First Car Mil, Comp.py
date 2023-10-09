class Car:

    def __init__(self):
        self.mil=10
        self.comp="BMW"                  # Instant Variable

c1=Car()
c2=Car()                                 # Object Calling


c1.mil=8                                 # Changing Mil 


print(c1.mil,c1.comp)
print(c2.mil,c2.comp )
