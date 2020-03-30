# # 字典的创建
# # 1. 使用{}
# dict1 = {}  # 空的字典
# print(type(dict1))
# dict2 = {'name': '王峰', 'sex': "男",
#          'hiredate': '1997-10-20', 'grade': 'A',
#          'job': '销售', 'salary': 1000,
#          'welfare': 100
#          }
# print(dict2)
#
# # 2. 利用dict函数创建字典
# dict3 = dict(name='王峰',sex='男',hiredate='1997-10-20')
# print(dict3)
# dict4 = dict.fromkeys(['name' , 'sex' , 'hiredate' , 'grade'] , 'N/A')
# print(dict4)
#
#
#
#
# # 字典的取值操作
# employee = {'name': '王峰', 'sex': "男",
#             'hiredate': '1997-10-20', 'grade': 'A',
#             'job': '销售', 'salary': 1000,
#             'welfare': 100
#             }
#
# # 字典的取值
# name =  employee['name']
# print(name)
# salary = employee['salary']
# print(salary)
#
# print(employee.get('job'))
# print(employee.get('dept' , '其他部门'))
#
# # in 成员运算符
# print('name' not in employee)
# print('dept' not in employee)
#
# # 遍历字典
# for key in employee:
#     v = employee[key]
#     print(v)
#
# for k,v in employee.items():
#     print(k,v)
#
#     # 字典的更新操作
#     employee = {'name': '王峰', 'sex': "男",
#                 'hiredate': '1997-10-20', 'grade': 'A',
#                 'job': '销售', 'salary': 1000,
#                 'welfare': 100
#                 }
#     print(employee)
#     # 单个kv进行更新
#     employee['grade'] = 'B'
#     print(employee)
#     # 对多个kv进行更新
#     employee.update(salary=1200, welfare=150)
#     print(employee)
#
#     # 字典的新增操作与更新操作完全相同,秉承有则更新,无则新增的原则
#     employee['dept'] = '研发部'
#     print(employee)
#     employee['dept'] = '市场部'
#     print(employee)
#     employee.update(weight=80, dept='财务部')
#     print(employee)
#
#     # 与删除相关的函数
#     # 1. pop 删除指定的kv
#     employee.pop('weight')
#     print(employee)
#
#     # 2.popitem 删除最后一个kv
#     kv = employee.popitem()
#     kv = employee.popitem()
#
#     print(kv)
#     print(employee)
#
#     # 3. clear 清空字典
#     employee.clear()
#     print(employee)
#
#     emp1 = {'name': 'Jacky', 'grade': 'B'}
#     emp2 = {'name': 'Lily', 'grade': 'A'}
#     # 1. setdefault为字典设置默认值,如果某个key已存在则忽略,如果不存在则设置
#     emp1.setdefault('grade', 'C')
#     emp2.setdefault('grade', 'C')
#
#     # if 'grade' not in emp2:
#     #    emp2['grade'] = 'C'
#     print(emp2)
#
#     # 2. 获取字典的视图
#     # (1) keys 代表获取所有的键
#     ks = emp1.keys()
#     print(ks)
#     print(type(ks))
#     # (2) values 代表获取所有的值
#     vs = emp1.values()
#     print(vs)
#     print(type(vs))
#     # (3) items 代表获取所有的键值对
#     its = emp1.items()
#     print(its)
#     print(type(its))
#
#     emp1['hiredate'] = '1984-05-30'
#     print(ks)
#     print(vs)
#     print(its)
#
#     # 3. 利用字典格式化字符串
#     # 老版本的字符串格式化
#     emp_str = "姓名:%(name)s,评级:%(grade)s,入职时间:%(hiredate)s" % emp1
#     print(emp_str)
#
#     # 新版本的字符串格式化
#     emp_str1 = "姓名:{name},评级:{grade},入职时间:{hiredate}".format_map(emp1)
#     print(emp_str1)
#
#
#
#
# # 散列值 hash()
# h1 = hash("abc")
# print(h1)
# h2 = hash("bcd")
# print(h2)
# h3 = hash(8838183)
# print(h3)
# h4 = hash("abc")
# h5 = hash("def")
# print(h4)
# print(h5)
#
#


# # 处理员工shuju
# source = '7782,CLARK,MANAGER,SALES,5000$7934,MILLER,SALESMAN,SALES,3000$7369,SMITH,ANALYST,RESEARCH,2000'
# employee_list = source.split('$')
# all_emp = {}
# for i in range(len(employee_list)):
#     e = employee_list[i].split(',')
#     employee = {"no": e[0], 'name': e[1], 'job': e[2], 'department': e[3], 'salary': e[4]}
#     all_emp[employee['no']] = employee
# print(all_emp)
# for k, v in all_emp.items():
#     print(k, "编号：{no}， 名字：{name}， 工作：{job}， 部门：{department}， 收入：{salary}".format_map(v))


