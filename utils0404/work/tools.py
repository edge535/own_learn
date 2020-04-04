import os.path
import utils0404.constant as const

def get_file_type(file_name):
    """
    根据文件的名称来判断文件的类型
    :param file_name:str 文件名称
    :return:文件类型
    0：图片文件
    1：word文件
    2：excel文件
    3：ppt
    -1:未知
    """
    result = const.FILE_TYPE_UNKNOW
    #不是文件类型直接返回
    if not os.path.isfile(file_name ):
        return result
    path_name, ext = os.path.splitext(file_name)
    #后缀名统一成小写
    ext = ext.lower()
    if ext in (".png", ".jpg", ".gif", ".bmp"):
        result = const.FILE_TYPE_IMG
    elif ext in ('.doc', '.docx'):
        result = const.FILE_TYPE_DOC
    elif ext in ('.xls', '.xlsx'):
        result = const.FILE_TYPE_EXCEL
    elif ext in ('.ppt', 'pptx'):
        result = const.FILE_TYPE_PPT
    return result