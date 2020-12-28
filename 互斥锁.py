import threading

# 定义全局变量
g_num = 0

# 创建全局互斥锁
lock = threading.Lock()

# 循环一次给全局变量加1
def sum_num1():
    # 上锁
    lock.acquire()
    for i in range(2000000):
        global  g_num
        g_num += 1

    print('sum1:', g_num)
    # 释放锁
    lock.release()


# 循环一次给全局变量加1
def sum_num2():
    # 上锁
    lock.acquire()
    for i in range(2000000):
        global g_num
        g_num += 1

    print('sum2:', g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)
    # 启动线程
    first_thread.start()
    second_thread.start()

    # 提示：加上互斥锁，哪个线程抢到这个锁我们决定不了，哪个线程抢到锁那个哪个线程先执行，没抢到的线程需要等待
    # 加上互斥锁多任务瞬间变成单任务，性能会下降，也就是说同一时刻只能有一个线程去执行