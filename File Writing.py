# File Writing

text = "Hello\nThis is some text\nHave a good day\n"

with open('test.txt','w') as file:
    file.write(text)

with open('test.txt') as file:
    print(file.read())