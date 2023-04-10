# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 21:55
from sqlalchemy import Column, Integer, String, Boolean, DOUBLE, Float

from db import Base


class ProjectState(Base):
    """项目阶段"""
    __tablename__ = "project_state"
    id = Column(Integer, name="id", autoincrement=True, primary_key=True, index=True, nullable=False)
    b_id = Column(String(80), name="b_id", comment="雪花id")
    state_name = Column(String(64), name="state_name", comment="阶段名称")
    template_id = Column(String(80), name="template_id", comment="模版id")
    sort = Column(Integer, name="sort", comment="排序")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "state_name": self.state_name,
            "sort": self.sort
        }


class Wbs(Base):
    __tablename__ = "wbs"
    id = Column(Integer, name="id", autoincrement=True, primary_key=True, index=True, nullable=False)
    b_id = Column(String(80), name="b_id", comment="雪花id")
    task_name = Column(String(128), name="task_name", comment="任务名称")
    person_liable = Column(String(128), name="person_liable", comment="责任人")
    state = Column(Integer, name="state", comment="任务状态")
    rate = Column(Integer, name="rate", comment="任务进度")
    duration_ratio = Column(DOUBLE, name="duration_ratio", comment="工期比")
    healthy = Column(Integer, name="healthy", comment="任务健康状态")
    estimate_start_time = Column(String(30), name="estimate_start_time", comment="预计开始时间")
    estimate_end_time = Column(String(30), name="estimate_end_time", comment="预计结束时间")
    estimate_all_day = Column(Float, name="estimate_all_day", comment="预计投入人天")
    reality_start_time = Column(String(30), name="reality_start_time", comment="实际开始时间")
    reality_end_time = Column(String(30), name="reality_end_time", comment="实际结束时间")
    reality_all_day = Column(Float, name="reality_all_day", comment="实际投入人天")
    move_about = Column(String(256), name="move_about", comment="前置活动")
    milepost = Column(Boolean, name="milepost", comment="是否是里程碑", default=False)
    deliverables = Column(Boolean, name="deliverables", comment="是否有交付物", default=False)
    is_delete = Column(Boolean, name="is_delete", comment="是否删除")
