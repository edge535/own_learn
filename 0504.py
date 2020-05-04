# import threading
#
# import time
#
# def loop():
#     '''新的线程执行的代码'''
#     # 当前正在执行的线程名称
#     now_thread = threading.current_thread()
#     print('loop now thread name: {}'.format(now_thread.name))
#     n = 0
#     while n < 5:
#         print(n)
#         time.sleep(1)
#         n += 1
#
# def use_thread():
#     '''使用线程来实现'''
#     # 当前正在执行的线程名称
#     now_thread = threading.current_thread()
#     print('now thread name: {}'.format(now_thread.name))
#     # 设置线程
#     t = threading.Thread(target=loop, name='loop_thread')
#     # 启动线程
#     t.start()
#     # 挂起线程
#     t.join()
#
# if __name__ == '__main__':
#     use_thread()









# import threading, time
#
#
# class loopthread(threading.Thread):
#     """自定义线程"""
#     n = 0
#     def run(self):
#         while self.n < 5:
#             print(self.n)
#             now_thread = threading.current_thread()
#             print('loop now thread name: {}'.format(now_thread.name))
#             time.sleep(1)
#             self.n += 1
#
# if __name__ == '__main__':
#     loopthread(name='loop_thread_oop').start()









# import threading, time
#
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     time.sleep(1)
#     balance = balance - n
#     time.sleep(2)
#     print('{}<--------->{}'.format(n, balance))
#
# class changeBalanceThread(threading.Thread):
#     """改变银行余额的线程"""
#     def __init__(self, num, *args, ** kwargs):
#         super().__init__(*args, **kwargs)
#         self.num = num
#
#     def run(self):
#         for i in range(10000):
#             change_it(self.num)
#
# if __name__ == '__main__':
#     t1 = changeBalanceThread(5)
#     t2 = changeBalanceThread(8)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('The last: {}'.format(balance))









# import threading, time
#
# # 获得一把锁
# my_lock = threading.Lock()  # 只能锁一次
# your_lock = threading.RLock()  # 可以锁多次
#
# balance = 0
# def change_it(n):
#     global balance
#     #with your_lock:
#     try:
#         # 添加锁
#         my_lock.acquire()
#         balance = balance + n
#         time.sleep(1)
#         balance = balance - n
#         time.sleep(2)
#         print('{}<--------->{}'.format(n, balance))
#     finally:
#         # 释放锁
#         my_lock.release()
#
# class changeBalanceThread(threading.Thread):
#     """改变银行余额的线程"""
#     def __init__(self, num, *args, ** kwargs):
#         super().__init__(*args, **kwargs)
#         self.num = num
#
#     def run(self):
#         for i in range(10000):
#             change_it(self.num)
# if __name__ == '__main__':
#     t1 = changeBalanceThread(5)
#     t2 = changeBalanceThread(8)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('The last: {}'.format(balance))









# import threading, time
#
# def run(n):
#     """"线程要做的事"""
#     time.sleep(1)
#     print(threading.current_thread().name, n)
# def main():
#     """使用传统方式做任务"""
#     t1 = time.time()
#     for n in range(100):
#         run(n)
#     print(time.time() - t1)
# def main_use_thread():
#     """使用线程优化"""
#     t1 = time.time()
#     ls = []
#     for count in range(10):
#         for i in range(10):  # 最多跑10个线程
#             t = threading.Thread(target=run, args=(i,))
#             ls.append(t)
#             t.start()
#         for l in ls:
#             l.join()
#     print(time.time() - t1)
# def main_use_pool():
#     """使用线程池"""
#     t1 = time.time()
#     n_list = range(100)
#     pool = pool(10)
#     pool.map(run, n_list)
#     pool.close()
#     pool.join()
#     print(time.time() - t1)
# if __name__ == '__main__':
#     # main()
#     # main_use_thread()
#     main_use_pool()









# import time, os
# from multiprocessing import Process
# def do_sth(name):
#     """进程要做的事情"""
#     print('进程的名称{}'.format(name))
#     time.sleep(2)
#     print("进程要做的事情")
# class myprocess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print('MyProcess进程的名称{}'.format(self.name))
#         time.sleep(2)
#         print("MyProcess进程要做的事情")
# if __name__ == '__main__':
#     # p = Process(target=do_sth, args=('my process', ))
#     # p.start()
#     # p.join()
#     p = myprocess('my process class')
#     p.start()
#     p.join()










# from multiprocessing import Process, Queue
# import random, time
# class writeProcess(Process):
#     """写的进程"""
#     def __init__(self, q, *args, **kwargs):
#         self.q = q
#         super().__init__(*args, **kwargs)
#     def run(self):
#         ls = [
#             '第1行内容',
#             '第2行内容',
#             '第3行内容',
#             '第4行内容'
#         ]
#         for line in ls:
#             self.q.put(line)
#             # 每写入一次，休息1-5秒
#             time.sleep(random.randint(1, 5))
# class readProcess(Process):
#     """读的进程"""
#     def __init__(self, q, *args, **kwargs):
#         self.q = q
#         super().__init__(*args, **kwargs)
#     def run(self):
#         while True:
#             content = self.q.get()
#             print('读取到的内容: {}'.format(content))
# if __name__ == '__main__':
#     # 通过queue共享数据
#     q = Queue()
#     # 写入内容的进程
#     t_write = writeProcess(q)
#     t_write.start()
#     # 读取进程
#     t_read = readProcess(q)
#     t_read.start()
#     t_write.join()
#     t_read.join()
#     # 因为读取的进程是死循环，需要强制结束
#     t_read.terminate()









# from multiprocessing import Process, Lock
# import random, time
# class writeprocess(Process):
#     """写入文件"""
#     def __init__(self, file_name, num, lock,  *args, **kwargs):
#         self.file_name = file_name
#         self.num = num
#         self.lock = lock
#         super().__init__()
#     def run(self):
#         for i in range(5):
#             content = '现在是{} : {} : {} \n'.format(self.name, self.pid, self.num)
#             try:
#                 self.lock.acquire()
#                 with open(self.file_name, 'a+', encoding='utf-8') as f:
#                     f.write(content)
#                     print(content)
#                     time.sleep(random.randint(1, 3))
#             finally:
#                 self.lock.release()
# if __name__ == '__main__':
#     file_name = '504.txt'
#     # 锁的对象
#     lock = Lock()
#     for x in range(5):
#         p = writeprocess(file_name, x, lock)
#         p.start()










# from multiprocessing import current_process, Pool
# import time, random
# def run(file_name, num):
#     """
#     进程执行的业务逻辑
#     :param file_name: str 文件的名称
#     :param num: 写入的数字
#     :return: str 写入的结果
#     """
#     with open(file_name, 'a+', encoding='utf-8') as f:
#         # 当前的进程
#         now_process = current_process()
#         # 写入的内容
#         content = '{} : {} : {}'.format(now_process.name, now_process.pid, num)
#         f.write(content)
#         f.write('\n')
#         time.sleep(random.randint(1, 2))
#         print(content)
#     return 'OK'
# if __name__ == '__main__':
#     file_name = 'process_pool.txt'
#     # 进程池
#     pool = Pool(2)
#     for i in range(20):
#         # 同步任务
#         # rest = pool.apply(run, args=(file_name, i))
#         # 异步任务
#         rest = pool.apply_async(run, args=(file_name, i))
#         print('{}----{}'.format(i, rest.get()))
#     # 关闭池
#     pool.close()
#     pool.join()








# # python3.5之前使用
# def yield_test():
#     while True:
#         n = (yield )
#         print(n)
# if __name__ == '__main__':
#     rest = yield_test()
#     next(rest)
#     rest.send('666')
#     rest.send('666')
#
# import asyncio
# async def do_sth(x):  # 当被调用时，不执行代码，而返回一个协程对象。在事件循环中调度其执行前，携程对象不执行
#     """定义协程函数"""
#     print('等待中{}'.format(x))
#     await asyncio.sleep(x)  # 1.等待协程执行完成 2.阻塞调用的函数时，将协程的控制权让出，以便调用其他协程
# print(asyncio.iscoroutinefunction(do_sth))  # 判断是否是协程函数
#
# coroutine = do_sth(5)
# # 事件的循环队列
# loop = asyncio.get_event_loop()
# # 注册任务，将函数添加到携程队列
# task = loop.create_task(coroutine)
# print(task)
# # 等待协程任务执行结束
# loop.run_until_complete(task)
# print(task)










# import asyncio
# async def compute(x, y):
#     print('计算x+y=>{}+{}'.format(x, y))
#     await asyncio.sleep(1)
#     return x + y
# async def get_sum(x, y):
#     rest = await compute(x, y)  # 嵌套调用，需要等待compute完成
#     print('{}+{}={}'.format(x, y, rest))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_sum(1, 2))
# loop.close()










import asyncio, random
    #1.定义一个队列
    #2.两个协程进行通信
    #3.一个协程写入数据
    #4.一个协程读取数据
async def add(store, name):
    for i in range(5):
        num = '{}---{}'.format(name, i)
        await asyncio.sleep(random.randint(1, 3))
        await store.put(num)
        print('add:{} --- size:{} --- name:{}'.format(i, store.qsize(), name))

async def reduce(store):
    for i in range(10):
        rest = await store.get()
        print('reduce:{} --- size:{}'.format(rest, store.qsize()))
if __name__ == '__main__':
    store = asyncio.Queue(maxsize=5)
    a1 = add(store, 'a1')
    a2 = add(store, 'a2')
    r1 = reduce(store)
    # 添加到事件队列
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(a1, a2, r1))
    loop.close()