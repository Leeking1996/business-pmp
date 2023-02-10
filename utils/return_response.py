# -*- coding:utf-8 -*-
# Author: lee
# 2023/1/31 22:28
# Func: 创建返回数据，承接多参数类型
import json

from starlette import status
from starlette.responses import JSONResponse


def success(data=None):
    code = 200
    message = "success"
    content = {"code": code, "message": message}
    if data is not None:
        content.update({"data": data})
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


def error(message=None):
    code = 500
    if message:
        content = {"code": code, "message": message}
    else:
        content = {"code": code, "message": "error"}
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=content)


def message(data):
    # 直接返回数据
    return JSONResponse(data)
