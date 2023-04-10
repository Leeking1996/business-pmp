# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 21:55
from pydantic import BaseModel, Field


class ProjectState(BaseModel):
    state_name: str = Field(title="阶段名称")
    sort: int = Field(title="排序")


class CreateProjectState(BaseModel):
    template_id: str = Field(title="模版id")
    project_states: list[ProjectState] = Field(title="阶段数据")


class DeleteProjectState(BaseModel):
    template_id: str = Field(title="模版id")
    b_id: str = Field(title="b_id")


class CreateWbs(BaseModel):
    table_file: str = Field(title="字段名称")
    is_true: bool = Field(title="是否选择")
    sort: int = Field(title="排序")


class ProjectPlan(BaseModel):
    """保存项目计划模块整体数据"""
    template_id: str = Field(title="模板id")
    wbs_list: list[CreateWbs] = Field(title="排序")
