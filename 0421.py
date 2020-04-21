#
# 简单理解
# def test_div(num1, num2):
#     """
#     当除数为0时
#     :param num1:
#     :param num2:
#     :return: num1 / num2
#     """
#     return num1 / num2
#
# if __name__ == '__main__':
#     try:
#         rest = test_div(5, 1)
#         print(rest)
#     except (ZeroDivisionError, TypeError) as e:
#         print('报错了')
#         print(e)
#     finally:
#         print('无论程序是否报错，都要执行这一句话')









# # 自定义异常
# class ApiException(Exception):
#     """自定义异常"""
#     err_code = ''
#     err_msg = ''
#
#     def __init__(self, err_code=None, err_msg=None):
#         self.err_code = self.err_code if self.err_code else err_code
#         self.err_msg = self.err_msg if self.err_msg else err_msg
#
#     def __str__(self):
#         return 'Error:{0} - {1}'.format(self.err_code, self.err_msg)
#
# class ChuShuWeiLing(ApiException):
#     """除数为零"""
#     err_code = '40001'
#     err_msg = '除数为0'
#
# class CanShuWeiFeiInt(ApiException):
#     """参数不能整数"""
#     err_code = '40002'
#     err_msg = '参数不为整数'
#
#
# def divide(num1, num2):
#     """除法的实现"""
#     # 两个数必须为整数
#     if not isinstance(num1, int) or not isinstance(num2, int):
#         raise CanShuWeiFeiInt()
#     #除数不能为零
#     if num2 == 0:
#         raise ChuShuWeiLing()
#     return num1 / num2
#
#
# if __name__ =='__main__':
#     try:
#         divide(5, 's')
#     except ApiException as err:
#         print('出错了')
#         print(err)





























# 错误的传递     异常逐层向上传递
class MyException(Exception):
    """自定义异常"""
    pass

def v_for():
    """自定义函数"""
    for i in range(1, 100):
        if i == 20:
            raise MyException
        print(i)

def call_v_for():
    print('开始调用v_for')
    try:
        v_for()
    except MyException:
        print('----------------------')
    print('结束调用v_for')

def test_raise():
    print('测试函数')
    call_v_for()
    print('测试完毕')

if __name__ == '__main__':
    test_raise()