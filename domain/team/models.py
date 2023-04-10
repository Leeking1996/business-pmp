# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 20:27
from sqlalchemy import Column, Integer, String, Boolean

from db import Base


class TeamOptionalFiled(Base):
    __tablename__ = "team_optional_filed"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    b_id = Column(String(128), name="b_id", comment="雪花id")
    code = Column(String(128), name="code", comment="登录账号")
    leader = Column(String(128), name="leader", comment="上级")
    leader_code = Column(String(64), name="leader_code", comment="上级领导账号")
    office = Column(String(128), name="office", comment="科室")
    department = Column(String(128), name="department", comment="部门")
    unit = Column(String(64), name="unit", comment="单位")
    level = Column(Integer, name="level", comment="职级")
    type = Column(Integer, name="type", comment="类型")