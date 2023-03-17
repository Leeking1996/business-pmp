# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/7 21:44
# func: 调用项目接口
from utils.consul_ import InitializationServer


class Invocation(object):
    def __init__(self, domain_name, api, method, body=None, params=None):
        self.domain_name = domain_name
        self.api = api
        self.method = method
        self.body = body
        self.params = params

    def call_api(self):
        """调用接口"""
        init = InitializationServer(self.domain_name)
        project_address = init.detection()
        url = F"{project_address}{self.api}"
        return url


I = Invocation("pmp-project", "/project/test", "get")
