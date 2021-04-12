# 学习装饰器的目的：对已有函数进行额外的功能扩展,装饰器本质上一个闭包函数,也就是说他也是一个函数嵌套

# 装饰器的特点：
# 1.不修改已有函数的源代码
# 2.不修改已有函数的调用方式
# 3.给以后函数添加额外的功能

# 定义装饰器
def decorator(func):    # 如果闭包函数的参数有且只有一个是函数类型,那么这个闭包函数称为装饰器
    def inner():
        # 在内部函数里面对已有函数进行装饰
        print("已添加登录验证")
        func()
    return inner

# 装饰器的语法糖写法:@装饰器,装饰器的语法糖就是在装饰以后函数的时候写法更加简单
@decorator # comment = decorator(comment),装饰器语法糖对该代码进行了封装,comment=inner
def comment():
    print("发表评论")


# 已添加登录验证
# 发表评论

# # 调用装饰器对已有函数进行装饰
# comment = decorator(comment)

# 调用方式不变
comment()
