from threading import Thread
import time
import time

class InnerDaemon(Thread):
    def run(self):
        print("%s run inner thread..." % self.getName())
        time.sleep(10)
        print("%s end..." % self.getName())

class MyDaemon(Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        print("%s is starting..." % self.getName())
        innerThread = InnerDaemon()
        innerThread.setDaemon(True)
        innerThread.start()
        innerThread.join(1)
        print("%s end..." % self.getName())

mt1 = MyDaemon()
mt1.setName("mythread-01")

mt1.start()

print("主线程死亡....")   # 执行完这一行，主线程结束

"""
        print(self.getName())   # 获取线程名称， 注意self.name是父类中的属性。
        self.setName("thread-01")  # 设置线程名称

        print(self.is_alive())   # 判断线程是否还是运行状态
        print(self.isDaemon())   # 是否是守护线程
        self.setDaemon(False)   # 设置是否是守护线程

        self.join(5)     # 设置优先执行
"""
