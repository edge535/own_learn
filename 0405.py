from functools import reduce


def use_filer(l):
    """
    获取指定列表/元组中的奇数
    :param l: list/tuple要过滤的数据
    :return: 过滤好的奇数列表
    """
    rest = filter(lambda n: n % 2 != 0, l)
    return rest


def pow_number(l):
    """
    根据给定的列表数据，计算每一项的立方
    :param l:  list/ type int类型的列表或者元组
    :return:  原来列表中的每一项
    """
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
    return rest_list


def f(n):
    """
    求给定数的立方
    """
    return n * n * n
def pow_number_map(l):
    """
    使用map 根据给定的列表数据，计算每一项的立方
    :param l:  list/ type int类型的列表或者元组
    :return:  原来列表中的每一项
    """
    return map(f,l)


def pow_number_lambda(l):
    return map(lambda n: n * n * n, l)


def get_sum(l):
    """
    根据给定的列表，求各个数字的总和
    :param l:  list/type里面是整数
    :return:  列表所有的和
    """
    rest = 0
    for i in l:
        rest += i
    return rest


def get_sum_use_py(l):
    """
    使用python内置的sum（）求和
    :param l:  list/type里面是整数
    :return:  列表所有的和
    """
    return sum(l)


def ff(m, n):
    return m + n
def get_sum_use_reduce(l):
    """
    使用reduce进行求和
    :param l:  list/type里面是整数
    :return:  列表所有的和
    """
    return reduce(ff, l)


def get_sum_use_lambda(l):
    """
    使用lambda进行求和
    :param l:  list/type里面是整数
    :return:  列表所有的和
    """
    return reduce(lambda m, n: m + n, l)

if __name__ == '__main__':
    # l = range(1, 11)
    # rest = use_filer(l)
    # print(list(rest))
    #
    # l = range(1, 11)
    # rest = pow_number(l)
    # print(rest)
    #
    # l = range(1, 11)
    # rest = pow_number_map(l)
    # print(list(rest))
    #
    # l = range(1, 11)
    # rest = pow_number_lambda(l)
    # print(list(rest))
    #
    # l = map(str, (1, 2, 3, 4))
    # print(list(l))
    #
    # l = range(1, 11)
    # rest = get_sum(l)
    # print(rest)
    #
    # rest = get_sum_use_py(l)
    # print(rest)
    #
    # rest = get_sum_use_reduce(l)
    # print(rest)
    #
    # rest = get_sum_use_lambda(l)
    # print(rest)

    print(reduce(lambda x, y: x * y, range(1,21)))
