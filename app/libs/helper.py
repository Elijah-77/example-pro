# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2018/07/12 
"""
import datetime
import os
import time
import uuid


def change_filename(filename):
    """
    修改文件名称
    :param filename:
    :return:
    """
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
               str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


def get_timestamp(dt, fmt="%Y-%m-%d"):
    """将2018-xx-xx格式数据转换为'1531881731'
    "
    :param dt:
    :param fmt:
    :return:
    """
    if dt is not None:
        time_array = time.strptime(dt, fmt)
        return int(time.mktime(time_array))
    return None


def str_timestamp(dt, fmt="%Y-%m-%d"):
    """将1531881731类型转换为'2018-xx-xx'
    """
    __time = time.localtime(dt)
    time_array = time.strftime(fmt, __time)
    return time_array
