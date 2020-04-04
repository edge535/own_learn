#
# # 匪警[110],火警[119],急救中心[120],道路交通事故报警[122],水上求救专用电话[12395],天气预报[12121],报时服务[12117],森林火警[12119],电力服务[95598],红十字会急救台[999],公安短信报警[12110],通用紧急求救[112],信产部IP/网站备案[010-66411166]
# # 北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风
#
# phone_number = '匪警[110],火警[119],急救中心[120],道路交通事故报警[122],水上求救专用电话[12395],天气预报[12121],报时服务[12117],森林火警[12119],电力服务[95598],红十字会急救台[999],公安短信报警[12110],通用紧急求救[112],信产部IP/网站备案[010-66411166]'
# phone_list = phone_number.split(',')
# print(phone_list)
#
#
# weather_souce = '北京,2019年1月12日,多云,8°C,-4°C,南风3级~上海,2019年1月12日,小雨,9°C,6°C,北风2级~广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风'
# weather_list = weather_souce.split('~')
# weather_dict = dict()
# for i in range(0, len(weather_list)):
#     w = weather_list[i].split(',')
#     wd = {'名字':w[0], '时间':w[1], '天气':w[2], '最高温':w[3], '最低温':w[4], '风':w[5]}
#     weather_dict[wd['名字']] = wd
#
# #随机数
# import random
#
# def fun1(number):                        #双色球
#     for j in range(int(number)):
#         print(j+1,'- ',end=' ')
#         for i in range(6):
#             r = random.randint(1, 33)
#             print(r, end=' ')
#         b = random.randint(1, 16)
#         print(b)
# def fun2(n):                            #号码百事通
#     for p in phone_list:
#         if p.find(n) != -1:
#             print(p)
# def fun3(n):         #天气预报
#     if n in weather_dict:
#         print('城市：{名字}，日期：{时间}，天气状况：{天气}，最高温：{最高温}，最低温：{最低温}，风向：{风}'.format_map(weather_dict[n]))
#     else:
#         print('不存在该城市')
#
# while(True):
#     print("-----------------")
#     print("1-双色球随机选号")
#     print("2-号码百事通")
#     print("3-天气预报")
#     print("0-结束程序")
#     print("-----------------")
#     c = input("输入功能编号：")
#
#     if c == '1':
#         n = input("需要生成几注号码：")
#         fun1(n)
#     elif c == '2':
#         n = input("请输入要查询的机构或者号码:")
#         fun2(n)
#     elif c == '3':
#         n = input("请输入要查询城市:")
#         fun3(n)
#     elif c == '0':
#         print("已退出")
#         break
#     else:
#         print('输入有误')
#
# #新增
# #新增#新增#新增#新增#新增#新增#新增
# #新增
# #新增
# #新增
# #新增
# #新增
# #新增
# #新增
# #新增
#

li = [1,2,3]
print(li)
li.append("qwe")
print(li)
li.append([5,6])
print(li)
li.append(9)
print(li)

li.extend([7,8])
print(li)
li.extend("asd")
print(li)

