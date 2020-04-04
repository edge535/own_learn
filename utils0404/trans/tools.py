import random
from datetime import datetime


def gen_trans_id(date = None):
    """
    根据传入的时间得到一个唯一的交易流水ID
    :param date: 日期
    :return: 交流流水字符串
    """
    #如果没有传入时间，使用当前的时间
    if date is None:
        date = datetime.now()
    #保证唯一 日期+时间+毫秒+六位随机数
    return date.strftime("%y%m%d%H%M%S%f") + str(random.randint(10000, 999999))