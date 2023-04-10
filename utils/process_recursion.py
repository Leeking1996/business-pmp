# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/28 19:15
# func: 处理单表中存在id，parent_id 递归

class Handle(object):

    def __init__(self, all_data):
        self.all_data = all_data
        self.flag = list()

    def circulate(self):
        new_data = list()
        for i in self.all_data:
            if i.get("id") in self.flag:
                continue
            children = self.recurrence(i, self.all_data)
            i.update({"children": children})
            new_data.append(i)
        return new_data

    def recurrence(self, i, all_data):
        children = list()
        for one_data in all_data:
            if i.get("id") == one_data.get("parent_id"):
                data = self.recurrence(one_data, all_data)
                one_data.update({"children": data})
                # 最外层的id 得跳过内层中的children 的id
                self.flag += [one_data.get("id")]
                children.append(one_data)
        return children
