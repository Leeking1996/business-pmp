# -*- coding:utf-8 -*-
# Author: lee
# 2023/4/9 20:25
# func: 方法类实现
from sqlalchemy.orm import Session

from domain.score.models import FirstScore, SecondScore
from utils.gender_snow_flake import gender_snow_flake_id


async def create_score(createScore, db: Session):
    """创建项目定级，合并数据"""
    template_id = createScore.template_id
    # 获取一级菜单
    flag = False
    score_lists = createScore.score_list
    objects = list()
    try:
        for one_score in score_lists:
            first_b_id = gender_snow_flake_id()
            first_name = one_score.name
            first_score = one_score.score
            second_list = one_score.second_score

            objects.append(FirstScore(b_id=first_b_id,
                                      name=first_name,
                                      score=first_score,
                                      template_id=template_id))
            [objects.append(SecondScore(b_id=gender_snow_flake_id(),
                                        name=i.name,
                                        score=i.score,
                                        first_score_id=first_b_id)) for i in second_list]
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def update_score(createScore, db):
    flag = False
    template_id = createScore.template_id
    score_list = createScore.score_list
    try:
        db.query(FirstScore).filter(FirstScore.template_id == template_id).update({"is_delete": True})
        # 获取二级菜单数据
        first_score_b_id = [i.b_id for i in score_list]
        db.query(SecondScore).filter(SecondScore.first_score_id.in_(first_score_b_id)).update({"is_delete": True})
        objects = list()
        for one_score in score_list:
            first_b_id = gender_snow_flake_id()
            first_name = one_score.name
            first_score = one_score.score
            second_list = one_score.second_score
            objects.append(FirstScore(b_id=first_b_id,
                                      name=first_name,
                                      score=first_score,
                                      template_id=template_id))
            [objects.append(SecondScore(b_id=gender_snow_flake_id(),
                                        name=i.name,
                                        score=i.score,
                                        first_score_id=first_b_id)) for i in second_list]
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_score(template_id, db):
    """查询数据一对多"""
    data = db.query(FirstScore).filter(FirstScore.template_id == template_id,
                                       FirstScore.is_delete.is_(False)).all()
    objects = list()
    flag = False
    try:
        for i in data:
            one_data = i.to_dict()
            one_data.update({"children": [i.to_dict() for i in i.children]})
            objects.append(one_data)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, objects


def delete(template_id, db):
    db.query(FirstScore).filter(FirstScore.template_id == template_id).delete()
    db.commit()

    return True
