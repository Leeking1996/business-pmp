# encoding=utf-8
from Interface.user import user_api


def register_api_path(path):
    """注册接口，如果接口不存在则抛出异常"""
    if path not in user_api:
        return False
    return True
