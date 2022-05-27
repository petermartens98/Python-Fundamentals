# File Reading

try:
    with open('ReadingText.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

print(file.closed)