'''
    lambda作为一个表达式
    定义了一个【匿名函数】
    x为入口参数，x+1为函数体

'''
g = lambda x:x+1
print(g(1))
print(g(2))
print(g(3))

# 等价函数来表示为：
def g(x):
    return x+1

# 上面简要介绍了什么是lambda,下面介绍为什么使用lambda???

# 例子
# processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

'''
    问题：
    在Visual Basic，你很有可能要创建一个函数，接受一个字符串参数和一个 collapse 参数，
    并使用 if语句确定是否压缩空白，然后再返回相应的值。
    这种方式是低效的，因为函数可能需要处理每一种可能的情况。
    每次你调用它，它将不得不在给出你所想要的东西之前，判断是否要压缩空白。

    解决方案：
    在 Python 中，你可以将决策逻辑拿到函数外面，而定义一个裁减过的 lambda函数提供确切的 (唯一的) 你想要的。
    这种方式更为高效、更为优雅，而且很少引起那些令人讨厌 (哦，想到那些参数就头昏) 的错误。

    通过此例子，我们发现，lambda的使用大量简化了代码，使代码简练清晰。
    但是值得注意的是，这会在一定程度上降低代码的可读性。
    如果不是非常熟悉python的人或许会对此感到不可理解。

    lambda 定义了一个匿名函数
    lambda 并不会带来程序运行效率的提高，只会使代码更简洁。
    如果可以使用for...in...if来完成的，坚决不用lambda。
    如果使用lambda，lambda内不要包含循环，如果有，我宁愿定义函数来完成，使代码获得可重用性和更好的可读性。

    总结：lambda 是为了减少单行函数的定义而存在的。
'''