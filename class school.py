class Student:

    school= "Telusko"                                    # Class Variable

    def __init__(self,m1,m2,m3):                         # Instance Variable

        self.m1= m1
        self.m2= m2
        self.m3= m3

    def ave(self):
        return (self.m1+self.m2+self.m3)/3

s1=Student(34,46,48)                                     # Function Call
s2=Student(24,46,80)                                     # Function Call

print((s1.ave()))
print(s2.ave())
