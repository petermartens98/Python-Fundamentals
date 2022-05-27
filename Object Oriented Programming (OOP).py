# Object Oriented Programming (OOP)

# attributes = is/has
# methods = actions


from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print()

car_1.drive()
car_2.stop()