# # 迭代器
# class pownumber(object):
#     """
#     迭代器
#     生成1，2，3，4，5。。。。的平方
#     # """
#
#     value = 0
#
#     def __next__(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value * self.value
#
#     def __iter__(self):
#         return self
#
#
# if __name__ == '__main__':
#     pow = pownumber()
#     # 一种
#     # print(pow.__next__())
#     # print(pow.__next__())
#     # print(pow.__next__())
#
#     # 两种
#     # print(next(pow))
#     # print(next(pow))
#     # print(next(pow))
#     # print(next(pow))
#     # print(next(pow))
#
#     #三种
#     for i in pow:
#         print(i)










# # 生成器
# def pow():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
# def pow_number():
#     return (x*x for x in [1, 2, 3, 4, 5])
#
# def pow_number2():
#     for x in [1, 2, 3, 4, 5]:
#         yield x*x
#
# if __name__ == '__main__':
#     # rest = pow()
#     # print(next(rest))
#     # print(next(rest))
#     # print(next(rest))
#     # print(next(rest))
#     # print(next(rest))
#
#     # for i in rest:
#     #     print(i)
#
#     rest = pow_number2()
#     print(next(rest))
#     print(next(rest))










# 模拟range
def user_range():
    """python内置range"""
    for i in range(5, 10):
        print(i)


class iterrange(object):
    """迭代器模拟"""
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        return self


class genrange(object):
    """生成器模拟"""
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def gen_num(self):
        while True:
            if self.start >= self.end - 1:
                break
            self.start += 1
            yield self.start


def get_gen(start, end):
    start -= 1
    while True:
        if start >= end - 1:
            break
        start += 1
        yield start


if __name__ == '__main__':
    # user_range()
    iter = iterrange(5, 10)
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))
    # print(next(iter))

    gen = genrange(5, 10).gen_num()
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    ggen = get_gen(5, 10)
    # print(next(ggen))
    # print(next(ggen))
    # print(next(ggen))
    # print(next(ggen))
    # print(next(ggen))