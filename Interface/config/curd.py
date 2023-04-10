# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 23:01
# Func: 方法实现区
import time

from sqlalchemy.orm import Session
from domain.config.models import *
from domain.config.schemy import UpdateSonState, OptionalFileList
from domain.project_plan.models import *
from utils.config import config_paging
from utils.encryption import MyDESCrypt
from utils.gender_snow_flake import gender_snow_flake_id
# 不能删除，创建模板时，通过数据进行展示
from domain.team.models import *


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
        smp_id = updateSmp.pop("id")
        update_smp_dict = dict()
        for k, v in updateSmp.items():
            if v:
                update_smp_dict.update({k: v})
        db.query(SysPostManagement).filter(SysPostManagement.id == smp_id).update(update_smp_dict)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_smp(deleteSmp: dict, db: Session):
    ids = deleteSmp.get("id")
    flag = False
    try:
        db.query(SysPostManagement).filter(SysPostManagement.id.in_(ids)).update({"is_delete": True})
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
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_sys_dict(searchSysDict: dict, db: Session):
    # 查询字典
    flag = False
    data = None
    q_filter = db.query(SysDict).filter(SysDict.is_delete.is_(False), SysDict.dict_state.is_(True))
    try:
        if searchSysDict.get("dict_name"):
            q_filter = q_filter.filter(SysDict.dict_name.like(F"%{searchSysDict.get('dict_name')}%"))
        if searchSysDict.get("dict_type"):
            q_filter = q_filter.filter(SysDict.dict_type.like(F"%{searchSysDict.get('dict_type')}%"))
        if searchSysDict.get("dict_state"):
            q_filter = q_filter.filter(SysDict.dict_state.is_(searchSysDict.get("dict_state")))
        data = config_paging(q_filter, searchSysDict.get("page"), searchSysDict.get("size"))
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data


async def update_sys_dict(updateSysDict: dict, db: Session):
    new_update_sys_dict = dict()
    id = updateSysDict.pop("id")
    flag = False
    for k, v in updateSysDict.items():
        if v:
            new_update_sys_dict.update({k: v})
    try:
        db.query(SysDict).filter(SysDict.id == id).update(new_update_sys_dict)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_sys_dict(deleteSysDict: dict, db: Session):
    ids = deleteSysDict.get("ids")

    db.query(SysDict).filter(SysDict.id.in_(ids)).update({"is_delete": True})
    db.commit()
    return True


async def search_sys_dict_value(searchSysDictValue: dict, db: Session):
    flag = False
    all_data = None
    try:
        sys_dict_id = searchSysDictValue.get("sys_dict_id")
        q_filter = db.query(SysDictValue).filter(SysDictValue.sys_dict_id == sys_dict_id,
                                                 SysDictValue.is_delete.is_(False))
        if searchSysDictValue.get("dict_label"):
            q_filter = q_filter.filter(SysDictValue.data_label.like(F"{searchSysDictValue.get('dict_label')}"))
        if searchSysDictValue.get("dict_state"):
            q_filter = q_filter.filter(SysDictValue.value_state.is_(searchSysDictValue.get('dict_state')))
        all_data = [i.to_dict() for i in q_filter.order_by(SysDictValue.sort).all()]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, all_data


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
                new_update_sys_dict_value.update({k: v})
        db.query(SysDictValue).filter(SysDictValue.id == id).update(new_update_sys_dict_value)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_sys_dict_value(deleteSysDictValue: dict, db: Session):
    ids = deleteSysDictValue.get("ids")
    db.query(SysDictValue).filter(SysDictValue.id.in_(ids)).update({"is_delete": True})
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
    flag = False
    id = updateMenu.pop("id")
    try:
        for k, v in updateMenu.items():
            if v:
                new_update_menu.update({k: v})
        db.query(SysMenu).filter(SysMenu.id == id).update(new_update_menu)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_menu(searchMenu: dict, db: Session):
    flag = False,
    all_menu_data = None
    try:
        all_data = db.query(SysMenu).filter(SysMenu.is_delete.is_(False), SysMenu.parent_id.is_(None)).all()
        all_menu_data = list()
        for one_menu in all_data:
            children = menu_recursion(one_menu.id, one_menu.menuData)
            one_menu_dict = one_menu.to_dict()
            one_menu_dict.update({"children": children})
            all_menu_data.append(one_menu_dict)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, all_menu_data


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
    db.query(SysMenu).filter(SysMenu.id == deleteMenu.get("id")).update({SysMenu.is_delete: True})
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
        menu_ids = updateRole.pop("menus")
        role_id = updateRole.pop("role_id")
        db.query(SysRole).filter(SysRole.id == role_id).update(updateRole)
        db.query(SysRoleRelationMenu).filter(SysRoleRelationMenu.sys_role_id == role_id).delete()
        objects = [SysRoleRelationMenu(sys_role_id=role_id, sys_menu_id=i) for i in menu_ids if i]
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
        db.query(SysRole).filter(SysRole.id.in_(deleteRole.role_id)).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_role(db: Session):
    flag = False
    return_data = list()
    try:
        role_data = db.query(SysRole).filter(SysRole.is_delete.is_(False)).all()
        # 根据角色id 查询菜单数据
        for i in role_data:
            role_dict = i.to_dict()
            role_id = role_dict.get("id")
            menus = db.query(SysMenu, SysRoleRelationMenu).join(SysMenu,
                                                                SysMenu.id == SysRoleRelationMenu.sys_menu_id).filter(
                SysRoleRelationMenu.sys_role_id == role_id).all()
            if menus:
                role_dict.update({"menus": [i.SysMenu.to_dict() for i in menus]})
            else:
                role_dict.update({"menus": []})
            return_data.append(role_dict)
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, return_data


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


async def delete_brod_heading(b_ids, db: Session):
    flag = False
    try:
        db.query(BrodHeading).filter(BrodHeading.b_id.in_(b_ids.b_ids)).update({"is_delete": True})
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
        # 循环查询小类数据
        data_list = list()
        for i in q_filter.all():
            b_id = i.b_id
            sub_class = db.query(SubClass).filter(SubClass.brod_heading_id == b_id, SubClass.is_delete.is_(False)).all()
            sub_class_list = [i.to_dict() for i in sub_class]
            brod_class_dict = i.to_dict()
            brod_class_dict.update({"sub_class_list": sub_class_list})
            data_list.append(brod_class_dict)
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


async def delete_sub_class(b_ids, db: Session):
    flag = False
    try:
        print(b_ids, "b_ids")
        db.query(SubClass).filter(SubClass.b_id.in_(b_ids.b_ids)).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_value_type(db: Session):
    value_data = db.query(ValueType).all()
    return [i.to_dict() for i in value_data]


# 创建可选模版函数
async def create_optional_module(params: dict, db: Session):
    flag = False
    try:
        b_id = gender_snow_flake_id()
        create_module_dict = {"name": params.get("name"), "name_en": params.get("name_en"), "b_id": b_id}
        add_ser = SysOptionalModule(**create_module_dict)
        db.add(add_ser)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def delete_optional_module(params, db: Session):
    flag = False
    try:
        db.query(SysOptionalModule).filter(SysOptionalModule.b_id.in_(params.b_ids)).update({"is_delete": True})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def update_optional_module(params: dict, db: Session):
    flag = False
    try:
        b_id = params.pop("b_id")
        new_update_dict = dict()
        for k, v in params.items():
            if v:
                new_update_dict.update({k: v})
        db.query(SysOptionalModule).filter(SysOptionalModule.b_id == b_id).update(new_update_dict)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_optional_module(db: Session):
    flag = False
    data = None
    try:
        all_data = db.query(SysOptionalModule).filter(SysOptionalModule.is_delete.is_(False)).all()
        data = [i.to_dict() for i in all_data]
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data


# 创建模板
async def create_template(params: dict, db: Session):
    """创建模板， 拿到数据，更新到数据中，配置进行写死"""
    flag = False
    template_b_id = gender_snow_flake_id()
    try:
        add_ser = SysTemplate(**{"b_id": template_b_id, "name": params.get("name")})
        db.add(add_ser)
        # 获取子模块，保存到数据中，保存到数据中
        son_modules = db.query(SysOptionalModule).all()
        objects = list()
        for son_module in son_modules:
            son_module_b_id = gender_snow_flake_id()
            objects.append(
                SysOptionalModuleTemplate(b_id=son_module_b_id, optional_module_id=son_module.b_id, is_true=False,
                                          template_b_id=template_b_id))
            # 可选字段和模版数据做绑定
            optional_table = son_module.optional_table
            if not optional_table:
                continue
            optional_table_name = globals().get(optional_table)
            files = optional_table_name.__table__.columns
            for file in files:
                if file.key in ["id", "b_id"]:
                    continue
                # 保存数据到可选字段表中
                objects.append(
                    OptionalField(file_name=file.comment, table_file=file.key, table_name=optional_table,
                                  is_true=False, template_id=template_b_id, module_id=son_module.b_id,
                                  b_id=gender_snow_flake_id()))
        # 创建模板时，同时创建项目阶段
        project_states = params.get("project_states")
        for project_state in project_states:
            objects.append(ProjectState(b_id=gender_snow_flake_id(), state_name=project_state.get("state_name"),
                                        template_id=template_b_id, sort=project_state.get("sort")))
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)

    return flag, template_b_id


async def search_template_details(template_id: str, db: Session):
    """查看模板详情，查看可选字段名称和id，前端通过调用模版的名称进行数据的查询，通过可选模版的数据进行数据的展示"""
    flag = False
    data = list()
    try:
        all_data = db.query(SysOptionalModule.b_id,
                            SysOptionalModuleTemplate.is_true,
                            SysOptionalModuleTemplate.is_change,
                            SysOptionalModule.name).join(SysOptionalModule,
                                                         SysOptionalModuleTemplate.optional_module_id == SysOptionalModule.b_id).filter(
            SysOptionalModuleTemplate.template_b_id == template_id).all()

        for one_data in all_data:
            # TODO 判断当前登录人是不是管理员权限， 如果是管理员权限，则需要修改is_change 是能够被修改的

            data.append({"b_id": one_data.b_id, "is_true": one_data.is_true, "name": one_data.name,
                         "is_change": one_data.is_change})

        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag, data


async def search_template(db: Session):
    all_data = db.query(SysTemplate).filter(SysTemplate.is_delete.is_(False)).all()
    objects = list()
    for i in all_data:
        b_id = i.b_id
        states = db.query(ProjectState).filter(ProjectState.template_id == b_id,
                                               ProjectState.is_delete.is_(False)).all()
        data = i.to_dict()
        data.update({"project_states": [i.to_dict() for i in states]})
        objects.append(data)

    return objects


async def delete_template(params, db: Session):
    db.query(SysTemplate).filter(SysTemplate.b_id.in_(params.b_ids)).update({"is_delete": True})
    db.commit()
    return True


async def update_template_son_module_state(params: UpdateSonState, db: Session):
    """根据模板和自模块的b_id 修改数据是否展示"""
    flag = False
    try:
        db.query(SysOptionalModuleTemplate).filter(SysOptionalModuleTemplate.template_b_id == params.template_id,
                                                   SysOptionalModuleTemplate.optional_module_id == params.module_id).update(
            {"is_true": params.is_true, "is_change": params.is_change})
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag


async def search_project_optional_field(template_id: str, module_id, db: Session):
    """返回可选字段"""
    all_data = list()
    # 查看自定义字段属性
    choose_data = db.query(ChooseFiled, ValueType.type_name).join(
        ValueType,
        ValueType.id == ChooseFiled.file_type).filter(
        ChooseFiled.template_id == template_id,
        ChooseFiled.module_id == module_id).all()

    for one_choose in choose_data:
        all_data.append(
            {"file_name": one_choose.ChooseFiled.file_name, "file_name_en": one_choose.ChooseFiled.file_name_en,
             "file_type": one_choose.type_name, "custom_field": True, "is_true": True,
             "template_id": one_choose.ChooseFiled.template_id, "module_id": one_choose.ChooseFiled.module_id
             })
    # 根据模板id查看可选字段
    optionals = db.query(OptionalField).filter(OptionalField.template_id == template_id,
                                               OptionalField.module_id == module_id).all()
    for i in optionals:
        one_optional = i.to_dict()
        one_optional.update({"custom_field": False})
        all_data.append(one_optional)
    return all_data


async def update_optional_file(data: OptionalFileList, db: Session):
    """批量更新可选字段状态"""
    flag = False
    try:
        template_id = data.template_id
        module_id = data.module_id
        optional_list = data.optional_list
        choose_files = data.choose_files

        db.query(OptionalField).filter(OptionalField.template_id == template_id,
                                       OptionalField.module_id == module_id).update({"is_true": False})
        is_true_ids = [i.b_id for i in optional_list if i.is_true]
        db.query(OptionalField).filter(OptionalField.b_id.in_(is_true_ids)).update({"is_true": True})
        # 自定义字段属性
        objects = list()
        db.query(ChooseFiled).filter(ChooseFiled.template_id == template_id, ChooseFiled.module_id == module_id).update(
            {"is_delete": True})
        for one_choose in choose_files:
            b_id = gender_snow_flake_id()
            objects.append(ChooseFiled(b_id=b_id, template_id=template_id, module_id=module_id,
                                       file_name=one_choose.file_name, file_name_en=one_choose.file_name_en,
                                       file_type=one_choose.file_type))
        db.bulk_save_objects(objects)
        db.commit()
        db.flush()
        flag = True
    except Exception as e:
        print(e)

    finally:
        return flag


async def update_template(updateTemplate, db: Session):
    """更新模板"""
    flag = False
    template_id = updateTemplate.template_id
    objects = list()
    try:
        db.query(SysTemplate).filter(SysTemplate.b_id == template_id).update({"name": updateTemplate.name})
        db.query(ProjectState).filter(ProjectState.template_id == template_id).update({"is_delete": True})

        for one_project_state in updateTemplate.project_states:
            b_id = gender_snow_flake_id()
            objects.append(ProjectState(b_id=b_id, template_id=template_id, state_name=one_project_state.state_name,
                                        sort=one_project_state.sort))
        db.bulk_save_objects(objects)
        db.commit()
        flag = True
    except Exception as e:
        print(e)
    finally:
        return flag
