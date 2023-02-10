# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/9 22:53
# Func: 验证模块，token验证模块

import base64
from datetime import timedelta, datetime
from typing import Optional
import jwt
from fastapi import HTTPException
from starlette import status


def generate_access_token(data: dict, expiration: Optional[timedelta] = None):
    """
    生成token并加密
    :param data:
    :param expiration:
    :return:
    """
    to_encode = data.copy()
    if expiration:
        expire = datetime.utcnow() + expiration
    else:
        expire = datetime.utcnow() + timedelta(hours=8)
    to_encode.update({"exp": expire})
    to_encode_jwt = jwt.encode(to_encode, key="lee", algorithm="HS256")
    # base64加密
    content_b = to_encode_jwt.encode("utf-8")
    data = base64.b64encode(content_b)
    return data.decode("utf-8")


def verify_token(token):
    """
    获取用户并解密token
    :param x_token:
    :param token:
    :return:
    """
    credentials_exception_token = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={"Message": " 用户未登录或者登陆 token 已经失效！"})
    try:
        #   解析token值
        token_b = base64.b64decode(token).decode("utf-8")
        payload = jwt.decode(token_b, key="lee", algorithms="HS256")
        if isinstance(payload, dict):
            return payload
    except Exception as e:
        print(e, "eeeeee")
        return credentials_exception_token
