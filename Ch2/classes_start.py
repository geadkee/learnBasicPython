#
# Example file for working with classes
#

class Vehicles():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle;     #"Vehicle()" class has "bodystyle" property
    wheels = 3;

    def Drive(self, speed, distance, time):
        self.speed = speed
        self.mode = "driving"

class Car(Vehicles):
    def __init__(self, enginetype):
        super().__init__("Car")         #"super().__init__()" is to initalise the "bodystyle" property in the Vehicle() class. 
        self.wheel = 4
        self.doors = 4
        self.cylinder = 4
        self.enginetype = enginetype

    def Drive(self, speed, distance, time):
        super().Drive(speed, distance, time)
        return print("Driving my ", self.enginetype, self.enginetype ," at speed ", self.speed)

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

car1 = Car("Manual");
car2 = Car("Auto");
bike1 = Bike("Gas", True);

print(car1.cylinder)
print(car2.enginetype)
print(car1.wheels, car1.wheel)
print(bike1.hasSideCar)

car1.Drive(60)
car2.Drive(120)


def main():
    print("classes")


if __name__ == "__main__":
    main()
