# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 23:01
# Func: 方法实现区
import math

from sqlalchemy.orm import Session
from domain.config.models import *
from utils.config import config_paging
from utils.encryption import MyDESCrypt


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
    q_filter = db.query(SysDepartment)
    return_data = list()
    try:
        if searchDepartment.get("department_name"):
            q_filter = q_filter.filter(
                SysDepartment.department_name.like(F"%{searchDepartment.get('department_name')}%"))
        if searchDepartment.get("department_state"):
            q_filter = q_filter.filter(SysDepartment.department_state.is_(searchDepartment.get("department_state")))
        all_data = q_filter.filter(SysDepartment.is_delete.is_(False)).all()
        for i in all_data:
            return_data.append(i.to_dict())
    except Exception as e:
        print(e)
    finally:
        return return_data


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
        q_filter = q_filter.like(F"%{searchPerson.get('person_name')}%")
    if searchPerson.get("person_code"):
        q_filter = q_filter.like(F"%{searchPerson.get('person_code')}%")
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
        for k, v in updatePerson.items():
            if v:
                update_person_dict.update({k, v})
        db.query(SysUser).filter(SysUser.id == person_id).update(update_person)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    return flag


async def delete_person(deletePerson: dict, db: Session):
    db.query(SysUser).filter(SysUser.id == deletePerson.get("person_id")).update({"is_delete": True})
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
    q_filter = db.query(SysPostManagement).filter(SysPostManagement.is_delete.is_(False))
    if searchSmp.get("post_management_name"):
        q_filter = q_filter.filter(SysPostManagement.like(F"%{searchSmp.get('post_management_name')}%"))
    if searchSmp.get("post_management_code"):
        q_filter = q_filter.filter(
            SysPostManagement.post_management_code.like(F"%{searchSmp.get('post_management_code')}%"))
    if searchSmp.get("state"):
        q_filter = q_filter.filter(SysPostManagement.state.is_(searchSmp.get("state")))
    all_data = q_filter.order_by(SysPostManagement.index).all()
    return [i.to_dict() for i in all_data]


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
