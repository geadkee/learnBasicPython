#
# Example file for working with classes
#

class Vehicles():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle;
    wheels = 3;

class Car(Vehicles):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheel = 4
        self.doors = 4
        self.cylinder = 4
        self.enginetype = enginetype

class Bike(Vehicles):
    def __init__(self, enginetype, hasSideCar):
        super().__init__("Bike")
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


def main():
    print("classes")


if __name__ == "__main__":
    main()
