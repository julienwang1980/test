def make_div(func):
    print("make_div装饰器执行了")
    def inner():
        # 在内部函数对已有函数进行装饰
        result = "<div>" + func() + "</div>"
        return result

    return inner


# 定义装饰器
def make_p(func):
    print("make_p装饰器执行了")
    def inner():
        # 在内部函数对已有函数进行装饰
        result = "<p>" + func() + "</p>"
        return result

    return inner

# 多个装饰器的过程：由内到外的装饰过程，先执行内部的装饰器
# 原理剖析：content = make_div(make_p(content))
# 分步拆解：content = make_p(content),内部装饰器装饰完成content = make_p.inner
#         content = make_div(make_p.inner)
@make_div
@make_p
def content():
    return "人生苦短，我用python！"

# <p>人生苦短，我用python！</p>
result = content()
print(result)