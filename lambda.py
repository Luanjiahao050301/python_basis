# lambda 表达式

def add1(a:int, b:int):
    return a + b
print(add1(3, 4))

add2 = lambda a, b : a + b
print(add2(3, 4))

# lambda函数作为其他函数的参数

my_list = [1, 2, 3, 4, 5]
# map函数对迭代器的每一个元素应用前面的函数，并返回一个迭代器
new_list = list(map(lambda a : a**2, my_list))
print(new_list)