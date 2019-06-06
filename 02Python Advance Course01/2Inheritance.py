class Animal:
    def eat(self):
        print("I am Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d=Dog()
print(d.eat())
print(d.bark())


