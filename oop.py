# class is a blueprint of an object
#object is an instance of a class
from os import name


class Employee:

    def __init__(self , name ,gender , position):
        self.name = name
        self.gender = gender
        self.position = position



    def movement(self):
        print("Employee is working")

employee1 = Employee("Mary", "Female" ,"CEO") #creating an object
print(employee1.name)
print(employee1.gender)
employee1.movement()



employee2 = Employee("John", "male" , "Admin")
print(employee2.name)
print(employee2.gender)
employee2.movement()

employee3 = Employee("Mark" ,"male", "Director")
print(employee3.name)
print(employee3.gender)
employee3.movement()

employee4 = Employee("sarah" ,"female" ,"secretary")
print(employee4.name)
print(employee4.gender)
employee4.movement()
