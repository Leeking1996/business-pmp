# -*- coding:utf-8 -*-
# Author: lee
# 2023/4/8 19:38
# func: 项目定级配置接口
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.content_db import get_db_content
from domain.score.schemy import CreateScore
from Interface.score import curd
from utils.return_response import *

router = APIRouter(tags=["项目定级"], prefix="/config")


@router.post("/score", name="创建数据")
async def create_first_score(createScore: CreateScore, db: Session = Depends(get_db_content)):
    """创建一级数据"""
    judge_data = await curd.create_score(createScore, db)
    if judge_data:
        return success()
    return error()


@router.put("/score", name="更新数据")
async def update_score(createScore: CreateScore, db: Session = Depends(get_db_content)):
    """更新定级数据"""
    judge_data = await curd.update_score(createScore, db)
    if judge_data:
        return success()
    return error()


@router.get("/score", name="查看数据")
async def search_score(template_id: str, db: Session = Depends(get_db_content)):
    judge, data = await curd.search_score(template_id, db)
    if judge:
        return success(data)
    return error()


@router.delete("/score", name="删除数据")
async def delete_score(template_id: str, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete(template_id, db)
    if judge_data:
        return success()
    return error()
