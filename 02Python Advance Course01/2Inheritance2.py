class Animal:
    def eat(self):
        print ('Eating...'  )

class Dog(Animal):
    def bark(self):
        print ('Barking...'  )

class BabyDog(Dog):
    def weep(self):
        print ('Weeping...')

d=BabyDog()
print(d.eat())
print(d.bark())
print(d.weep())

