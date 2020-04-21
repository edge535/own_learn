
# 身份证匹配
# 123456 1999 10 07 789 9
# (\d{6})(\d{4})((\d{2})(\d{2}))(\d{2})(\d{1})(\d|[x,X])


# 电子邮箱匹配
# 123456@qq.com
# 123456@vip.qq.com
# 123456@forxmail.com
# 123456@163.com.cn
# 123456@xx.net
# [a-zA-Z0-9_-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,5})

import re

# # 将正则表达式进行编译
# pattern = re.compile(r'hello', re.I)
#
# # 通过match进行匹配
# rest = pattern.match('Hello world！')
# print(rest)
# print(rest.string)
# print(rest.re)


# # 找出字符串中的数字
# content = 'one1two2three3four4five5six698'
# p = re.compile(r'\d')
# rest = p.findall(content)
# print(rest)


# # 使用search
# content = 'hello, world!'
# p = re.compile(r'world')
# rest = p.search(content)
# print(rest)
# # 使用match
# rest_match = p.match(content)
# print(rest_match)


# # group 和 groups
# content = 'hello, world!'
# p = re.compile(r'world')
# rest = p.search(content)
# print(rest)
# if rest:
#     print(rest.group())
#     print(rest.groups())



# def test_id_card():
#     """身份证正则匹配"""
#     # p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))(\d{2})(\d{1})(\d|[x,X])')
#     p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))(\d{2})(\d{1})(\d|[x,X])')
#     id1 = '123456199910077899'
#     id2 = '65432119940410698X'
#     rest1 = p.search(id1)
#     rest2 = p.search(id2)
#     print(rest1.group())
#     print(rest1.group(1))
#     print(rest1.group(2))
#     print(rest1.group(3))
#     print(rest1.groups())
#     print(rest2.groups())
#     print(rest1.groupdict())


# 正则进行分割
# s = 'one1two2three3four4five5six698'
# p = re.compile(r'\d+')
# rest = p.split(s)
# print(rest)


# 正则进行替换
# s = 'one1two2three3four4five5six698'
# p = re.compile(r'\d+')
# rest = p.sub('@', s)
# print(rest)


# # 前后两个单词换位
# s2 = 'hello world'
# p2 = re.compile(r'(\w+) (\w+)')
# rest = p2.sub(r'\2~\1', s2)
# print(rest)
#
#
# # 在原有基础上，替换并改变内容
# def f(m):
#     return m.group(2).upper()+' '+m.group(1)
# rest_change = p2.sub(f, s2)
# print(rest_change)
#
#
# # 使用匿名函数进行替换
# rest_lamb = p2.sub(lambda m: m.group(2).upper()+' '+m.group(1), s2)
# print(rest_lamb)




#使用正则表达式找到图片的地址
def test_re_img():
    with open('img.html', encoding ='utf-8') as f:
        html = f.read()
        p = re.compile(r'<img.+?src=\"(.+?)\".+?>')
        lsit_img = p.findall(html)
        for ls in lsit_img:
            ls.replace('&amp;', '&')