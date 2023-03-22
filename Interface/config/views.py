# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 22:57
from fastapi import APIRouter, Depends, Query
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


@router.post("/delete/department", summary="删除部门")
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


@router.post("/delete/person", summary="删除用户")
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
    judge_data, return_data = await curd.search_smp(searchSmp.dict(), db)
    if judge_data:
        return return_response.success(return_data)
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


@router.get("/search/role", summary="查看角色")
async def search_role(db: Session = Depends(get_db_content)):
    judge, data = await curd.search_role(db)
    if judge:
        return return_response.success(data)
    return return_response.error()


@router.put("/update/role", summary="更新角色")
async def update_role(updateRole: UpdateRole, db: Session = Depends(get_db_content)):
    judge = await curd.update_role(updateRole.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/role", summary="删除角色")
async def delete_role(deleteRole: DeleteRole, db: Session = Depends(get_db_content)):
    judge = await curd.delete_role(deleteRole, db)
    if judge:
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
    judge = await curd.update_master_plate(updateMasterPlate.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/master/plate", summary="删除模板")
async def delete_master_plate(deleteMasterPlate: DeleteMasterPlate, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_master_plate(deleteMasterPlate.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.get("/search/master/plate", summary="查询模板数据")
async def search_master_plate(master_plate_name=Query(None), db: Session = Depends(get_db_content)):
    judge_data = await curd.search_master_plate(master_plate_name, db)
    if isinstance(judge_data, list):
        return return_response.success(judge_data)
    return return_response.error()


# 可选字段选择
@router.get("/search/optional-field", summary="查看可选字段")
async def search_optional_field():
    judge = await curd.search_optional_field()
    return return_response.success(judge)


@router.post("/create/optional-log", summary="可选字段记录")
async def create_optional_log(createOptionalLog: CreateOptionalLog, db: Session = Depends(get_db_content)):
    judge = await curd.create_optional_log(createOptionalLog.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.get("/search/optional-log/{template_id}", summary="查看可选字段记录")
async def search_optional_log(template_id: str, db: Session = Depends(get_db_content)):
    judge = await curd.search_optional_log(template_id, db)
    return return_response.success(judge)


@router.post("/search/value-type", summary="查看字段类型")
async def search_value_type(db: Session = Depends(get_db_content)):
    judge_data = await curd.search_value_type(db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


"""
模版和项目阶段做绑定，敏捷和瀑布的阶段
"""


@router.post("/create/project-state", summary="创建项目状态")
async def create_project_state(createProjectState: CreateProjectState, db: Session = Depends(get_db_content)):
    judge = await curd.create_project_state(createProjectState.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.post("/search/project-state", summary="查询项目状态")
async def search_project_state(searchProjectState: SearchProjectState, db: Session = Depends(get_db_content)):
    """查询项目状态"""
    judge, all_data = await curd.search_project_state(searchProjectState, db)
    if judge:
        return return_response.success(all_data)
    return return_response.error()


@router.put("/update/project-state", summary="更新项目状态")
async def update_project_state(updateProjectState: UpdateProjectState, db: Session = Depends(get_db_content)):
    judge = await curd.update_project_state(updateProjectState.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/project-state/b_id", summary="删除项目状态")
async def delete_project_state(b_id: str, db: Session = Depends(get_db_content)):
    judge = await curd.delete_project_state(b_id, db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.get("/search/history/master/plate", summary="查看历史数据")
async def search_history_master_plate(master_plate_id: str, db: Session = Depends(get_db_content)):
    judge_data = await curd.search_history_master_plate(master_plate_id, db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.delete("/delete/history/master/plate", summary="删除历史模板")
async def delete_master_plate(deleteMasterPlate: DeleteMasterPlate, db: Session = Depends(get_db_content)):
    judge_data = await curd.delete_history_master_plate(deleteMasterPlate.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/brod-heading", summary="查询项目大类")
async def search_brod_heading(searchBrodHeading: SearchBrodHeading, db: Session = Depends(get_db_content)):
    """查询项目大类"""
    judge, data_list = await curd.search_brod_heading(searchBrodHeading.dict(), db)
    print(judge, "judge")
    if judge:
        return return_response.success(data_list)
    return return_response.error()


@router.post("/create/brod-heading", summary="增加项目大类")
async def create_brod_heading(createBrodHeading: CreateBrodHeading, db: Session = Depends(get_db_content)):
    """增加项目大类"""
    judge, id = await curd.create_brod_heading(createBrodHeading.dict(), db)
    if judge:
        return return_response.success(id)
    return return_response.error()


@router.put("/update/brod-heading", summary="更新项目大类")
async def update_brod_heading(updateBrodHeading: UpdateBrodHeading, db: Session = Depends(get_db_content)):
    """更新项目大类"""
    judge = await curd.update_brod_heading(updateBrodHeading.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/brod-heading/{b_id}", summary="删除项目大类")
async def delete_brod_heading(b_id: str, db: Session = Depends(get_db_content)):
    """删除项目大类"""
    judge = await curd.delete_brod_heading(b_id, db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.post("/create/sub-class", summary="创建小类")
async def create_sub_class(createSubClass: CreateSubClass, db: Session = Depends(get_db_content)):
    judge = await curd.create_sub_class(createSubClass.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.post("/search/sub-class", summary="查询小类")
async def search_sub_class(searchSubClass: SearchSubClass, db: Session = Depends(get_db_content)):
    judge, data_list = await curd.search_sub_class(searchSubClass.dict(), db)
    if judge:
        return return_response.success(data_list)
    return return_response.error()


@router.put("/update/sub-class", summary="更新小类")
async def update_sub_class(updateSubClass: UpdateSubClass, db: Session = Depends(get_db_content)):
    judge = await curd.update_sub_class(updateSubClass.dict(), db)
    if judge:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/sub-class/{b_id}", summary="删除小类")
async def delete_sub_class(b_id: str, db: Session = Depends(get_db_content)):
    judge = curd.delete_sub_class(b_id, db)
    if judge:
        return return_response.success()
    return return_response.error()


