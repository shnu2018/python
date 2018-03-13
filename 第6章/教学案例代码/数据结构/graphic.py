
class Vertex:  # 顶点
    def __init__(self, index):
        self.index = index     # 顶点标识
        self.first_edge = None # 连接的第一条边
class Edge:
    def __init__(self, index, weight):
        self.weight = weight       # 边的的权重
        self.end_index = index  # 终端顶点的索引
        self.next_edge = None   # 下一条边
class AdjTable:
    def __init__(self, adjMat):
        """由邻接矩阵创建邻接表"""
        self.adjMat = adjMat
        self.n = len(adjMat)    # 方阵维度
        self.vertexs = [Vertex(i) for i in range(self.n)]  # 初始化顶点
        self.visit_flag = [False] * self.n             # 顶点是否被访问过的标记
        self.create_table(adjMat)
        self.depth_visit = []                          # 深度遍历的结果
        self.breadth_visit = []                        # 广度遍历的结果
    
    def create_table(self, mat):
        for i in range(self.n):
            for j in range(self.n):
                if mat[i][j] is not None:  # 存在边
                    self.insert_edge(self.vertexs[i], Edge(j, mat[i][j]))

    def insert_edge(self, vertex, edge):
        """顶点后面添加一条边"""
        edge.next_edge = vertex.first_edge
        vertex.first_edge = edge
    
    def _depth_first(self, ver):
        """
        深度优先遍历, 先尝试从一个顶点出发。
        可能出现遍历不完整。
        """
        if self.visit_flag[ver.index]:
            return 
        self.depth_visit.append(ver.index)   # 访问
        self.visit_flag[ver.index] = True   # 标记访问过了
        p = ver.first_edge
        while p is not None:
            if not self.visit_flag[p.end_index]:
                self._depth_first(self.vertexs[p.end_index])
            p = p.next_edge
            
    def depth_first(self, start=0):
        """检查所有顶点是否都完成遍历"""
        self.visit_flag = [False] * self.n     # 初始化标记
        for i in range(start, start + self.n):
            i = i % self.n                     # 取余构成索引回环
            self._depth_first(self.vertexs[i])
            # 如果发现所有顶点都遍历完成了，则跳出
            if set(self.visit_flag) == {True}:
                break
        return self.depth_visit
        
    def _breadth_first(self, ver):
        """
        从某一个节点开始广度优先遍历
        可能出现遍历不完整
        """
        queue = [ver]       # 起始节点入队
        while len(queue) != 0:
            visited_vertex = queue.pop(0)
            self.breadth_visit.append(visited_vertex.index)   # 访问
            self.visit_flag[visited_vertex.index] = True      # 标记
            p = visited_vertex.first_edge
            while p is not None:                       # 相关的都添加进去
                # 如果顶点已经被标记或者已经被放入了队列中，则不加入队列
                if (not self.visit_flag[p.end_index]) and (queue.count(self.vertexs[p.end_index]) == 0):
                    queue.append(self.vertexs[p.end_index])
                p = p.next_edge
        
    def breadth_first(self, start=0):
        """检查所有顶点，保证完全遍历"""
        self.visit_flag = [False] * self.n     # 初始化标记
        for i in range(start, start + self.n):
            i = i % self.n
            self._breadth_first(self.vertexs[i])
            if set(self.visit_flag) == {True}:
                break
        return self.breadth_visit
    
    def display(self):
        for i in range(self.n):
            s = ""
            v = self.vertexs[i]
            s += str(v.index) + " -> "
            p = v.first_edge
            while p is not None:
                s += str(p.end_index) + ","
                p = p.next_edge
            print(s)
            
mat = [[None, None, None, 1],
       [1, None, 1, None],
       [1, 1, None, None],
       [None, None, None, None]]
adj = AdjTable(mat)
adj.display()
depth = adj.depth_first(2)         # 从顶点2开始深度遍历
breadth = adj.breadth_first(1)     # 从顶点1开始广度遍历
print("深度遍历结果：%s" % depth)
print("广度遍历结果：%s" % breadth)
