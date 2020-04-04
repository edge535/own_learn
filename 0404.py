# from datetime import datetime
# import time
#
# now_time = datetime.now()
#
# print("now: {0}".format(now_time))
#
# # 当前的日期
# print('now day: {0}'.format(now_time.date()))
#
# # 当前的时间
# print('now time: {0}'.format(now_time.time()))
#
# print('now day2: {0}'.format(datetime.today()))
#
# print('year: {0}'.format(now_time.year))
# print('month: {0}'.format(now_time.month))
# print('day: {0}'.format(now_time.day))
# print('microsecond: {0}'.format(now_time.microsecond))
#
# print(dir(now_time))
#
# print('------------------')
# # 获取到毫秒数
# print(time.time())
# #
# time.sleep(2)

# def fun():
#     import  time
#     time.sleep(5)
#     print("睡了五秒")
#
# fun()

# import time
# from datetime import  datetime
# dt = datetime.now()
# print(dt.microsecond)
# print(time.time())










from datetime import datetime, date, time, timedelta

# 1.自定义日期和时间
d = datetime(2020, 10, 30, 14, 5)
print(d)

d2 = date(2019, 3, 23)
print(d2)

t = time(9, 0)
print(t)

print('---------1-----------')
# 2. 日期、时间与字符串之间的相互转换
# 字符串转换datetime对象
ds = '2018/10/3T3:42:09'
ds_t = datetime.strptime(ds, '%Y/%m/%dT%I:%M:%S')
print(ds_t)
print(ds_t.second)
# datetime对象转换成字符串
print('-----2---------')
n = datetime.now()
print(n)
n_str = n.strftime('%m')
print(n_str)
print(n.strftime('%A'))


# 3. datetime之间的加减操作
print('------3-------')
n = datetime.now()
print(n)
n_next = n + timedelta(days=-5, hours=0, minutes=0, seconds=0, microseconds=0)
print(n_next)

print('---------------')
# 时间的减法
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)

rest = d2 - d1
print(type(rest))
print(rest.days)

rest2 = d1 - d2
print(rest2.days)
