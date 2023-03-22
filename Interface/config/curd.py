# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 23:01
# Func: 方法实现区
import math

from sqlalchemy.orm import Session
from domain.config.models import *
from domain.config.schemy import SearchProjectState
from utils.config import config_paging
from utils.encryption import MyDESCrypt
from utils.gender_snow_flake import gender_snow_flake_id


async def create_department(createDepartment, db: Session):
    """创建部门"""
    try:
        add_ser = SysDepartment(**createDepartment)
        db.add(add_ser)
        db.commit()
        db.refresh(add_ser)
        return True
    except Exception as e:
        print(e, "e")
        return False


async def search_department(searchDepartment: dict, db: Session):
    q_filter = db.query(SysDepartment).filter(SysDepartment.parent_id.is_(None))
    return_data = list()
    try:
        # if searchDepartment.get("department_name"):
        #     q_filter = q_filter.filter(
        #         SysDepartment.department_name.like(F"%{searchDepartment.get('department_name')}%"))
        # if searchDepartment.get("department_state"):
        #     q_filter = q_filter.filter(SysDepartment.department_state.is_(searchDepartment.get("department_state")))
        all_data = q_filter.filter(SysDepartment.is_delete.is_(False)).all()
        for i in all_data:
            one_department_dict = i.to_dict()
            children = recurrence_department(i.id, i.departmentData)
            if children:
                one_department_dict.update({"children": children})
            return_data.append(one_department_dict)

    except Exception as e:
        print(e)
    finally:
        return return_data


def recurrence_department(parent_id, data):
    children = list()
    for one_department in data:
        if parent_id == one_department.parent_id:
            one_department_dict = one_department.to_dict()
            data_list = recurrence_department(one_department.id, one_department.departmentData)
            if data_list:
                one_department_dict.update({"children": data_list})
            children.append(one_department_dict)
    return children


async def update_department(updateDepartment: dict, db: Session):
    # 更新部门操作
    new_update_data = dict()
    id = updateDepartment.pop("id")

    for k, v in updateDepartment.items():
        if v:
            new_update_data.update({k: v})
    try:
        db.query(SysDepartment).filter(SysDepartment.id == id).update(new_update_data)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False


async def delete_department(deleteDepartment: dict, db: Session):
    # 删除部门
    ids = deleteDepartment.get("ids")
    try:
        if len(ids) != 0:
            db.query(SysDepartment).filter(SysDepartment.id.in_(ids)).update({"is_delete": True})
            db.commit()
            return True
    except Exception as e:
        print(e)
        return False


async def create_person(createPerson: dict, db: Session):
    flag = False
    password = createPerson.get("password")
    # 进行密码加密
    encrypt_password = MyDESCrypt().encrypt(password)
    createPerson["password"] = encrypt_password
    # 工号是唯一的，是否需要判断数据
    person_num = createPerson.get("person_num")
    judge_existence = db.query(SysUser).filter(SysUser.person_num == person_num).count()
    if judge_existence:
        return False
    try:
        add_ser = SysUser(**createPerson)
        db.add(add_ser)
        db.commit()
        db.refresh(add_ser)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_person(searchPerson: dict, db: Session):
    # 查询人员数据
    q_filter = db.query(SysUser).filter(SysUser.is_delete.is_(False))
    if searchPerson.get("person_name"):
        q_filter = q_filter.filter(SysUser.person_name.like((F"%{searchPerson.get('person_name')}%")))
    if searchPerson.get("person_code"):
        q_filter = q_filter.filter(SysUser.person_num.like(F"%{searchPerson.get('person_code')}%"))
    if searchPerson.get("department_id"):
        q_filter = q_filter.filter(SysUser.department_id == searchPerson.get("department_id"))
    if searchPerson.get("person_state"):
        q_filter = q_filter.filter(SysUser.person_state.is_(searchPerson.get("person_state")))
    if searchPerson.get("person_id"):
        q_filter = q_filter.filter(SysUser.id == searchPerson.get("id"))
    # 获取全部页码
    return config_paging(q_filter, searchPerson.get("page"), searchPerson.get("size"))


async def update_person(updatePerson: dict, db: Session):
    update_person_dict = dict()
    flag = False
    try:
        if updatePerson.get("password"):
            # 如果密码为真，则需要提取出来并把数据进行加密
            encrypt_password = MyDESCrypt().encrypt(updatePerson.get("password"))
            update_person_dict.update({"password": encrypt_password})
        del updatePerson["password"]
        person_id = updatePerson.pop("person_id")
        db.query(SysUser).filter(SysUser.id == person_id).update(updatePerson)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    return flag


async def delete_person(deletePerson: dict, db: Session):
    db.query(SysUser).filter(SysUser.id.in_(deletePerson.get("person_id"))).update({"is_delete": True})
    db.commit()
    return True


async def create_smp(createSmp: dict, db: Session):
    # 新增岗位管理
    flag = False
    try:
        add_ser = SysPostManagement(**createSmp)
        db.add(add_ser)
        db.commit()
        db.refresh(add_ser)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_smp(searchSmp: dict, db: Session):
    # 查询岗位管理
    flag = False
    return_data = None
    try:
        q_filter = db.query(SysPostManagement).filter(SysPostManagement.is_delete.is_(False))
        if searchSmp.get("post_management_name"):
            q_filter = q_filter.filter(
                SysPostManagement.post_management_name.like(F"%{searchSmp.get('post_management_name')}%"))
        if searchSmp.get("post_management_code"):
            q_filter = q_filter.filter(
                SysPostManagement.post_management_code.like(F"%{searchSmp.get('post_management_code')}%"))
        if searchSmp.get("state"):
            q_filter = q_filter.filter(SysPostManagement.state.is_(searchSmp.get("state")))
        all_data = q_filter.order_by(SysPostManagement.index).all()
        flag = True
        return_data = [i.to_dict() for i in all_data]
    except Exception as e:
        print(e)
    finally:
        return flag, return_data


async def update_smp(updateSmp: dict, db: Session):
    # 岗位更新
    flag = False
    try:
        smp_id = updateSmp.get("id")
        update_smp_dict = dict()
        del updateSmp["id"]
        for k, v in updateSmp:
            if v:
                update_smp_dict.update({k, v})
        db.query(SysPostManagement).filter(SysPostManagement.id.is_(smp_id)).update(update_smp_dict)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_smp(deleteSmp: dict, db: Session):
    id = deleteSmp.get("id")
    flag = False
    try:
        db.query(SysPostManagement).filter(SysPostManagement.id == id).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    return flag


async def create_sys_dict(createSysDict: dict, db: Session):
    flag = False
    try:
        add_ser = SysDict(**createSysDict)
        db.add(add_ser)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_sys_dict(searchSysDict: dict, db: Session):
    # 查询字典
    q_filter = db.query(SysDict).filter(SysDict.is_delete.is_(False), SysDict.dict_state.is_(True))
    try:
        if searchSysDict.get("dict_name"):
            q_filter = q_filter.filter(SysDict.dict_name.like(F"%{searchSysDict.get('dict_name')}%"))
        if searchSysDict.get("dict_type"):
            q_filter = q_filter.filter(SysDict.dict_type.like(F"%{searchSysDict.get('dict_type')}%"))
        if searchSysDict.get("dict_state"):
            q_filter = q_filter.filter(SysDict.dict_state.is_(searchSysDict.get("dict_state")))
        return config_paging(q_filter, searchSysDict.get("page"), searchSysDict.get("size"))
    except Exception as e:
        print(e)
    finally:
        return {}


async def update_sys_dict(updateSysDict: dict, db: Session):
    new_update_sys_dict = dict()
    id = updateSysDict.pop("id")
    flag = False
    for k, v in updateSysDict.items():
        if v:
            new_update_sys_dict.update({k, v})
    try:
        db.query(SysDict).filter(SysDict.id.is_(id)).update(new_update_sys_dict)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_sys_dict(deleteSysDict: dict, db: Session):
    id = deleteSysDict.get("id")
    db.query(SysDict).filter(SysDict.id.is_(id)).update({SysDict.is_delete: True})
    return True


async def search_sys_dict_value(searchSysDictValue: dict, db: Session):
    parent_id = searchSysDictValue.get("parent_id")
    q_filter = db.query(SysDictValue).filter(SysDictValue.id == parent_id)
    if searchSysDictValue.get("dict_label"):
        q_filter = q_filter.filter(SysDictValue.data_label.like(F"{searchSysDictValue.get('dict_label')}"))
    if searchSysDictValue.get("dict_state"):
        q_filter = q_filter.filter(SysDictValue.value_state.is_(searchSysDictValue.get('dict_state')))
    all_data = [i.to_dict() for i in q_filter.order_by(SysDictValue.sort).all()]
    return all_data


async def create_sys_dict_value(createSysDictValue: dict, db: Session):
    add_ser = SysDictValue(**createSysDictValue)
    db.add(add_ser)
    db.commit()
    db.refresh(add_ser)
    return True


async def update_sys_dict_value(updateSysDictValue: dict, db: Session):
    id = updateSysDictValue.pop("id")
    flag = False
    new_update_sys_dict_value = dict()
    try:
        for k, v in updateSysDictValue.items():
            if v:
                new_update_sys_dict_value.update({k, v})
        db.query(SysDictValue).filter(SysDictValue.id.is_(id)).update(new_update_sys_dict_value)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_sys_dict_value(deleteSysDictValue: dict, db: Session):
    id = deleteSysDictValue.get("id")
    db.query(SysDictValue).filter(SysDictValue.id.is_(id)).update({SysDictValue.is_delete: True})
    db.commit()
    return True


async def create_menu(createMenu: dict, db: Session):
    add_ser = SysMenu(**createMenu)
    db.add(add_ser)
    db.commit()
    db.refresh(add_ser)
    return True


async def update_menu(updateMenu: dict, db: Session):
    new_update_menu = dict()
    # 在此处使用递归，查询数据，第一层是父级，往下进行数据的展示， 是否统一能力进行社保
    flag = False
    id = updateMenu.pop("id")
    try:
        for k, v in updateMenu.items():
            if v:
                new_update_menu.update({k, v})
        db.query(SysMenu).filter(SysMenu.id.is_(id)).update(new_update_menu)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_menu(searchMenu: dict, db: Session):
    all_data = db.query(SysMenu).filter(SysMenu.is_delete.is_(False), SysMenu.parent_id.is_(None)).all()
    all_menu_data = list()
    for one_menu in all_data:
        children = menu_recursion(one_menu.id, one_menu.menuData)
        one_menu_dict = one_menu.to_dict()
        one_menu_dict.update({"children": children})
        all_menu_data.append(one_menu_dict)

    return all_menu_data


def menu_recursion(parent_id, menuData):
    """递归处理菜单数据"""
    children = list()
    for one_menu in menuData:
        if parent_id == one_menu.parent_id:
            one_menu_dict = one_menu.to_dict()
            data_list = menu_recursion(one_menu.id, one_menu.menuData)
            if data_list:
                one_menu_dict.update({"children": data_list})
            children.append(one_menu_dict)
    return children


async def delete_menu(deleteMenu: dict, db: Session):
    db.query(SysMenu).filter(SysMenu.id.is_(deleteMenu.get("id"))).update({SysMenu.is_delete: True})
    db.commit()
    return True


async def create_role(createRole: dict, db: Session):
    flag = False
    try:
        menu_ids = createRole.pop("menu_ids")
        add_ser = SysRole(**createRole)
        db.add(add_ser)
        db.commit()
        id = add_ser.id
        objects = [SysRoleRelationMenu(sys_role_id=id, sys_menu_id=i) for i in menu_ids]
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def update_role(updateRole: dict, db: Session):
    # 获取菜单权限
    flag = False
    try:
        menu_ids = updateRole.pop("menu_ids")
        role_id = updateRole.pop("role_id")
        db.query(SysRole).filter(SysRole.id == role_id).update(updateRole)
        db.query(SysRoleRelationMenu).filter(SysRoleRelationMenu.sys_role_id == role_id).delete()
        objects = [SysRoleRelationMenu(sys_role_id=id, sys_menu_id=i) for i in menu_ids]
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_role(deleteRole, db):
    flag = False
    try:
        db.query(SysRole).filter(SysRole.id == deleteRole.role_id).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_role(db: Session):
    flag = False
    return_data = None
    try:
        role_data = db.query(SysRole).filter(SysRole.is_delete.is_(False)).all()
        return_data = [i.to_dict() for i in role_data]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, return_data


async def create_master_plate(createMasterPlate: dict, db: Session):
    flag = False

    try:
        """先创建模版， 然后在根据数据进行修改"""
        master_plate_name = createMasterPlate.get("name")
        template_properties = createMasterPlate.get("template_properties")
        template_type = createMasterPlate.get("type")
        code = createMasterPlate.get("code")
        b_id = gender_snow_flake_id()
        add_ser = MasterPlate(**{"name": master_plate_name, "b_id": b_id, "template_properties": template_properties,
                                 "type": template_type, "code": code})
        db.add(add_ser)
        master_plate_value = createMasterPlate.get("master_plate_value")
        if master_plate_value:
            objects = [MasterPlateValue(name_en=i.get("name_en"),
                                        name_english=i.get("name_english"),
                                        value_type=i.get("value_type"),
                                        master_plate_id=b_id,
                                        b_id=gender_snow_flake_id()) for i in master_plate_value]
            db.bulk_save_objects(objects)
            db.commit()
        flag = True
    except Exception as e:
        print(e)
    return flag


async def update_master_plate(param, db: Session):
    """创建新的模板，查询是否有项目。如果项目id为真，则需要反向更新项目模板id，
    如果项目模板id为空，则不需要更新项目id"""
    """
    1，更新模板的同时生成历史记录表， 把之前的数据存到log里面， 更新项目表中是否有是历史模板，返回历史表中的b_id
    更新到项目表中，两个字段，一个：是否是历史模板， True， 二：更新模板id 为历史表中的id，模
    
    
    
    """


    flag = False
    try:
        # 根据模板id查询项目ID，如果项目id为空，则直接修改，并且记录到日志表中， 如果有数据，反向修改 项目表中的 模板id
        master_plate_id = param.get("master_plate_id")
        # 根据模板反差项目是否有用着模板id
        master_plate = db.query(MasterPlate).filter(MasterPlate.b_id == master_plate_id).first()
        master_plate_log_id = gender_snow_flake_id()
        is_use_master_plate_project = False
        if is_use_master_plate_project:
            """有项目用着，需要更新数据"""

            pass
        else:
            """没有项目用着,"""
        create_master_plate_log_dict = {"master_plate_id": master_plate.b_id,
                                        "name": master_plate.name,
                                        "b_id": master_plate_log_id,
                                        "platform_code": master_plate.platform_code,
                                        "type": master_plate.type,
                                        "template_properties": master_plate.template_properties}
        add_ser = MasterPlateLog(**create_master_plate_log_dict)
        # 在这快根据模板id进行数据的反查

        db.add(add_ser)
        # 把值表中的数据修改成 日志表中的id
        db.query(MasterPlateValue).filter(MasterPlateValue.master_plate_id == master_plate_id).update(
            {"master_plate_id": master_plate_log_id})

        # 添加数据
        master_plate_value = param.get("master_plate_value")
        if master_plate_value:
            objects = [MasterPlateValue(name_en=i.get("name_en"),
                                        name_english=i.get("name_english"),
                                        value_type=i.get("value_type"),
                                        master_plate_id=master_plate_id,
                                        b_id=gender_snow_flake_id()) for i in master_plate_value]
            db.bulk_save_objects(objects)
        db.query(MasterPlate).filter(MasterPlate.b_id == master_plate_id).update({"name": param.get("name")})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
        db.rollback()

    finally:
        return flag


async def delete_master_plate(param: dict, db: Session):
    db.query(MasterPlate).filter(MasterPlate.b_id == param.get("master_plate_id")).update({"is_delete": True})
    db.commit()
    return True


async def search_master_plate(master_plate_name: None, db: Session):
    """查询模板"""
    q_filter = db.query(MasterPlate).filter(MasterPlate.is_delete.is_(False))
    if master_plate_name:
        q_filter = q_filter.filter(MasterPlate.name.ilike(F"%{master_plate_name}%"))
    all_master_data = q_filter.all()
    all_master_list = [i.to_dict() for i in all_master_data]
    return all_master_list


async def search_history_master_plate(master_plate_id: str, db: Session):
    """查看历史模板数据"""
    history_master_plate_data = db.query(MasterPlateLog).filter(MasterPlateLog.master_plate_id == master_plate_id,
                                                                MasterPlateLog.is_delete.is_(False)).all()
    return [i.to_dict() for i in history_master_plate_data]


async def delete_history_master_plate(deleteMasterHistory: dict, db: Session):
    """删除历史数据"""
    flag = False
    try:
        db.query(MasterPlateLog).filter(MasterPlateLog.b_id == deleteMasterHistory.get("master_plate_id")).update(
            {"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        return flag


async def create_brod_heading(params: dict, db: Session):
    """创建项目大类"""
    flag = False
    b_id = gender_snow_flake_id()
    try:
        params.update({"b_id": b_id})
        add_ser = BrodHeading(**params)
        db.add(add_ser)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    return flag, b_id


async def update_brod_heading(params: dict, db: Session):
    flag = False
    try:
        b_id = params.pop("b_id")
        db.query(BrodHeading).filter(BrodHeading.b_id == b_id).update(params)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_brod_heading(b_id: str, db: Session):
    flag = False
    try:
        db.query(BrodHeading).filter(BrodHeading.b_id == b_id).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_brod_heading(params: dict, db: Session):
    flag = False
    data_list = None
    try:
        q_filter = db.query(BrodHeading).filter(BrodHeading.is_delete.is_(False))
        if params.get("brod_name"):
            q_filter = q_filter.filter(BrodHeading.brod_name.like(F"%{params.get('brod_name')}%"))
        if params.get("brod_chart"):
            q_filter = q_filter.filter(BrodHeading.brod_chart == params.get("brod_chart"))
        data_list = [i.to_dict() for i in q_filter.all()]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data_list


async def create_sub_class(params: dict, db: Session):
    """创建小类"""
    b_id = gender_snow_flake_id()
    flag = False
    try:
        params.update(b_id=b_id)
        add_ser = SubClass(**params)
        db.add(add_ser)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_sub_class(params: dict, db: Session):
    """查询数据"""
    flag = False
    data_list = None
    try:
        q_filter = db.query(SubClass).filter(SubClass.is_delete.is_(False))
        if params.get("sub_class_name"):
            q_filter = q_filter.filter(SubClass.sub_class_name.like(F"%{params.get('sub_class_name')}%"))
        if params.get("sub_class_chart"):
            q_filter = q_filter.filter(SubClass.sub_class_chart == params.get("sub_class_chart"))
        if params.get("brod_heading_id"):
            q_filter = q_filter.filter(SubClass.brod_heading_id == params.get("brod_heading_id"))
        data_list = [i.to_dict() for i in q_filter.all()]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data_list


async def update_sub_class(params: dict, db: Session):
    b_id = params.pop("b_id")
    new_params = dict()
    flag = False
    try:
        for k, v in params.items():
            if v:
                new_params.update({k: v})
        db.query(SubClass).filter(SubClass.b_id == b_id).update(new_params)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_sub_class(b_id: str, db: Session):
    flag = False
    try:
        db.query(SubClass).filter(SubClass.b_id == b_id).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def create_project_state(params: dict, db: Session):
    """创建状态"""
    flag = True
    try:
        b_id = gender_snow_flake_id()
        params.update(b_id=b_id)
        add_ser = ProjectState(**params)
        db.add(add_ser)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_project_state(params: SearchProjectState, db: Session):
    flag = False
    all_data = None
    try:
        q_filter = db.query(ProjectState)
        if params.state_name:
            q_filter = q_filter.filter(ProjectState.state_name.like(F"%{params.state_name}%"))
        if params.template_id:
            q_filter = q_filter.filter(ProjectState.template_id == params.template_id)
        q_filter.order_by(ProjectState.index)
        all_data = [i.to_dict() for i in q_filter.all()]
    except Exception as e:
        print(e)
    finally:
        return flag, all_data


async def update_project_state(params: dict, db: Session):
    flag = False
    new_params = dict()
    try:
        b_id = params.pop("b_id")
        for k, v in params.items():
            if v:
                new_params.update({k: v})
        db.query(ProjectState).filter(ProjectState.b_id == b_id).update(new_params)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_project_state(b_id: str, db: Session):
    db.query(ProjectState).filter(ProjectState.b_id == b_id).update({"is_delete": True})
    db.commit()
    return True


async def search_value_type(db: Session):
    value_data = db.query(ValueType).all()
    return [i.to_dict() for i in value_data]


async def search_optional_field():
    # 去掉字符串第一位是_
    data = [i for i in OptionalTable.__dict__.keys() if i[0] != "_"]
    return data


async def create_optional_log(params: dict, db: Session):
    """保存数据"""
    flag = False
    try:
        template_id = params.get("template_id")
        optionals = params.get("optionals")
        data = [OptionalLog(colum=i.get("colum"), is_true=i.get("is_true"), template_id=template_id) for i in optionals]
        db.bulk_save_objects(data)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_optional_log(params: str, db):
    data = db.query(OptionalLog).filter(OptionalLog.template_id == params).all()
    return [{"id": i.id, "template_id": i.template_id, "colum": i.colum, "is_true": i.is_true} for i in data]
