# python生成器，处理超大数据,节省空间

list = [1, 2, 3, 4 ,5]

# 原方法
def square_list(list):
    new_list = []
    for i in list:
        new_list.append(i * i)
    return new_list

new_list = square_list(list)
print(new_list)

# 采用生成器(yield)
def square_lsit2(list):
    for i in list:
        yield i * i

new_list = square_lsit2(list)
print(new_list)

# 两种遍历方式 next 和 for
print("The first number(using next):")
print(next(new_list))
print("The following number(using for):")
for i in new_list:
    print(i)

# 生成器的简略写法
my_list = [i*i for i in list]
print(my_list)

my_gen = (i*i for i in list)
print(my_gen)