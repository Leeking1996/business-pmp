# -*- coding:utf-8 -*-
# Author: lee
# 2023/1/30 22:37
from db import engine
from domain.config import models as config_models


def auto_create_models():
    """自动创建表"""
    config_models.Base.metadata.create_all(bind=engine)
