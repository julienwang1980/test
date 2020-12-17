
teeth = 100
class Dog(object):
    __tooth = 10
    def __init__(self):
        self.th = 1000

    @staticmethod
    def info_print():
        global teeth
        print('这是一个狗类，用于创建狗实例...')
        return teeth


wangcai = Dog()
wangcai.info_print()
Dog.info_print()
print(wangcai.info_print())
print(wangcai.info_print())