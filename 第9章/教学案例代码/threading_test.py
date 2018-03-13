from threading import Thread
import time

class MyThread(Thread):
    """多线程计算一段数据求和"""
    total = 0   # 类属性，公共求和变量。所有线程共享。
    def __init__(self, begin_index, end_index):
        super().__init__()
        self.begin_index = begin_index
        self.end_index = end_index
    def show_isAlive(self):
        if mt1.is_alive():
            print("show_isAlive()->线程%s依然存活..." % self.getName())
        else:
            print("show_isAlive()->线程%s死亡..." % self.getName())
    def run(self):
        s = 0
        for i in range(self.begin_index, self.end_index+1):
            if i % 13 == 0:
                print(self.getName())   # 打印当前线程名称
            s += i
            time.sleep(0.01)   # 为了体现交替效果
        MyThread.total += s
        print("线程%s死亡..." % self.getName())
mt1 = MyThread(1, 100)
mt1.setName("mythread-01")
mt2 = MyThread(101, 200)
mt3 = MyThread(201, 300)
mt1.start()
mt2.start()
mt3.start()
mt1.join(), mt2.join(), mt3.join()
mt1.show_isAlive()
print(MyThread.total)    # 1 ~ 300 求和
print("主线程死亡....")   # 执行完这一行，主线程结束

"""
        print(self.getName())   # 获取线程名称， 注意self.name是父类中的属性。
        self.setName("thread-01")  # 设置线程名称

        print(self.is_alive())   # 判断线程是否还是运行状态
        print(self.isDaemon())   # 是否是守护线程
        self.setDaemon(False)   # 设置是否是守护线程

        self.join(5)     # 设置优先执行
"""
