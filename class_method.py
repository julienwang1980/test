class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    def get(self):
        return self.__tooth


wangcai = Dog()
result1 = wangcai.get_tooth()
result2 = Dog.get_tooth()
result3 = wangcai.get()

print(result1)
print(result2)
print(result3)