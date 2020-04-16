# # 装饰器就是一个返回函数的函数，在不影响代码的情况下增加功能
# def log_once(func):
#     def wrapper():
#         print("开始,once")
#         func()
#         print("结束，once")
#
#     return wrapper
#
#
# def log_twice(func):
#     def wrapper():
#         print("开始,twice")
#         func()
#         print("结束，twice")
#
#     return wrapper
#
# @log_once
# @log_twice
# def hello():
#     print("hello")
#
# if __name__ == '__main__':
#     hello()











# # 带参数的装饰器和带参数的函数
# def log(name=None):
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print("{},start".format(name))
#             rest = func(*args, **kwargs)
#             print("{}，end".format(name))
#             return rest
#         return wrapper
#     return decorator
#
#
# @log()
# def hello():
#     print("hello")
#
#
# @log('from add')
# def add(a, b):
#     return a+b
#
# if __name__ == '__main__':
#     hello()
#     print(add(5, 6))











# # 带参数的装饰器和带参数的函数
# from functools import wraps
#
# def log(name=None):
#
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("{},start".format(name))
#             rest = func(*args, **kwargs)
#             print("{}，end".format(name))
#             return rest
#         return wrapper
#     return decorator
#
#
# @log()
# def hello():
#     """简单功能模拟"""
#     print("hello")
#
#
# if __name__ == '__main__':
#     print(hello.__doc__)
#     print(hello.__name__)
#     hello()








# # 类的装饰器
# def f(self):
#     print('{}要吃东西'.format(self.name))
#
# def eat(cls):
#     # cls.eat = lambda self: print('{}要吃东西'.format(self.name))
#     cls.eat = f
#     return cls
#
# @eat
# class cat(object):
#     def __init__(self, name):
#         self.name = name
#
# if __name__ == '__main__':
#     cat = cat('小黑')
#     cat.eat()