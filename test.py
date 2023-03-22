# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/21 21:22
# func: 递归
from db.content_db import get_db
from domain.config.models import SysDepartment


def test():
    db = get_db()
    data = db.query(SysDepartment).all()
    all_data = list()
    for i in data:
        children = digui(i.id, i.departmentData)
        one_department_dict = i.to_dict()
        one_department_dict.update({"children": children})
        all_data.append(one_department_dict)
    print(all_data)
def digui(parent_id, data):
    children = list()
    for i in data:
        if parent_id == i.parent_id:
            one_department_dict = i.to_dict()
            data_list = digui(i.id, i.departmentData)
            if data_list:
                one_department_dict.update({"children": data_list})
            children.append(one_department_dict)
    return children





if __name__ == '__main__':
    test()
