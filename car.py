
class Car:

    wheels = 4  # class variable

    def __init__(self,make,model,year,color):                # The Constructor

        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):                # self refers to object using this method
        print("This "+self.model +" is driving")

    def stop(self):
        print("This "+ self.model+ " car is stopped")