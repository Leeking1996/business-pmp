# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 21:53
# func: 实现方法文件
from sqlalchemy.orm import Session
from utils.gender_snow_flake import gender_snow_flake_id
from domain.project_plan.models import ProjectState, Wbs
from domain.project_plan.schemy import *


async def create_project_state(params: CreateProjectState, db: Session):
    flag = False
    objects = list()
    try:
        project_states = params.project_states
        for project_state in project_states:
            b_id = gender_snow_flake_id()
            objects.append(ProjectState(b_id=b_id, template_id=params.template_id, state_name=project_state.state_name,
                                        sort=project_state.sort))
        db.bulk_save_objects(objects)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_project_state(template_id: str, db: Session):
    """根据id查询阶段"""
    flag = False
    data = None
    try:
        project_states = db.query(ProjectState).filter(ProjectState.template_id == template_id,
                                                       ProjectState.is_delete.is_(False)).all()
        data = [i.to_dict() for i in project_states]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data


async def delete_project_state(params: DeleteProjectState, db: Session):
    db.query(ProjectState).filter(ProjectState.b_id == params.b_id).update({"is_delete": True})
    db.commit()
    return True


async def search_wbs_file():
    """查看wbs表字段名称"""
    files = Wbs.__table__.columns
    files_list = list()
    for i in files:
        if i.key in ["b_id", "is_delete"]:
            continue
        files_list.append({"table_file": i.key, "table_name": i.comment})
    return files_list


async def create_project_plan(params: ProjectPlan, db: Session):
    """创建整体模板"""
    flag = False
    objects = list()
    try:
        template_id = params.template_id
        wbs_list = params.wbs_list
        for i in wbs_list:
            b_id = gender_snow_flake_id()
            objects.append(
                ProjectWbsTemplate(b_id=b_id, template_id=template_id, table_file=i.table_file, is_true=i.is_true,
                                   sort=i.sort))

        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag
