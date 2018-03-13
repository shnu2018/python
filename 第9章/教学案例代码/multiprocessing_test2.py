from multiprocessing import current_process
from multiprocessing import Process
import time
def write_info(lock):
    """向文件中写入信息"""
    lock.acquire()
    with open("test-multiprocess", "a") as f:
        for i in range(100):
            f.write("%s -- %s\n" % (current_process().name, time.ctime()))
    lock.release()
if __name__ == "__main__":
    from multiprocessing import Lock
    lock = Lock()
    p1 = Process(target=write_info, args=(lock, ))
    p2 = Process(target=write_info, args=(lock, ))
    p3 = Process(target=write_info, args=(lock, ))
    p1.start()
    p2.start()
    p3.start()
