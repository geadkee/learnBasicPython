#
# Example file for working with classes
#

class Vehicles():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle;     #"Vehicle()" class has "bodystyle" property
    wheels = 3;

    def Drive(self, distance, time):    # defining a function in a class
        self.distance = distance
        self.time = time
        self.mode = "driving"

class Car(Vehicles):
    def __init__(self, enginetype):
        super().__init__("Car")         #"super().__init__()" is to initalise the "bodystyle" property in the Vehicle() class. 
        self.wheel = 4
        self.doors = 4
        self.cylinder = 4
        self.enginetype = enginetype

    def Drive(self, distance, time):    #derive a function from it's parent class
        super().Drive(distance, time)
        self.speed = distance/time
        return print("Driving my ", self.enginetype, self.bodystyle ," at speed ", self.speed, "meter/min")

class Bike(Vehicles):
    def __init__(self, enginetype, hasSideCar):
        super().__init__("Bike")        #"super().__init__()" is to initalise the "bodystyle" property in the Vehicle() class. 
        if(hasSideCar):
            self.wheel = 3
        else:
            self.wheel = 2
        self.enginetype = enginetype
        self.hasSideCar = hasSideCar
        self.cylinder = 2

    def Drive(self, distance, time):    #derive a function from it's parent class
        super.Drive(distance, time)
        self.speed = distance/time;
        return print("Riding my ", self.enginetype, self.bodystyle, " at speed ", self.speed, "meter/min")

car1 = Car("Manual");
car2 = Car("Auto");
bike1 = Bike("Gas", True);

print(car1.cylinder)
print(car2.enginetype)
print(car1.wheels, car1.wheel)
print(bike1.hasSideCar)

car1.Drive(60, 10)
car2.Drive(120, 10)


# def main():
#     print("classes")


# if __name__ == "__main__":
#     main()
