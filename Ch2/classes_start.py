#
# Example file for working with classes
#

class Vehicles():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle;
    wheels = 4;
    engine = 1;

class Car(Vehicles):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheel = 4
        self.doors = 4
        self.cylinder = 4
        self.enginetype = enginetype



def main():
    print("classes")


if __name__ == "__main__":
    main()
