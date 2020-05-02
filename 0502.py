# class Cat(object):
#     def __init__(self):
#         print('对象产生了:{0}'.format(id(self)))
#
#     def __del__(self):
#         print('对象删除了:{}'.format(id(self)))
#
#
# def f0():
#     while True:
#         c1 = Cat()
#
# f0()








# import sys
#
# l = []  # 一次
# l2 = l  # 一次
# l3 = l  # 一次
# l5 = l3  # 一次
# del l2  # 减一次
# # 对象l被引用的次数
# print(sys.getrefcount(l))  # 一次












import gc
# 每10次0代垃圾回收，便会便随一个1次垃圾回收... 所有新建的对象都是0代，当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象
import sys

print(gc.get_threshold())

class Persion(object):
    pass
class Cat(object):
    pass

p = Persion()
c = Cat()
p.name = 'Susan'
p.pet = c
c.master = p
print(sys.getrefcount(p))
print(sys.getrefcount(c))

del p
del c

# 手动回收垃圾
gc.collect()