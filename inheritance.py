
#PARENT CLASS
class Animal:
    isMammal = True
    gender = 'male'
    age = 2

    def movement(self):
        print("Animal is moving")

#CHILD Class/sub class/ derived class
class Cow(Animal):
    def moow(self):
        print("Cow is moving")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

mycow = Cow()
mycow.moow()

mycat = Cat()
mycat.movement()