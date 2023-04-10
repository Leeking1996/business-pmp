# -*- coding:utf-8 -*-
# Author: lee
# 2023/4/9 20:03
# func: 参数数据
from typing import Optional

from pydantic import BaseModel, Field


class SecondScore(BaseModel):
    """二级选项"""
    name: Optional[str] = Field(title="二级菜单")
    score: Optional[float] = Field(title="分数")


class FirstScore(BaseModel):
    """一级选项"""
    b_id: Optional[str] = Field(title="b_id")
    name: str = Field(title="一级菜单名称")
    score: float = Field(title="分数")
    second_score: list[SecondScore] = Field(title="二级菜单数据")


class CreateScore(BaseModel):
    """创建选项数据"""
    template_id: str = Field(title="模版id")
    score_list: list[FirstScore] = Field(title="一级菜单数据")
