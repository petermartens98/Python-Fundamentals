# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "Peter Martens"

#if(name[0].islower()):
#    name = name.capitalize()

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
