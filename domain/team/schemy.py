# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 20:27
from pydantic import BaseModel, Field


class ChooseFiles(BaseModel):
    table_file: str = Field(title="字段")
    table_file_en: str = Field(title="中文名称")
    is_true: bool = Field(title="是否选择")


class CreateTeamOptionalFile(BaseModel):
    template_id: str = Field(title="模版id")
    choose_files: list[ChooseFiles] = Field(title="可选字段")
