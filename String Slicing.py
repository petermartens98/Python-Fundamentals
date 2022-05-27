# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Peter Martens"

first_name = name[:5]       #[0:5]
last_name = name[6:]        #[6:end]
funky_name = name[::2]      #[0:end:2]  #count every second character
reversed_name = name[::-1]  #[0:end:-1]

print(reversed_name)
print(name[3])         # print 4th character[index] of name

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)   #used a negative index

print(website1[slice])
print(website2[slice])