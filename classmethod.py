# 类变量 类方法 静态方法

class Student:
    # 类变量直接在init外定义
    student_num = 0

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Student.student_num += 1

    # 类方法要通过装饰器classmethod修饰
    # 类方法参数的第一个变量为类名，这里使用cls代替
    @classmethod
    def add_student_num(cls, add_num):
        Student.student_num += add_num

    @classmethod
    def from_string(cls, info):
        name, sex = info.split(" ")
        return cls(name, sex)
    
    # 静态方法通过装饰器staticmethod修饰
    @staticmethod
    def name_len(name):
        return len(name)

s1 = Student("llj", "male")
s2 = Student.from_string("mike male")
# 类变量类方法要通过类名调用
print(f"student_num:{Student.student_num}")
print(f"s2.name:{s2.name}, s2.name.length:{Student.name_len(s2.name)}")