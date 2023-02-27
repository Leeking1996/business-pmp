# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 22:57
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.gender_snow_flake import gender_snow_flake_id
from db.content_db import get_db_content
from Interface.config import curd
from domain.config.schemy import *
from utils import return_response

router = APIRouter(tags=["系统配置接口"], prefix="/config")


@router.get("/search/snow/id", summary="获取雪花id")
async def search_snow_flake_id(datacenter_id: Optional[int], worker_id: Optional[int], sequence: Optional[int]):
    """
       初始化
       :param datacenter_id: 数据中心（机器区域）ID
       :param worker_id: 机器ID
       :param sequence: 其实序号
       """
    return gender_snow_flake_id(datacenter_id, worker_id, sequence)


@router.post("/create/department", summary="创建部门")
async def create_department(createDepartment: CreateDepartment, db: Session = Depends(get_db_content)):
    """创建部门"""
    judge_data = await curd.create_department(createDepartment.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/department", summary="查询部门")
async def search_department(searchDepartment: SearchDepartment, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_department(searchDepartment.dict(), db)
    return return_response.success(judge_data)


@router.put("/update/department", summary="修改部门")
async def update_department(updateDepartment: UpdateDepartment, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_department(updateDepartment.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/department", summary="删除部门")
async def delete_update(deleteDepartment: DeleteDepartment, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_department(deleteDepartment.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/create/person", summary="创建用户")
async def create_person(createPerson: CreatePerson, db: Session = Depends(get_db_content)):
    # 创建用户
    judge_data = await curd.create_person(createPerson.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error(message="添加失败，账号已经存在")


@router.post("/search/person", summary="查询用户")
async def search_person(searchPerson: SearchPerson, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_person(searchPerson.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.put("/update/person", summary="更新用户")
async def update_person(updatePerson: UpdatePerson, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_person(updatePerson.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/person", summary="删除用户")
async def delete_person(deletePerson: DeletePerson, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_person(deletePerson.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/create/spm", summary="新增岗位")
async def create_spm(createSpm: CreateSpm, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_smp(createSpm.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/spm", summary="查询岗位")
async def search_spm(searchSmp: SearchSmp, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_smp(searchSmp.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.put("/update/spm", summary="更新岗位")
async def update_spm(updateSmp: UpdateSmp, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_smp(updateSmp.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/delete/smp", summary="删除岗位")
async def delete_smp(deleteSmp: DeleteSmp, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_smp(deleteSmp.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/create/sys_dict", summary="创建字典")
async def create_sys_dict(createSysDict: CreateSysDict, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_sys_dict(createSysDict.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/sys_dict", summary="查询字典")
async def search_sys_dict(searchSysDict: SearchSysDict, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_sys_dict(searchSysDict.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.post("/update/sys_dict", summary="修改字典")
async def update_sys_dict(updateSysDict: UpdateSysDict, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_sys_dict(updateSysDict.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/sys_dict", summary="删除字典")
async def delete_sys_dict(deleteSysDict: DeleteSysDict, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_sys_dict(deleteSysDict.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/sys_dict_value", summary="查询子集字典")
async def search_sys_dict_value(searchSysDictValue: SearchSysDictValue, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_sys_dict_value(searchSysDictValue.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.post("/create/sys_dict_value", summary="创建子集")
async def create_sys_dict_value(createSysDictValue: CreateSysDictValue, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_sys_dict_value(createSysDictValue.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.put("/update/sys_dict_value", summary="更新子集")
async def update_sys_dict_value(updateSysDictValue: UpdateSysDictVale, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_sys_dict_value(updateSysDictValue.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.delete("/delete/sys_dict_value", summary="删除子集")
async def delete_sys_dict_value(deleteSysDictValue: DeleteSysDict, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_sys_dict_value(deleteSysDictValue.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.post("/create/menu", summary="添加菜单")
async def create_menu(createMenu: CreateMenu, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_menu(createMenu.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.put("/update/menu", summary="修改菜单")
async def update_menu(updateMenu: UpdateMenu, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_menu(updateMenu.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/menu", summary="查看菜单")
async def search_menu(searchMenu: SearchMenu, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_menu(searchMenu.dict(), db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.delete("/delete/menu", summary="删除菜单")
async def delete_menu(deleteMenu: DeleteMenu, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_menu(deleteMenu.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/create/role", summary="新增角色")
async def create_role(createRole: CreateRole, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_role(createRole.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/create/mater/plate", summary="增加模版")
async def create_master_plate(createMasterPlate: CreateMasterPlate, db: Session = Depends(get_db_content)):
    """增加模版"""
    judge_data = await curd.create_master_plate(createMasterPlate.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.put("/update/master/plate", summary="更新模版")
async def update_master_plate(updateMasterPlate: UpdateMasterPlate, db: Session = Depends(get_db_content)):
    """每次更新模板， 相当于重新创建了一个模版，但是保留记录 记录原始数据,，
    1, 解决思路， 每次保存创建流程表，把数据放到流程表中， 更新模版中的数据的模版id，为流程表id，
    拉取历史数据时，则需要修改数据，相关联的 项目模版id一并修改成流程表中的id，设置雪花id
    """
