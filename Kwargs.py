# **kwargs =  parameter that will pack all arguments into a dictionary
#             useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):      #** is the important part
    #print("Hello " + kwargs['first'] + " " + kwargs['last']
    print("Hello",end=" ")    #replace new line character, with a space
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Peter",middle="Frederick",Last="Martens")
