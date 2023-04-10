# -*- coding:utf-8 -*-
# Author: lee
# 2023/3/31 20:27
# func: 实现方法
from sqlalchemy.orm import Session
from utils.gender_snow_flake import gender_snow_flake_id
from domain.team.models import *
from domain.team.schemy import *


async def search_team_optional_file():
    files = TeamOptionalFiled.__table__.columns
    file_list = list()
    for i in files:
        if i.key in ["id", "b_id"]:
            continue
        file_list.append({"table_file": i.key, "table_file_en": i.comment})
    return file_list


async def create_team_optional_file(params: CreateTeamOptionalFile, db: Session):
    """团队表和模板数据做绑定"""
    template_id = params.template_id
    choose_files = params.choose_files
    objects = list()
    flag = False
    try:
        # 根据模板id 先把之前的数据删除掉
        db.query(TeamOptionalFieldTemplate).filter(TeamOptionalFieldTemplate.template_id == template_id).delete()
        for file in choose_files:
            b_id = gender_snow_flake_id()
            objects.append(TeamOptionalFieldTemplate(template_id=template_id, b_id=b_id, table_file=file.table_file,
                                                     table_file_name=file.table_file_en, is_true=file.is_true))
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_team_optional_detail(template_id: str, db: Session):
    """根据模板id查看那些字段已经选择"""
    files = db.query(TeamOptionalFieldTemplate).filter(TeamOptionalFieldTemplate.template_id == template_id).all()
    all_data = [i.to_dict() for i in files]
    return all_data
