class Vehicle:
    color = ""
    def __init__(self,name,passengers):
        self.name = name
        self.passengers = passengers
    def move(self):
        print("The vehicle", self.name, "is moving")
        print("It has", self.passengers, "passengers")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass 

class Toilet:
    def move(self):
        print("The vehicle toilet is moving")
        print("It has 1 passenger. You.")

car = Car("car",5)
boat = Boat("boat",10)
plane = Vehicle("plane", 20)
toilet = Toilet()

vehicles = [car,boat,plane,toilet]
for v in vehicles:
    v.move()
