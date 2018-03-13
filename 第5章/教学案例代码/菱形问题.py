class Base:
    def method(self):
        print("base...")
    
class A(Base):
    def method(self):
        print("A...")
class B(Base):
    def method(self):
        print("B...")
class C(A, B):
    def show(self):
        self.method()
c = C()
c.show()