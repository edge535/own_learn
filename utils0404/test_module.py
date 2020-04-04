from datetime import datetime
from utils0404.trans.tools import *
from utils0404.work.tools import *

def test_trans_tool():
    """测试trans包下的tools模块"""
    id1 = gen_trans_id()
    print(id1)
    date = datetime(2020, 4, 4, 22, 44)
    id2 =gen_trans_id(date)
    print(id2)

def test_work_tool():
    """测试work模块"""
    path = 'C:\\Users\\hasee\\Desktop\\微信图片_20180803004033.jpg'
    result = get_file_type(path)
    print(result)

if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()