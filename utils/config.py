# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/7 21:18
import math


def config_paging(q_filter, page, size):
    # 使用偏移量进行数据分页
    """
    :param q_filter: 查询数据的sql
    :param page: 当前页码数
    :param size: 当前一页数据
    :return:
    """
    counts = q_filter.count()
    page_nums = math.ceil(counts / size)
    offset_data = size * (page - 1)
    all_data = q_filter.offset(offset_data).limit(size).all()
    all_data_list = [i.to_dict() for i in all_data]
    return {
        "counts": counts,
        "page": page,
        "size": size,
        "page_nums": page_nums,
        "data_list": all_data_list
    }
