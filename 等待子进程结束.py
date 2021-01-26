import multiprocessing
import time

# 定义进程所需要执行的任务
def task(number, count):
    for i in range(count):
        print(number, '任务执行中...')
        time.sleep(0.2)
    else:
        print('任务执行完成')



if __name__ == '__main__':
    # 创建子进程
    sub_process = multiprocessing.Process(target=task, args=(5,), kwargs={'count': 10})
    # 设置守护主进程，主进程退出子进程直接销毁，子进程的生命周期依赖与主进程
    # sub_process.daemon = True
    sub_process.start()

    # 主进程延时0.5秒钟
    time.sleep(1)
    print('over')
    # 让子进程销毁
    sub_process.terminate()
    exit()

