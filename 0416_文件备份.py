
import os
import os.path



class filebackup():
    """
    文本文件备份
    """

    def __init__(self, src, dist):
        """
        构造方法
        :param src: 需要备份的文件目录
        :param dist:  备份后的目录
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取指定src目录下的所有文件
        """
        ls = os.listdir(self.src)
        # print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        """
        # 1.判断list是否存在，不存在则创建目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定目录不存在，创建完成")

        # 拼接完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        # 2.判断文件是否为我们要备份的文件
            # 2.1判断是否为文件夹
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            print(full_src_path)
            # 3.读取文件的内容
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist:
                print(">>开始备份【{}】".format(file_name))
                # 4.把读取到的内容写到新文件中
                with open(full_src_path, 'r', encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.readlines()
                        if not rest:
                            break
                        f_dist.writelines(rest)
                    f_dist.flush()
                print(">>备份完成【{}】".format(file_name))
        else:
            print("文件类型不符合要求")





class filebackup2():
    """
    文本文件备份,优化
    """

    def __init__(self, src, dist):
        """
        构造方法
        :param src: 需要备份的文件目录
        :param dist:  备份后的目录
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取指定src目录下的所有文件
        """
        ls = os.listdir(self.src)
        # print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        """
        # 1.判断list是否存在，不存在则创建目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定目录不存在，创建完成")

        # 拼接完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        # 2.判断文件是否为我们要备份的文件
            # 2.1判断是否为文件夹
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            print(full_src_path)
            # 3.读取文件的内容
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist, \
                open(full_src_path, 'r', encoding='utf-8') as f_src:
                print(">>开始备份【{}】".format(file_name))
                # 4.把读取到的内容写到新文件中
                while True:
                    rest = f_src.readlines()
                    if not rest:
                        break
                    f_dist.writelines(rest)
                f_dist.flush()
                print(">>备份完成【{}】".format(file_name))
        else:
            print(full_src_path)
            print("文件类型不符合要求")


if __name__ == '__main__':
    # src_path = 'E:\\python_project_mk\\src'
    # dist_path = 'E:\python_project_mk\dist'

    base_path = os.path.dirname(os.path.abspath(__file__))  # 得到当前代码的目录名称
    src_path = os.path.join(base_path, 'src')
    dist_path = os.path.join(base_path, 'dist')

    # bak = filebackup(src_path, dist_path)
    # bak.read_files()

    bak = filebackup2(src_path, dist_path)
    bak.read_files()

