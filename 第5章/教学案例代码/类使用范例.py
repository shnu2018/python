class Person:
    def __init__(self, name, age=100):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)
p = Person("john")
p.show()
p = Person("john", 999)
p.show()
print(p.name, p.age)