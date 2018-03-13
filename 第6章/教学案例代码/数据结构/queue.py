
class Queue:
    def __init__(self):
        self._data = []
    def enqueue(self, x):  
        """进队"""
        self._data.append(x)
    def dequeue(self):
        """出队"""
        return self._data.pop(0)
    def peek(self):
        """取对头数据，不删除"""
        return self._data[0]
    def size(self):
        """队列大小"""
        return len(self._data)
    def empty(self):
        return self.size() == 0
q =  Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.peek())
print(q.dequeue())
print(q.size())
print(q.empty())
print(q.dequeue())
print(q.dequeue())
print(q.empty())