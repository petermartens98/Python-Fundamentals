# Lambda Function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parmeters:expression

double = lambda x: x * 2
print(double(5))
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_nume = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False
print(age_check(18))
