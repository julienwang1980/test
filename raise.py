# 自定义一场类，继承Execption
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

        # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度是{self.length}，不能少于{self.min_len}个字符'

def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')

    try:
        print(1/0)
    except(NameError, ZeroDivisionError) as result:
        print(result)


if __name__ == '__main__':
    main()