# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Peter",23,"male")

print(student.count("Peter"))
print(student.index("male"))

for x in student:
    print(x)

if "Peter" in student:
    print("Peter is here!")