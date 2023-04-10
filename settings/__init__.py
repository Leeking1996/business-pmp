"""服务端口和服务名称"""
import os

port = 8030
server_name = "pmp-config"


env = os.getenv("ENV")
if env == "PRO":
    from settings.pro_settings import *
elif env == "GET":
    from settings.dev_setting import *
else:
    from settings.dev_setting import *