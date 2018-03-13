
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
    
class LinkedList:
    def __init__(self, lst=[0, 1, 2, 3, 4, 5]):
        self.head = Node(0) # 头结点数据部分存储链表长度
        for k in lst:      # 初始化数据
            self.insert(k, 0)
        
    def insert(self, x, i):
        """在第i个位置添加元素x"""
        if self.empty():
            node = Node(x)
            node.next = self.head.next
            self.head.next = node 
        else:
            if i < 0 or i > self.head.data - 1:
                raise Exception("插入位置超出链表范围...")
            else:
                p = self.head
                for _ in range(i):  # 找到第i-1个位置
                    p = p.next
                node = Node(x)
                node.next = p.next
                p.next = node
        self.head.data += 1
    def empty(self):
        return self.head.data == 0
    
    def delete_by_pos(self, i):
        """删除第i个位置的数据"""
        if self.empty() or (i < 0 or i > self.head.data-1):
            raise Exception("删除超出索引范围...")
        else:
            p = self.head
            for _ in range(i):  # 找到第i-1个位置
                p = p.next
            tmp = p.next.data
            p.next = p.next.next
        return tmp
    
    def display(self):
        tmp = []
        p = self.head.next
        while not p is None:
            tmp.append(p.data)
            p = p.next
        print(tmp)
lst = LinkedList()  # 初始链表
lst.display()

lst.insert(999, 3)    # 第3个位置插入999(起始位置为0)
lst.display()

print(lst.delete_by_pos(4)) # 删除第四个位置元素
lst.display()
