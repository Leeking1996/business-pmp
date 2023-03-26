# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/23 21:42
# func: 用于初始化数据
from db.content_db import get_db
from domain.config.models import *


def create_file_type():
    """初始化数据库数据"""
    db = get_db()
    value_type_list = list()
    value_type_list.append(ValueType(type_name="字符串", type_value="str"))
    value_type_list.append(ValueType(type_name="是否", type_value="bool"))
    value_type_list.append(ValueType(type_name="整型", type_value="int"))
    value_type_list.append(ValueType(type_name="小数点", type_value="float"))
    db.bulk_save_objects(value_type_list)
    db.commit()

