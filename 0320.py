# #赋值运算符
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# #加法赋值运算符
# #a = a + 1
# a += 1
# str = 'abc'
# str += 'bcd' #str = str + 'bcd'
# print(str)
#
# #减法、乘法、除法赋值运算符
# b -= a #b = b-a
# print(b)
# c *= 3
# print(c)
# d /= 10
# print(d)
#
# #取模、幂赋值、取整除赋值运算符
# e %= 4 #1
# print(e)
# f **= 2 # 6的2次方 36
# print(f)
# g //= 2 # 7 // 2 3
# print(g)


# #成员运算符
# sheet = ['张三' , '李四' , '王五']
# if ('张三' in sheet):
#     print("张三在听课")
# else:
#     print("张三已旷课")
#
# #身份运算符
# a = 5
# b = a
# c = 5.0
# print(a is b)
# print(a == c) #数值比较
# print(a is c) #内存地址比较



# #位运算符
# a = 60 #60的二进制：00111100
# b = 13 #13的二进制：00001101
# c = 0
# #00001100 = 12
# c = a & b
# print("a & b : " , c)
#
# #00111101 = 61
# c = a | b
# print("a | b : " , c)
#
# #00110001 = 49
# c = a ^ b
# print("a ^ b : " , c)
#
# #11000011 = -61
# #-(~11000011+1)
# #-(00111100+1)
# #-00111101 = -61
# c = ~a
# print("~a :" , c)
#
# #00111100
# #00111100000 = 480
# c = a << 3
# print("a << 3" , c)
#
# #00111100
# #00000111 = 7
# c = a >> 3
# print("a >> 3" , c)


# a = 199
# print(~a)

'''
    对于按位取反，规则为：
    eg:  199=11000111
    取反：00111000
    公示：-（~00111000+1）
         -（11000111+1）
         -（11001000）
        = -200
'''
a  = [199 ,60 , -64]
print(a)                    #[199, 60, -64]
for i in range(len(a)):
    print(~a[i] , end=' ')  #-200 -61 63