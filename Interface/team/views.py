# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 20:27
from sqlalchemy.orm import Session

from domain.team.schemy import *
from fastapi import APIRouter, Depends
from utils import return_response
from Interface.team import curd
from db.content_db import get_db_content

router = APIRouter(tags=["团队配置"], prefix="/config")


@router.get("/search/team/optional/file", summary="获取可选字段数据")
async def search_file_data():
    judge_data = await curd.search_team_optional_file()
    return return_response.success(judge_data)


@router.post("/create/team/optional", summary="团队可选字段和模板做绑定")
async def create_team_optional(createTeamOptionalFile: CreateTeamOptionalFile, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_team_optional_file(createTeamOptionalFile, db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.get("/search/team/optional/detail/{template_id}", summary="查看详情")
async def search_team_optional_files(template_id: str, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_team_optional_detail(template_id, db)
    return return_response.success(judge_data)
