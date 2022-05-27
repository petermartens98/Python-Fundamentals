# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true

# infinite loop
#while 1==1:
#    name = print("Help! I'm stuck in a loop!")

#name = ""

#while len(name) == 0:
#    name = input("Enter your name: ")

# print("Hello "+name)


name = None

while not name:
    name = input("Enter your name: ")

print("Hello "+name)