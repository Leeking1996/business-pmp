# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 21:53
# func: 实现方法类
from fastapi import APIRouter, Depends
from requests import Session
from db.content_db import get_db_content
from Interface.project_plan import curd
from utils.return_response import *

from domain.project_plan.schemy import *

router = APIRouter(tags=["项目计划"], prefix="/config")


@router.post("/create/project-state", summary="添加阶段")
async def create_project_state(createProjectState: CreateProjectState, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_project_state(createProjectState, db)
    if judge_data:
        return success()
    return error()


@router.get("/search/project-state/{template_id}", summary="查询阶段")
async def search_project_state(template_id: str, db: Session = Depends(get_db_content)):
    judge, data = await curd.search_project_state(template_id, db)
    if judge:
        return success(data)
    return error()


@router.delete("/delete/project-state", summary="删除阶段")
async def delete_project_state(deleteProjectState: DeleteProjectState, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_project_state(deleteProjectState, db)
    if judge_data:
        return success()
    return error()


# wbs配置接口
@router.get("/search/wbs/file", summary="查看wbs可选字段")
async def search_wbs_file():
    judge_data = await curd.search_wbs_file()
    return success(judge_data)


@router.post("/create/project/plan", summary="保存项目计划整体模块")
async def create_project_plan(projectPlan: ProjectPlan, db: Session = Depends(get_db_content)):
    """保存项目计划整体模块"""
    judge_data = await curd.create_project_plan(projectPlan, db)
    if judge_data:
        return success()
    return error()

