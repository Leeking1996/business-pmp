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
async def search_snow_flake_id(datacenter_id: Optional[int] = None, worker_id: Optional[int] = None,
                               sequence: Optional[int] = None):
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


@router.post("/create/smp", summary="新增岗位")
async def create_spm(createSpm: CreateSpm, db: Session = Depends(get_db_content)):
    judge_data = await curd.create_smp(createSpm.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/smp", summary="查询岗位")
async def search_spm(searchSmp: SearchSmp, db: Session = Depends(get_db_content)):
    judge_data, return_data = await curd.search_smp(searchSmp.dict(), db)
    if judge_data:
        return return_response.success(return_data)
    return return_response.error()


@router.put("/update/smp", summary="更新岗位")
async def update_spm(updateSmp: UpdateSmp, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_smp(updateSmp.dict(), db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.delete("/delete/smp", summary="删除岗位")
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
    judge, judge_data = await curd.search_sys_dict(searchSysDict.dict(), db)
    print(judge, "judge")
    if judge:
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
    judge, data = await curd.search_sys_dict_value(searchSysDictValue.dict(), db)
    if judge:
        return return_response.success(data)
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
        return return_response.success()
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
    judge, data = await curd.search_menu(searchMenu.dict(), db)
    if judge:
        return return_response.success(data)
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


@router.post("/search/value-type", summary="查看字段类型")
async def search_value_type(db: Session = Depends(get_db_content)):
    judge_data = await curd.search_value_type(db)
    if judge_data:
        return return_response.success(judge_data)
    return return_response.error()


@router.post("/search/brod-heading", summary="查询项目大类")
async def search_brod_heading(searchBrodHeading: SearchBrodHeading, db: Session = Depends(get_db_content)):
    """查询项目大类"""
    judge, data_list = await curd.search_brod_heading(searchBrodHeading.dict(), db)
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


@router.delete("/delete/brod-heading", summary="删除项目大类")
async def delete_brod_heading(delete: Delete, db: Session = Depends(get_db_content)):
    """删除项目大类"""
    judge = await curd.delete_brod_heading(delete, db)
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


@router.delete("/delete/sub-class", summary="删除小类")
async def delete_sub_class(b_ids: Delete, db: Session = Depends(get_db_content)):
    judge = await curd.delete_sub_class(b_ids, db)
    if judge:
        return return_response.success()
    return return_response.error()


"""模板相关接口"""


@router.post("/create/template", summary="新增模板")
async def create_template(createTemplate: CreateTemplate, db: Session = Depends(get_db_content)):
    """创建模板时，需要查询可选模块，可选模块进行数据的更新，保存到指定表中"""
    judge, template_b_id = await curd.create_template(createTemplate.dict(), db)
    if judge:
        return return_response.success(template_b_id)
    return return_response.error()


@router.delete("/delete/template", summary="删除模板")
async def delete_template(delete: Delete, db: Session = Depends(get_db_content)):
    """删除模板"""
    judge_data = await curd.delete_template(delete, db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.put("/update/template", summary="更新模板")
async def update_template(updateTemplate: UpdateTemplate, db: Session = Depends(get_db_content)):
    """更新模板"""
    judge_data = await curd.update_template(updateTemplate, db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.post("/search/template", summary="查看模板")
async def search_template(db: Session = Depends(get_db_content)):
    """查看模板"""
    judge_data = await curd.search_template(db)
    return return_response.success(judge_data)


@router.get("/search/template/{b_id}", summary="查看模板详情")
async def search_template_detail(b_id: str, db: Session = Depends(get_db_content)):
    """查看模板详情"""
    judge, data = await curd.search_template_details(b_id, db)
    if judge:
        return return_response.success(data)
    return return_response.error()


@router.put("/update/option/module/state", summary="修改状态子模块展示状态")
async def update_son_state(updateSonState: UpdateSonState, db: Session = Depends(get_db_content)):
    judge_data = await curd.update_template_son_module_state(updateSonState, db)
    if judge_data:
        return return_response.success()
    return return_response.error()


@router.get("/search/optional/field", summary="查看可选字段")
async def search_project_optional_field(template_id: str, module_id: str, db: Session = Depends(get_db_content)):
    """查看项目基本信息可选字段的数据"""
    judge_data = await curd.search_project_optional_field(template_id, module_id, db)
    return return_response.success(judge_data)


@router.put("/update/project/optional/file", summary="更新可选字段状态")
async def update_project_optional_file(updateOptionalFile: OptionalFileList, db: Session = Depends(get_db_content)):
    """更新项目可选字段状态"""
    judge_data = await curd.update_optional_file(updateOptionalFile, db)
    if judge_data:
        return return_response.success()
    return return_response.error()

