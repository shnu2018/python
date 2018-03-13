class Animal:
    def __init__(self, name):
        self.name = name 
    def run(self):
        print("%s is running..." % self.name)
class Cat(Animal): pass
class Dog(Animal): pass

class House:
    def animalDo(self, animal):
        animal.run()
    
cat = Cat("cat")
dog = Dog('dog')
h = House()

h.animalDo(cat)
h.animalDo(dog)
