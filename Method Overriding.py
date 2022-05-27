# Method Overriding

class Animal:

    def eat(self):
        print("This animal is eating")

#class Rabbit(Animal):
#    pass

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()