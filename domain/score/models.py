# -*- coding:utf-8 -*-
# Author: lee
# 2023/4/8 19:38
# func: 项目定级标准接口
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

from utils.gender_snow_flake import gender_snow_flake_id

from db import Base


class FirstScore(Base):
    """一级选项"""
    __tablename__ = "first_score"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True, index=True)
    b_id = Column(String(65), name="b_id", comment="雪花id", default=gender_snow_flake_id())
    name = Column(String(128), name="name", comment="选项名称")
    template_id = Column(String(128), name="template_id", comment="模版id")
    score = Column(Float, name="score", comment="分数")
    children = relationship("SecondScore")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "name": self.name,
            "template_id": self.template_id,
            "score": self.score
        }


class SecondScore(Base):
    """定级二级选择，一对多"""
    __tablename__ = "second_score"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True, index=True)
    b_id = Column(String(65), name="b_id", comment="雪花id", default=gender_snow_flake_id())
    name = Column(String(128), name="name", comment="名称")
    score = Column(Float, name="score", comment="分数")
    first_score_id = Column(String(128), ForeignKey("first_score.b_id"))
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {"b_id": self.b_id,
                "name": self.name,
                "score": self.score,
                "first_score_id": self.first_score_id
                }
