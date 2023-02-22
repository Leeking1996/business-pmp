#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import consul
import socket

import requests


def get_ip():
    """注册服务中心"""
    name = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    name.connect(('8.8.8.8', 80))

    ip = name.getsockname()[0]

    return ip


class InitializationServer(object):
    def __init__(self, port: int, server_name, key=None, value=None):
        """注册服务"""
        self.key = key
        self.value = value
        self.ip = get_ip()
        self.port = port
        self.server_name = server_name
        cursor = consul.Consul(host='127.0.0.1', port=8500)
        self.cursor = cursor

    def register(self):
        """注册服务"""
        self.cursor.agent.service.register(
            name=self.server_name, address=self.ip, port=self.port,
            # 心跳检查：间隔：5s，超时：30s，注销：30s
            check=consul.Check().tcp(self.ip, self.port, '5s', '30s', '30s')
        )

    def detection(self):
        """发现服务"""
        # # 获取服务
        services = self.cursor.agent.services()
        address = F"{services.get(self.server_name).get('Address')}:{services.get('pmp_config').get('Port')}"
        return address

    def get_value(self):
        """获取数据"""
        val = self.cursor.kv.put(self.key)
        return val

    def add_data(self):
        """增加数据"""
        self.cursor.kv.put(self.key, self.value)

    def logout(self):
        """
        注销服务
        """
        service_id = self.cursor.agent.services().get(self.server_name).get("ID")
        self.cursor.agent.service.deregister(service_id=service_id)
