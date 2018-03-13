from threading import Thread
import threading
import time
class SellTicket(Thread):
    """卖票问题。
        总共有n张火车票。
        有多个窗口同时进行售票。
        同步问题：要保证每个窗口的票数信息都是同步的。
    """
    lock = threading.Lock()
    ticket_nums = 100    # 票总数
    def __init__(self, win_name):
        super().__init__()
        self.win_name = win_name

    #
    # def run(self):
    #     """每隔0.1秒售出一张票，直到票售完为止"""
    #     while True:
    #         if SellTicket.ticket_nums <= 0:
    #             break
    #         print("剩余票数：%d...%s开始售票..." % (SellTicket.ticket_nums, self.win_name))
    #         SellTicket.ticket_nums -= 1
    #         print("剩余票数：%d...%s售票结束..." % (SellTicket.ticket_nums, self.win_name))
    #
    #         time.sleep(0.1)  # 售票延时0.1秒

    def run(self):
        """每隔0.1秒售出一张票，直到票售完为止"""
        while True:
            SellTicket.lock.acquire()   # 请求锁。当前线程获得锁之后，在释放之前，其余任何线程都不能进入锁住的代码块。

            if SellTicket.ticket_nums <= 0:   # 必须等到判断有票可以卖，然后把票卖出去了。这个售票过程中，不能有任何线程干扰。
                break
            print("剩余票数：%d...%s开始售票..." % (SellTicket.ticket_nums, self.win_name))
            SellTicket.ticket_nums -= 1
            print("剩余票数：%d...%s售票结束..." % (SellTicket.ticket_nums, self.win_name))

            SellTicket.lock.release()  # 释放锁

            time.sleep(0.1)  # 售票延时0.1秒

        SellTicket.lock.release()   # 对于break出来的锁，进行释放

win1 = SellTicket("窗口1")
win2 = SellTicket("窗口2")
win3 = SellTicket("窗口3")
win1.start()
win2.start()
win3.start()

win1.join(),win2.join(),win3.join()
# 等三个子线程处理完成了，主线程检查最终剩余票数(理论上是0张)
print("%s-- 剩余票数：%d" % (threading.current_thread().getName(), SellTicket.ticket_nums))

"""
卖票的过程基本可以分为以下三步：
    1. 检查到有票
    2. 售出一张票
    3. 更新系统票数总数

如果没有增加同步措施。
假如窗口A和窗口B几乎同时看到系统中还剩下一张票了，于是两个窗口都满足步骤一，于是都会执行步骤二。
最终导致的结果是：一张票，但是被两个窗口都减去了一，于是最终会发现库存是一个负数。

如果增加了同步措施。可以这样解决：当窗口A发现有票的时候，立即禁止其余窗口执行步骤一。只有当窗口A执行完三个售票步骤，才解除禁止。
如此一来，每一个时段窗口都会完成一个完整的售票工作。
"""

