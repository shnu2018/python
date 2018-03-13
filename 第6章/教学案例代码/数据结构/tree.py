
class Node:
    def __init__(self, x):
        self.data = x
        self.lchild = None   
        self.rchild = None
class BiTree:
    def __init__(self, d=[1, 2, 3, 4, 5, 6]):
        self.root = None
        self.create_tree(d)
        self.preorder = []    # 存储先序遍历结果
        self.afterorder = []    # 存储后序遍历结果
        self.midorder = []     # 存储中序遍历结果
        
    def create_tree(self, d):
        """使用层序遍历的方式创建二叉树"""
        self.root = Node(d[0])
        q =  [self.root]           # 队列结构，第一个元素作为根节点，入队
        i = 0                      # 数据索引
        while len(q) != 0:
            parent = q.pop(0)
            left_index = 2 * i + 1         # 出队节点作为父节点，其左孩子数据位置
            right_index = left_index + 1  # 右孩子数据位置
            if left_index < len(d):
                left_child = Node(d[left_index])
                parent.lchild = left_child    # 构建父子关系
                q.append(left_child)         # 孩子节点入队
            if right_index < len(d):
                right_child = Node(d[right_index])
                parent.rchild = right_child
                q.append(right_child)
            i += 1
    
    def preOrder(self, root):
        """先序遍历"""
        if root is not None:
            self.preorder.append(root.data)
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)
        return self.preorder
    
    def afterOrder(self, root):
        """后序遍历"""
        if root is not None:
            self.afterOrder(root.lchild)
            self.afterOrder(root.rchild)
            self.afterorder.append(root.data)
        return self.afterorder
    
    def midOrder(self, root):
        """中序遍历"""
        if root is not None:
            self.midOrder(root.lchild)
            self.midorder.append(root.data)
            self.midOrder(root.rchild)
        return self.midorder
    
b = BiTree()
print("前序遍历：%s" % b.preOrder(b.root))
print("后序遍历：%s" % b.afterOrder(b.root))
print("中序遍历：%s" % b.midOrder(b.root))
            
