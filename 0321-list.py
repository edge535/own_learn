# #列表的创建
# #变量名=[元素1,元素2,....]
# list = ['a' , 'b' , 'c' , 'd' , 1 , 2 , 3 , 4]
# print(list)
# list1 = []
# print(list1)
#
#
#
# # 列表的取值
# list = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# print(list)
# # 取值的语法: 变量 = 列表变量[索引值]
# zhaoliu = list[3]
# print(zhaoliu)
# zhaoliu = list[-3]
# print(zhaoliu)
#
# # 范围取值: 列表变量 = 原列表变量[起始索引:结束索引]
# # 在Python中列表范围取值是"左闭右开"
# list1 = list[1: 4]
# print(list1)
# print(list1[-1])
#
# # 列表的index函数用于获取指定元素的索引值
# zhaoliu_index = list.index('赵六')
# print(zhaoliu_index)
#
#
#
#
# # 遍历列表
# persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
#
# count = len(persons)  # 获取列表长度
# print(count)
# # for循环用于遍历列表
# # for 迭代变量 in 可迭代对象
# i = 0
# for p in persons:
#     if p == '赵六':
#         ri = count * -1 + i
#         print(p, i, ri)
#     i += 1
#
# i = 0
# while i < len(persons):
#     p = persons[i]
#     if p == '赵六':
#         ri = count * -1 + i
#         print(p , i , ri)
#     i += 1
#
#
#
#
#
# #列表的反转与排序
# persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# persons.reverse() #reverse方法用于反转列表
# print(persons)
#
# numbers = [28,32,14,12,53,42]
# numbers.sort(reverse=True) #sort()用于排序,reverse=True代表降序排列
# print(numbers)
#
#
#
#
# # 列表的写操作
# persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
# # 列表的追加
# persons.append("杨九")
# print(persons)
# # 列表的插入
# persons.insert(2 , '刘二')
# print(persons)
# persons.insert(len(persons) , '候大')
# print(persons)
#
# # 列表的更新
# persons[2] = '宋二'
# print(persons)
# # 列表范围取值是"左闭右开"
# persons[3:5] = ['王五','李四']
# print(persons)
#
# # 列表的删除操作
# # 按元素内容删除
# persons.remove('宋二')
# print(persons)
# # 按索引值删除元素
# persons.pop(4)
# print(persons)
# # 范围删除
# persons[4:7] = []
# print(persons)
#
#
#
#
# # 其他常用方法
# persons = ['张三', '赵六', '李四', '王五', '赵六', '钱七', '孙八']
#
# #统计出现次数
# cnt = persons.count('赵六')
# print(cnt)
#
# #追加操作
# #append将整个列表追加到末尾,extend则是将列表中的元素追加到原始列表末尾
# persons.append(['杨九' ,'吴十'])
# print(persons)
# persons.extend(['杨九' , '吴十'])
# print(persons)
#
# #in(成员运算符) 运算符用于判断数据是否在列表中存在,存在返回True,不存在返回False
# persons.remove('张三')
# b = '张三' in persons
# print(b)
#
# #copy 函数用于复制列表
# persons1 = persons.copy()
# persons2 = persons
# print(persons1)
# #is 身份运算符用于判断两个变量是否指向同一块内存
# print(persons1 is persons)
# print(persons2 is persons)
#
#
# #clear 用于清空列表
# persons.clear()
# print(persons)
# print(persons1)
# print(persons2)
#
#
#
#
# # 多维列表(嵌套列表)
# # [[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资],[姓名,年龄,工资]]
# # 字符串:"姓名,年龄,工资"例如: "张三,30,2000"
# # str = "张三,30,2000"
# # l = str.split(",")
# # print(l)
# emp_list = []
# while True:
#     info = input("请输入员工信息:")
#     if info == "":
#         print("程序结束")
#         break
#     info_list = info.split(",")
#     if len(info_list) != 3:
#         print("输入格式不正确,请重新输入")
#         continue
#     emp_list.append(info_list)
#     # print(emp_list)
#
#     for emp in emp_list:
#         print("{n},年龄:{a},工资:{s}".format(n=emp[0],a=emp[1],s=emp[2]))