# 类装饰器：使用类装饰已有幻术

class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call__这个方法，让对象变成可调用的对象，可调用的对象能够像函数使用
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print("课已讲完")
        self.__func()


@MyDecorator    # @MyDecorator => show = MyDecorator(show)
def show():
    print("快要下课啦")

# 执行show    # 执行My Decorator类创建实例对象 -> show() => 对象（）
show()

# 扩展：函数之所以能够调用是因为函数内部使用__call__

def mytest():
    print("哈哈")

print(dir(mytest))