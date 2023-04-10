# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/28 19:58
# func: 统一调用接口类
from settings import *
import httpx


class CallInterface:
    """统一调用接口类"""

    def __init__(self):
        self.domain = pmp_project_domain

    def request_httpx(self, url, method, data, params):
        """使用异步连接调用接口"""
        with httpx.AsyncClient() as client:
            client

    def search_b_id(self):
        """查询雪花id"""
