class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, p):           # 加
        return self.age + p.age

    def __sub__(self, other):       # 减
        v = self.age - other.age
        return v if v > 0 else -v

    def __mul__(self, other):       # 乘
        return self.age * other.age

    def __floordiv__(self, other):    # 整除
        return self.age // other.age

    def __mod__(self, other):         # 取余
        return self.age % other.age

    def __gt__(self, other):          # 大于
        return self.name > other.name or self.age > other.age

    def __lt__(self, other):         # 小于
        return other.name > self.name or self.age < other.age

    def __eq__(self, other):          # 等于
        return self.name == other.name and self.age == other.age

    def __str__(self):               # toString
        return "name: {0}, age: {1}".format(self.name, self.age)

p1 = Person("zhang", 100)
p2 = Person("lisi", 2343)
print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 // p2)
print(p1 % p2)
print(p1 == p2)
print(p1 > p2)

ps = [p1, p2]
ps.sort()
print(ps[0])
print(ps[1])
