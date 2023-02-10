# -*- coding:utf-8 -*-
# Author: lee
# 2023/1/30 21:38
# Func: 链接 数据库
from fastapi import Header

from db import SessionLocal


async def get_db_content(platform_code: str = Header(None, convert_underscores=False)):
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
        db.rollback()


def get_db():
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        raise e
    finally:
        db.close()
        db.rollback()