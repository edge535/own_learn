import random
from datetime import datetime

def read_file():
    """读取文件"""
    file_name = 'test.txt'
    file_path = 'E:\\python_project_mk\\test.txt'
    file_path2 = 'E:/python_project_mk/test.txt'
    #用普通方式打开
    f = open(file_path2, encoding='UTF-8')
    # rest = f.readlines()
    # print(rest[0])
    # print(f.read())
    # f.seek(3)#跳过一个汉字
    # print(f.read(5))
    f.close()

def write_file():
    file_name = 'write_file.txt'
  #  with open(file_name, 'w', encoding="UTF-8") as f:
        # f.write("hello")
        # f.write('\n')
        # f.write("world")
        # l = ['第一行', '\n', '第二行', '\n', '第三行']
        # f.writelines(l)

    with open(file_name, 'a', encoding="utf-8") as f:
        #记录用户日志
        for i in range(6):
            rest = '用户：{0} - 访问时间{1} \n'.format(random.randint(100, 1000), datetime.now())
            f.write(rest)


def read_and_write():
    file_name = 'read_and_write.txt'
    with open(file_name, 'a+') as f:
        read_rest = f.read()
        if '1' in read_rest:
            f.write('aaa')
        else:
            f.write('bbb')
        f.seek(0)
        print(f.read())

if __name__ == '__main__':
    #read_file()
    #write_file()
    read_and_write()