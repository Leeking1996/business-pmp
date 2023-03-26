# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/21 21:22
# func: 递归
import json

from db.content_db import get_db
from domain.config.models import SysDepartment


# def test():
#     db = get_db()
#     data = db.query(SysDepartment).all()
#     all_data = list()
#     for i in data:
#         children = digui(i.id, i.departmentData)
#         one_department_dict = i.to_dict()
#         one_department_dict.update({"children": children})
#         all_data.append(one_department_dict)
#     print(all_data)


# def digui(parent_id, data):
#     children = list()
#     for i in data:
#         if parent_id == i.parent_id:
#             one_department_dict = i.to_dict()
#             data_list = digui(i.id, i.departmentData)
#             if data_list:
#                 one_department_dict.update({"children": data_list})
#             children.append(one_department_dict)
#     return children

class Data:
    # 数据判断，如果已经展示数据，则进行跳过
    def __init__(self):
        self.flag = list()

    def test3(self):
        menus = [
            {
                "id": 12,
                "parent_id": None,
            },
            {
                "id": 13,
                "parent_id": 12,
            },
            {
                "id": 3,
                "parent_id": None,
            },
            {
                "id": 4,
                "parent_id": 3,
            },
            {
                "id": 15,
                "parent_id": 12,
            },
            {
                "id": 22,
                "parent_id": 13
            }

        ]
        # 编写递归， 循环展示数据
        new_data = list()
        for i in menus:
            if i.get("id") in self.flag:
                continue
            children = self.digui(i, menus)
            i.update({"children": children})
            new_data.append(i)
            # 怎么取消双循环带来的弊端，

        print(json.dumps(new_data))

    def digui(self, i, menus):
        children = list()
        for menu in menus:
            if i.get("id") == menu.get("parent_id"):
                data = self.digui(menu, menus)
                menu.update({"children": data})
                self.flag += [menu.get("id")]
                children.append(menu)
        return children


if __name__ == '__main__':
    data = Data()
    data.test3()
