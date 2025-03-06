# 装饰器

import time

def decorator(func):
    # 不确定func的参数，使用args, kwargs什么参数都能传进来
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} is running. It cost {end - start} seconds")
    return wrapper

# 简略写法
@decorator
def sleep_04():
    time.sleep(0.4)
sleep_04()

# 完整写法
def sleep_05():
    time.sleep(0.5)
sleep_05 = decorator(sleep_05)
sleep_05()

# 针对不同装饰器，定制装饰器
def make_decorator(threshold):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            if end - start > threshold:
                print(f"超时，时间上限是{threshold}seconds")
            else:
                print(f"时间在可接受范围内")
        return wrapper
    return decorator

@make_decorator(0.2)
def sleep_03():
    time.sleep(0.3)
sleep_03()