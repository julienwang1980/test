import time
try:
    f = open('test.txt')
    
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果咋读取文件的过程中，产生了异常，那么就会捕获到
        # 如果 按下了 ctrl+c
        print('意外终止了读取数据')

except:
    print('没有这个文件')