class Car:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
    def show(self):
        pass
class ElectricCar(Car):
    def __init__(self, name, miles):
        super().__init__(name)
        self.miles = miles
    def show(self):
        self.display()
        print(self.name, self.miles)
c = ElectricCar("tesla", 2000)
c.display()
print("-"*10)
c.show()