
class Stack:
    def __init__(self):
        self._data = []
    def push(self, x):
        self._data.append(x)
    def pop(self):
        return self._data.pop()
    def peek(self):
        return self._data[-1]
    def size(self):
        return len(self._data)
    def empty(self):
        return self.size() == 0
s = Stack()
s.push(3)
s.push(10)
s.push(100)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.size())
print(s.pop())
print(s.empty())

