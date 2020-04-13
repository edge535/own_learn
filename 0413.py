#
# class cat(object):
#     """pet cat"""
#     def __init__(self, name, age):
#         self.name = name
#         # 私有属性，不能操作
#         self.__age = age
#
#     # 描述符
#     @property
#     def show_info(self):
#         return '我叫{}，今年{}岁。'.format(self.name, self.__age)
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int):
#             print("年龄只能是整数")
#             return 0
#         if 0 > value or value > 100:
#             print('年龄只能在0-100之间')
#             return 0
#         self.__age = value
#
#     def __str__(self):  # 则可以直接打印实例 -18row
#         return self.show_info
#



# class cat(object):
#     """pet cat"""
#
#     # __slots__ 限制属性
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 描述符
#     @property
#     def show_info(self):
#         return '我叫{}，今年{}岁。'.format(self.name, self.age)
#
#     def __str__(self):  # 则可以直接打印实例 -18row
#         return self.show_info
#
#
# class huacat(cat):
#     pass
#
#
# def eat():
#     print('我喜欢吃鱼')



class cat(object):

    tag = '猫科动物'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """呼吸"""
        print('猫都会呼吸')

    def show_info(self):
        print('类的属性：{}，实例的属性：{}.'.format(self.tag, self.name))

    @classmethod
    def show(cls):
        print('类的属性:{}'.format(cls.tag))

if __name__ == '__main__':
#     cat_black = cat('小黑', 2)
#     rest = cat_black.show_info
#     print(rest)
#     #print(cat_black)
#     print("------")
#     print(cat_black.name)
#     print(cat_black.age)
#     print('---------0')
#     cat_black.age = 9
#     print(cat.age)
#     cat_black = cat('小黑', 2)
#     print(cat_black)
#
    # # 给实例添加新的属性
    # cat_black.color = '白色'
    # print(cat_black.color)
    # 给实例添加新的方法
    # cat_black.eat = eat
    # cat_black.eat()
    # cat_ju = huacat('小菊', 3)
    # cat_ju.color = '橘色'
    # print(cat_ju.color)
#
    cat.breath()
    cat_black = cat('小黑')
    cat_black.breath()
    cat_black.show_info()
    cat.show()



"""
演示用代码
class cat(object):
    def __init__(self, name, age):
        self.name = name
        # 私有属性，不能操作
        self.__age = age

    # 将方法变成属性，直接调用
    @property
    def show_info(self):
        print('我叫{}，年龄是{}岁。'.format(self.name, self.__age))

    # 提供在外部通过使用非私有属性的方法获得属性值
    @property
    def age(self):
        print(self.__age)

    # 提供在外部通过使用非私有属性的方法设置属性值
    @age.setter
    def age(self, value):
        # 通过这种方式，也可以在设置值时对值进行判断
        if not isinstance(value, int):
           print("年龄只能是整数")
           return 0
        if 0 > value or value > 100:
            print('年龄只能在0-100之间')
            return 0
        self.__age = value



if __name__ == '__main__':
    cat_black = cat('小黑', 2)
    cat_black.show_info
    print(cat_black.name)
    cat_black.age = 9
    cat_black.age
"""
