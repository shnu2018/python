import multiprocessing
def hello(name, d_map):
    print(multiprocessing.current_process().name)
    print("hello %s, 进程唯一标识pid：%s" % (name, multiprocessing.current_process().pid))
    s = 0
    for i in range(100):
        s += i
    d_map["result"] = s               # 存入子进程数据

if __name__ == "__main__":
    m = multiprocessing.Manager()      # 状态代理对象
    d_map = m.dict()                    # 字典，
    p1 = multiprocessing.Process(target=hello, args=("tom", d_map), name="my-process-01")
    p1.start()
    p1.join()
    print(multiprocessing.current_process().name, d_map)

from multiprocessing import Queue

class MyProcess(multiprocessing.Process):
    s = 0
    def __init__(self):
        super().__init__()
    def run(self):
        print(self.pid, self.name)   # 打印进程pid，进程名称
        for i in range(100):
            MyProcess.s += i
        print(MyProcess.s)
# if __name__ == "__main__":
#     process1 = MyProcess()
#     process2 = MyProcess()
#     process1.start(), process2.start()
#     process1.join(), process2.join()
#     print(multiprocessing.current_process().name, MyProcess.s)