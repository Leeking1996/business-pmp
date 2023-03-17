# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 23:03
from pydantic import BaseModel, Field
from typing import Optional


class CreateDepartment(BaseModel):
    # 创建部门接口
    department_name: Optional[str] = Field(None, title="部门名称")
    leader_name: Optional[str] = Field(None, title="负责人姓名")
    leader_code: Optional[str] = Field(None, title="负责人工号")
    phone_num: Optional[str] = Field(None, title="电话")
    email: Optional[str] = Field(None, title='邮箱')
    parent_id: Optional[int] = Field(None, title="上级部门id")
    department_state: Optional[int] = Field(default=False, title="部门状态")


class SearchDepartment(BaseModel):
    # 查询部门接口
    department_name: Optional[str] = Field(title="部门名称")
    department_state: Optional[bool] = Field(title="部门状态")


class UpdateDepartment(BaseModel):
    id: int = Field(title="部门ID")
    department_name: Optional[str] = Field(None, title="部门名称")
    leader_name: Optional[str] = Field(None, title="负责人姓名")
    leader_code: Optional[str] = Field(None, title="负责人工号")
    phone_num: Optional[str] = Field(None, title="电话")
    email: Optional[str] = Field(None, title='邮箱')
    parent_id: Optional[int] = Field(None, title="上级部门id")
    department_state: Optional[int] = Field(default=False, title="部门状态")


class DeleteDepartment(BaseModel):
    ids: list[int] = Field(title="部门id")


class CreatePerson(BaseModel):
    # 创建用户
    person_num: str = Field(title="用户工号")
    person_name: str = Field(title="用户姓名")
    password: str = Field(title="用户密码")
    department_id: int = Field(title="部门id")
    role_id: Optional[int] = Field(title="角色id")
    post_management_id: Optional[int] = Field(title="岗位id")
    person_state: Optional[bool] = Field(title="人员状态")


class SearchPerson(BaseModel):
    # 查询用户
    page: Optional[int] = Field(default=1, title="页码")
    size: Optional[int] = Field(default=10, title="数量")
    person_name: Optional[str] = Field(title="用户名称")
    person_code: Optional[str] = Field(title="工号")
    department_id: Optional[int] = Field(title="部门id")
    person_state: Optional[bool] = Field(title="员工状态")
    person_id: Optional[int] = Field(title="员工工号")


class UpdatePerson(BaseModel):
    person_id: int = Field(title="用户id")
    department_id: Optional[int] = Field(title="部门id")
    person_name: Optional[str] = Field(title="用户名称")
    person_code: Optional[str] = Field(title="用户工号")
    password: Optional[str] = Field(title="用户密码")
    person_state: Optional[bool] = Field(title="用户状态")
    role_id: Optional[int] = Field(title="岗位id")


class DeletePerson(BaseModel):
    person_id: int = Field(title="用户id")


class CreateSpm(BaseModel):
    post_management_name: str = Field(title="岗位名称")
    post_management_code: str = Field(title="岗位编码")
    index: int = Field(title="岗位顺序 从小到大")
    remarks: Optional[str] = Field(title="备注")
    state: bool = Field(title="岗位状态")


class SearchSmp(BaseModel):
    post_management_name: Optional[str] = Field(title="岗位名称")
    post_management_code: Optional[str] = Field(title="岗位编码")
    state: Optional[bool] = Field(title="岗位状态")


class UpdateSmp(BaseModel):
    id: int = Field(title="岗位管理id")
    post_management_name: Optional[str] = Field(title="岗位名称")
    post_management_code: Optional[str] = Field(title="岗位编码")
    index: Optional[int] = Field(title="岗位顺序")
    remarks: Optional[str] = Field(title="备注")


class DeleteSmp(BaseModel):
    id: int = Field(title="岗位id")


class CreateSysDict(BaseModel):
    dict_name: str = Field(title="字典名称")
    dict_type: str = Field(title="字典类型")
    dict_state: bool = Field(title="字典状态")
    remarks: Optional[str] = Field(title="备注")


class SearchSysDict(BaseModel):
    page: Optional[int] = Field(default=1, title="页码")
    size: Optional[int] = Field(default=10, title="条数")
    dict_name: Optional[str] = Field(title="字典名称")
    dict_type: Optional[str] = Field(title="字典类型")
    dict_state: Optional[bool] = Field(title="字典状态")


class UpdateSysDict(BaseModel):
    id: int = Field(title="父级id")
    dict_name: Optional[str] = Field(title="字典名称")
    dict_type: Optional[str] = Field(title="字典类型")
    dict_state: Optional[bool] = Field(title="字典状态")


class DeleteSysDict(BaseModel):
    id: int = Field(title="id")


class SearchSysDictValue(BaseModel):
    parent_id: int = Field(title="sys_dict.id")
    dict_label: Optional[str] = Field(title="字典标签")
    dict_state: Optional[bool] = Field(title="字典状态")


class CreateSysDictValue(BaseModel):
    sys_dict_id: int = Field(title="sys_dict.id")
    data_label: str = Field(title="数据标签")
    sort: Optional[int] = Field(title="排序")
    value_state: Optional[bool] = Field(title="状态")
    remarks: Optional[str] = Field(title="备注")


class UpdateSysDictVale(BaseModel):
    id: int = Field(title="自身id")
    sys_dict_id: int = Field(title="sys_dict.id")
    data_label: str = Field(title="数据标签")
    sort: Optional[int] = Field(title="排序")
    value_state: Optional[bool] = Field(title="状态")
    remarks: Optional[str] = Field(title="备注")


class CreateMenu(BaseModel):
    """创建菜单"""
    superior_menu: Optional[str] = Field(title="上级菜单")
    menu_type: int = Field(title="菜单类型 1：菜单， 2：按钮， 3：目录")
    menu_cron: Optional[str] = Field(title="菜单图标")
    menu_name: Optional[str] = Field(title="菜单名称")
    sort: int = Field(title="显示排序")
    router_address: Optional[str] = Field(title="路由地址")
    menu_state: Optional[bool] = Field(title="菜单状态")
    unit_address: Optional[str] = Field(title="组件地址")
    parent_id: Optional[int] = Field(title="父级id")


class UpdateMenu(BaseModel):
    """创建菜单"""
    id: int = Field(title="菜单id")
    superior_menu: Optional[str] = Field(title="上级菜单")
    menu_type: int = Field(title="菜单类型")
    menu_cron: Optional[str] = Field(title="菜单图标")
    menu_name: Optional[str] = Field(title="菜单名称")
    sort: int = Field(title="显示排序")
    router_address: Optional[str] = Field(title="路由地址")
    menu_state: Optional[bool] = Field(title="菜单状态")
    unit_address: Optional[str] = Field(title="组件地址")
    parent_id: Optional[int] = Field(title="父级id")


class SearchMenu(BaseModel):
    menu_name: Optional[str] = Field(title="菜单名称")
    menu_state: Optional[bool] = Field(title="菜单状态")


class DeleteMenu(BaseModel):
    id: int = Field(title="id")


class CreateRole(BaseModel):
    role_name: str = Field(title="角色名称")
    role_code: str = Field(title="角色英文")
    role_sort: int = Field(title="排序")
    role_state: bool = Field(title="角色状态")
    menu_ids: list = Field(title="菜单权限")


class CreateMasterPlateValue(BaseModel):
    """模版数据"""
    name_en: str = Field(title="自定义名称")
    name_english: str = Field(title="自定义英文名称")
    value_type: int = Field(title="字段类型")


class CreateMasterPlate(BaseModel):
    """创建模版"""
    name: str = Field(title="模版名称")
    template_properties: str = Field(title="模板属性")
    type: Optional[int] = Field(title="如果是软件 1:敏捷， 2: 瀑布")
    master_plate_value: list[CreateMasterPlateValue] = Field(title="模版名称数据")


class UpdateMasterPlate(BaseModel):
    """更新模版"""
    master_plate_id: str = Field(title="模板id")
    name: str = Field(title="模板名称")
    master_plate_value: list[CreateMasterPlateValue] = Field(title="模板数据")


class DeleteMasterPlate(BaseModel):
    master_plate_id: str = Field(title="模板id")
