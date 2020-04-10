#
# class cat:
#     """猫科动物类"""
#     tag = "我是家猫"
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def set_age(self, age):
#         """
#         更改猫的年龄
#         :param age: int 年龄
#         :return: 更改后的年龄
#         """
#         self.__age = age
#
#     def show_info(self):#显示猫的信息
#         print('我叫{}，今年岁{}'.format(self.name, self.__age))
#
#     def eat(self):
#         """吃"""
#         print("猫喜欢吃鱼")
#
#     def catch(self):
#         print("猫可以捉老鼠")
#
# class tiger:
#     pass



# class basecat(object):
#     """猫科动物的积累"""
#
#     tag = '猫科动物'
#
#     def __init__(self, name):
#         self.name = name  #猫都有名称
#
#     def eat(self):
#         """猫都吃东西"""
#         print("猫都吃东西")
#
#
# class protectmixin(object):
#     """受保护的类"""
#     def protect(self):
#         print("我是受省级保护的")
#
#
# class countryprotectmixin(object):
#     """受保护的类"""
#     def protect(self):
#         print("我是受国家保护的")
#
#
# class tiger(basecat, protectmixin, countryprotectmixin):
#     """老虎类，也是猫科动物"""
#
#     def eat(self):
#         super().eat()
#         print('我还喜欢吃肉')
#
#
# class panda(basecat, protectmixin):
#     """熊猫类，也是猫科动物"""
#     pass
#
#
# class petcat(basecat):
#     """家猫类"""
#
#     def eat(self):
#         super(petcat, self).eat()  # 调用父类
#         print('我还喜欢吃猫粮')
#
#
# class huacat(petcat):
#     """中华田园猫"""
#
#     def eat(self):
#         super(huacat, self).eat()  # 调用父类
#         print('我还喜欢吃零食')
#
#
# class duancat(petcat):
#     """短毛猫"""
#     # def eat(self):
#     #     super(duancat, self).eat()
#     #     #print('我啥都吃')





class basecat(object):
    """猫科动物的积累"""

    tag = '猫科动物'

    def __init__(self, name):
        self.name = name  #猫都有名称
        print("base init")

    def eat(self):
        """猫都吃东西"""
        print("猫都吃东西")


class tiger(basecat):
    """老虎类，也是猫科动物"""

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print("tiger init")

    def eat(self):
        super().eat()
        print('我还喜欢吃肉')

    def show_info(self):
        """展示信息"""
        print("名字叫{}， 颜色{}。".format(self.name, self.color))



if __name__ == "__main__":
    #pass
    # cat_black = cat("小黑", 2)
    # cat_black.eat()
    # cat_black.show_info()
    # cat_black.name = '小白'
    # cat_black.show_info()
    # cat_black.set_age(3)
    # cat_black.show_info()
    # cat.set_age(cat_black, 9)
    # cat_black.show_info()
    # print(cat.tag)
    # print(cat_black.tag)
    #
    # #类的实例判断
    # print(isinstance(cat_black, cat))
    # print(isinstance(cat_black, tiger))

    #实例化中华田园猫
    # cat = huacat("小黄")
    # cat.eat()
    # print('------')
    # cat_d = duancat('小灰')
    # cat_d.eat()
    # print('------')
    # print(issubclass(duancat, petcat))
    # print(issubclass(duancat, basecat))

    # panda = panda("熊猫")
    # panda.eat()
    # panda.protect()
    # print("-------")
    # tiger = tiger("华南虎")
    # tiger.eat()
    # tiger.protect()

    ti = tiger('华南虎', '黄色')
    ti.show_info()


