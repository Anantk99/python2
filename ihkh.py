class Student:
	def __init__(self,name,rollno):
            
	    self.name=name
	    self.rollno=rollno

	def deff(self):
            
            print('Hello My Name Is : ',self.name)
            print('Hello My Rollno Is :', self.rollno)

s1=Student('Durga',101)
s1.deff()
