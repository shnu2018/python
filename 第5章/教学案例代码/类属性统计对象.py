class Dog():
    count = 0   # 类属性
    def __init__(self, name):
        Dog.count += 1
        self.name = name
    def roll(self):
        print("dog name is %s, %d years old." % (self.name, self.age))
    def counter():  # 静态方法
        print(Dog.count)
        
Dog("tom")
Dog("")
Dog("")
Dog.counter()