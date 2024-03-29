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
    person_id: Optional[int] = Field(title="id")


class UpdatePerson(BaseModel):
    person_id: int = Field(title="用户id")
    department_id: Optional[int] = Field(title="部门id")
    person_name: Optional[str] = Field(title="用户名称")
    person_num: Optional[str] = Field(title="用户工号")
    password: Optional[str] = Field(title="用户密码")
    person_state: Optional[bool] = Field(title="用户状态")
    role_id: Optional[int] = Field(title="岗位id")


class DeletePerson(BaseModel):
    person_id: list[int] = Field(title="用户id")


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
    id: list[int] = Field(title="岗位id")


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
    ids: list[int] = Field(title="id")


class SearchSysDictValue(BaseModel):
    sys_dict_id: int = Field(title="sys_dict.id")
    dict_label: Optional[str] = Field(title="字典标签")
    dict_state: Optional[bool] = Field(title="字典状态")


class CreateSysDictValue(BaseModel):
    sys_dict_id: int = Field(title="sys_dict.id")
    data_label: str = Field(title="数据标签")
    sys_dict_value: str = Field(title="数据键值")
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
    menus: Optional[list[int]] = Field(title="菜单权限")


class UpdateRole(BaseModel):
    role_id: int = Field(title="角色id")
    role_name: Optional[str] = Field(title="角色名称")
    role_code: Optional[str] = Field(title="角色英文")
    role_sort: Optional[int] = Field(title="排序")
    role_state: Optional[bool] = Field(title="角色状态")
    menus: Optional[list[int]] = Field(None, title="菜单权限id")


class DeleteRole(BaseModel):
    role_id: list[int] = Field(title="role_id")


class CreateProjectState(BaseModel):
    state_name: str = Field(title="状态名称")
    index: int = Field(title="展示顺序")
    template_id: Optional[str] = Field(title="模板id")


class CreateBrodHeading(BaseModel):
    brod_name: str = Field(title="大类名称")
    brod_chart: str = Field(title="大类字符")


class UpdateBrodHeading(BaseModel):
    b_id: str = Field(title="b_id")
    brod_name: str = Field(title="大类名称")
    brod_chart: str = Field(title="大类字符")


class SearchBrodHeading(BaseModel):
    brod_name: Optional[str] = Field(title="大类名称")
    brod_chart: Optional[str] = Field(title="字符名称")


class CreateSubClass(BaseModel):
    sub_class_name: str = Field(title="小类名称")
    sub_class_chart: str = Field(title="小类字符")
    brod_heading_id: str = Field(title="大类id")


class SearchSubClass(BaseModel):
    sub_class_name: Optional[str] = Field(title="小类名称")
    sub_class_chart: Optional[str] = Field(title="小类字符")
    brod_heading_id: Optional[str] = Field(title="大类id")


class UpdateSubClass(BaseModel):
    b_id: Optional[str] = Field(title="小类id")
    sub_class_name: Optional[str] = Field(title="小类名称")
    sub_class_chart: Optional[str] = Field(title="小类字符")
    brod_heading_id: Optional[str] = Field(title="大类id")


# 创建可选模块
class CreateModule(BaseModel):
    name: str = Field(title="模块名称")
    sort: int = Field(title="顺序")
    name_en: str = Field(title="模块英文名称")


class DeleteModule(BaseModel):
    b_ids: list[str] = Field(title="模块id")


class UpdateModule(BaseModel):
    b_id: str = Field(title="模块id")
    name: Optional[str] = Field(title="模块名称")
    name_en: Optional[str] = Field(title="模块英文名称")


class ProjectState(BaseModel):
    # 项目阶段
    state_name: str = Field(title="阶段名称")
    sort: int = Field(title="排序")


class CreateTemplate(BaseModel):
    """创建模板"""
    name: str = Field(title="模版名称")
    project_states: list[ProjectState] = Field(title="项目阶段")


class UpdateTemplate(BaseModel):
    template_id: str = Field(title="模版id")
    name: str = Field(title="模版名称")
    project_states: list[ProjectState] = Field(title="项目阶段")


class UpdateSonState(BaseModel):
    """根据模板id和子模块id修改数据"""
    template_id: str = Field(title="模版id")
    module_id: str = Field(title="模块id")
    is_true: bool = Field(title="数据状态")
    is_change: Optional[bool] = Field(True, title="是否能够被更改")


class OptionalFile(BaseModel):
    """可选字段"""
    b_id: Optional[str] = Field(title="可选字段id")
    is_true: bool = Field(title="是否选择")


class ChooseFile(BaseModel):
    file_name: str = Field(title="自定义字段名称")
    file_name_en: str = Field(title="自定义字段英文名称")
    file_type: int = Field(title="类型")


class OptionalFileList(BaseModel):
    template_id: str = Field(title="模版id")
    module_id: str = Field(title="模板id")
    optional_list: list[OptionalFile] = Field(title="可选字段数据")
    choose_files: list[ChooseFile] = Field(title="自定义字段")


class TemplateOptionalFile(BaseModel):
    """和模板做绑定"""
    template_id: Optional[str] = Field(title="模板id")
    project_id: Optional[str] = Field(title="项目id")
    choose_files: list[ChooseFile] = Field(title="自定义字段")
    optional_files: list[OptionalFile] = Field(title="可选字段")


class Delete(BaseModel):
    b_ids: list[str] = Field(title="b_id数组")
