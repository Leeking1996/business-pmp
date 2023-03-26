# -*- coding:utf-8 -*-
# Author: lee
# 2023/2/1 23:03

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, func, ForeignKey, DateTime, text, JSON
from sqlalchemy.orm import relationship
from db import Base

"""增加 platform_code 字段 用来使用多租户模式"""


# 创建部门
class SysDepartment(Base):
    __tablename__ = "sys_department"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, name="id", comment="主键")
    superior_department = Column(Integer, name="superior_department", comment="上级部门")
    department_name = Column(String(64), name="department_name", comment="部门名称")
    leader_name = Column(String(64), name="leader_name", comment="部门负责人")
    leader_code = Column(String(32), name="leader_code", comment="部门负责人工号")
    phone_num = Column(String(11), name="phone_num", comment="电话号码")
    email = Column(String(32), name="email", comment="邮箱")
    parent_id = Column(ForeignKey("sys_department.id"))
    departmentData = relationship("SysDepartment")
    department_state = Column(Boolean, name="department_state", comment="部门状态")
    create_user = Column(String(32), name="create_user", comment="创建人")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    update_user = Column(String(32), name="update_user", comment="更新人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新人")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "superior_department": self.superior_department,
            "department_name": self.department_name,
            "leader_name": self.leader_name,
            "leader_code": self.leader_code,
            "phone_num": self.phone_num,
            "email": self.email,
            "parent_id": self.parent_id,
            "department_state": self.department_state,
            "create_user": self.create_user,
            "create_time": str(self.create_time),
            "update_user": self.update_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "platform_code": self.platform_code,
            "is_delete": self.is_delete
        }


# 创建人员
class SysUser(Base):
    __tablename__ = "sys_user"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, name="id", comment="主键")
    person_num = Column(String(32), name="person_num", comment="工号", nullable=False)
    password = Column(String(64), name="password", comment="密码", nullable=False)
    person_name = Column(String(32), name="person_name", comment="姓名", nullable=False)
    department_id = Column(ForeignKey("sys_department.id"))
    department_data = relationship("SysDepartment", uselist=False)
    role_id = Column(Integer, name="role_id", comment="角色")
    post_management_id = Column(ForeignKey("sys_post_management.id"))
    post_management_data = relationship("SysPostManagement")
    person_state = Column(Boolean, name="person_state", comment="人员状态，True显示， False不显示")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    update_user = Column(String(32), name="update_user", comment="更新人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "person_num": self.person_num,
            "person_name": self.person_name,
            "department_id": self.department_id,
            "role_id": self.role_id,
            "post_management_id": self.post_management_id,
            "update_user": self.update_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "is_delete": self.is_delete,
            "department_name": self.department_data.department_name,
            "platform_code": self.platform_code,
            "person_state": self.person_state

        }


# 岗位管理
class SysPostManagement(Base):
    __tablename__ = "sys_post_management"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    post_management_name = Column(String(32), name="post_management_name", comment="岗位名称")
    post_management_code = Column(String(32), name="post_management_code", comment="岗位编码")
    index = Column(Integer, name="index", comment="岗位顺序", nullable=False)
    remarks = Column(String(256), name="remarks", comment="备注")
    state = Column(Boolean, name="state", comment="岗位状态")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "post_management_name": self.post_management_name,
            "post_management_code": self.post_management_code,
            "index": self.index,
            "remarks": self.remarks,
            "state": self.state,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user,
            "platform_code": self.platform_code
        }


# 字典管理
class SysDict(Base):
    __tablename__ = "sys_dict"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    dict_name = Column(String(32), name="dict_name", comment="字典名称", nullable=False)
    dict_type = Column(String(32), name="dict_code", comment="字典类型", nullable=False)
    dict_state = Column(Boolean, name="dict_type", comment="字典状态")
    remarks = Column(String(256), name="remarks", comment="备注")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "dict_name": self.dict_name,
            "dict_type": self.dict_type,
            "dict_state": self.dict_state,
            "remarks": self.remarks,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user,
            "platform_code": self.platform_code
        }


# 字典值
class SysDictValue(Base):
    __tablename__ = "sys_dict_value"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    sys_dict_id = Column(Integer, name="sys_dict_id", comment="父级id")
    data_label = Column(String(64), name="data_label", comment="数据标签名称", nullable=False)
    sort = Column(Integer, name="sort", comment="排序")
    value_state = Column(Boolean, name="value_state", comment="状态")
    remarks = Column(String(256), name="remarks", comment="备注")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "data_label": self.data_label,
            "sort": self.sort,
            "value_state": self.value_state,
            "remarks": self.remarks,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user,
            "platform_code": self.platform_code

        }


# 角色管理
class SysRole(Base):
    __tablename__ = "sys_role"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    role_name = Column(String(32), name="role_name", comment="角色名称", nullable=False)
    role_code = Column(String(64), name="role_power", comment="角色编码", nullable=False)
    role_sort = Column(Integer, name="role_sort", comment="排序")
    role_state = Column(Boolean, name="role_state", comment="状态")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "role_name": self.role_name,
            "role_code": self.role_code,
            "role_sort": self.role_sort,
            "role_state": self.role_state,
            "platform_code": self.platform_code,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user

        }


class SysRoleRelationMenu(Base):
    __tablename__ = "sys_role_relation_menu"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    sys_role_id = Column(Integer, name="sys_role_id", comment="角色id")
    sys_menu_id = Column(Integer, name="sys_menu_id", comment="菜单表")


class SysMenu(Base):
    __tablename__ = "sys_menu"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    superior_menu = Column(Integer, name="superior_menu", comment="上级菜单")
    menu_type = Column(Integer, name="menu_type", comment="菜单类型: 1:目录, 2:菜单, 3:按钮")
    menu_cron = Column(String(32), name="menu_cron", comment="菜单图标")
    menu_name = Column(String(32), name="menu_name", comment="菜单名称", nullable=False)
    sort = Column(Integer, name="sort", comment="显示排序")
    router_address = Column(String(128), name="router_address", comment="路由地址", nullable=False)
    menu_state = Column(Boolean, name="menu_state", comment="菜单状态")
    unit_address = Column(String(128), name="unit_address", comment="组件地址")
    parent_id = Column(ForeignKey("sys_menu.id"))
    menuData = relationship("SysMenu")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "superior_menu": self.superior_menu,
            "menu_type": self.menu_type,
            "menu_cron": self.menu_cron,
            "menu_name": self.menu_name,
            "sort": self.sort,
            "router_address": self.router_address,
            "menu_state": self.menu_state,
            "unit_address": self.unit_address,
            "parent_id": self.parent_id,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user,
            "platform_code": self.platform_code
        }


# 模版表是否增加是软件类型的情况下 1，敏捷 2，瀑布

class MasterPlate(Base):
    __tablename__ = "master_plate"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(32), name="b_id", comment="唯一id")
    name = Column(String(128), name="name", comment="模版名称")
    template_properties = Column(String(128), comment="模板属性")
    code = Column(String(12), name="code", comment="用于生成项目编码")
    type = Column(Integer, comment="模板类型1")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "create_name": self.create_user,
            "create_time": str(self.create_time),
            "b_id": self.b_id,
            "platform_code": self.platform_code,
            "template_properties": self.template_properties,
            "type": self.type,
            "code": self.code,
        }


class MasterPlateLog(Base):
    __tablename__ = "master_plate_log"
    """历史模板"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    master_plate_id = Column(String(65), name="master_plate_id", comment="模板id")
    b_id = Column(String(32), name="b_id", comment="唯一id")
    name = Column(String(128), name="name", comment="模版名称")
    code = Column(String(12), name="code", comment="用于生成项目code")
    type = Column(Integer, name="type", comment="模板类型， 1 软件， 2，其他")
    project_type = Column(Integer, name="project_type", comment="软件类型下 1，敏捷 2，瀑布， 3策划")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "master_plate_id": self.master_plate_id,
            "name": self.name,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": self.update_time,
            "update_user": self.update_user,
            "type": self.type,
            "project_type": self.project_type

        }


class MasterPlateValue(Base):
    __tablename__ = "master_plate_value"
    """自定义模版属性"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(32), name="b_id", comment="唯一id")
    name_en = Column(String(128), name="name_en", comment="自定义名称")
    name_english = Column(String(128), name="name_english", comment="自定义名称英文")
    value_type = Column(Integer, name="value_type", comment="字段类型")
    master_plate_id = Column(String(65), name="mater_plate_id", comment="模版id")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="is_delete", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "name_en": self.name_en,
            "name_english": self.name_english,
            "value_type": self.value_type,
            "master_plate_id": self.master_plate_id,
            "platform_code": self.platform_code,
            "create_time": str(self.create_time),
            "create_user": self.create_user,
            "update_time": str(self.update_time) if self.update_time else None,
            "update_user": self.update_user

        }


class ValueType(Base):
    __tablename__ = "value_type"
    """类型，bool， str, int, float"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    type_name = Column(String(32), name="type_name", comment="类型名称")
    type_value = Column(String(32), name="type_value", comment="类型")

    def to_dict(self):
        return {
            "id": self.id,
            "type_name": self.type_name,
            "type_value": self.type_value
        }


class BrodHeading(Base):
    __tablename__ = "brod_heading"
    """项目大类"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(128), name="b_id", comment="b_id")
    brod_name = Column(String(128), name="brod_name", comment="项目大类")
    brod_chart = Column(String(30), name="brod_chart", comment="字符")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "brod_name": self.brod_name,
            "brod_chart": self.brod_chart
        }


class SubClass(Base):
    # 项目小类
    __tablename__ = "sub_class"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(128), name="b_id", comment="唯一id")
    sub_class_name = Column(String(128), name="sub_class_name", comment="项目小类")
    sub_class_chart = Column(String(30), name="sub_class_chart", comment="项目小类字符")
    brod_heading_id = Column(String(128), name="brod_heading_id", comment="项目大类id")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "sub_class_name": self.sub_class_name,
            "sub_class_chart": self.sub_class_chart,
            "brod_heading_id": self.brod_heading_id
        }


class ProjectState(Base):
    """项目阶段和模板绑定"""
    __tablename__ = "project_state"
    """项目阶段"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(128), name="b_id", comment="b_id")
    state_name = Column(String(256), name="state_name", comment="阶段名称")
    index = Column(Integer, name="index", comment="展示顺序")
    template_id = Column(String(128), name="template_id", comment="模板id")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)

    def to_dict(self):
        return {
            "b_id": self.b_id,
            "state_name": self.state_name,
            "index": self.index,
            "template_id": self.template_id,
            "platform_code": self.platform_code,
        }


class OptionalTable(Base):
    __tablename__ = "optional_table"
    """可选字段表"""
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    b_id = Column(String(128), name="b_id", comment="唯一id")
    territory = Column(String(128), name="territory", comment="领域")
    product_name = Column(String(128), name="product_name", comment="产品名称")
    product_manager = Column(String(128), name="product_manager", comment="产品经理工号")
    product_manager_code = Column(String(128), name="product_manager_code", comment="产品经理姓名")
    develop_type = Column(String(128), name="develop_type", comment="开发类型")
    estimate_all_day = Column(Integer, name="estimate_all_day", comment="预计总人天")
    project_director = Column(String(128), name="project_director", comment="项目总监")
    unit = Column(String(256), name="unit", comment="主责单位")
    department = Column(String(256), name="department", comment="主责部门")
    office = Column(String(256), name="office", comment="主责科室")
    service_manager = Column(String(256), name="service_manager", comment="业务经理")
    service_department = Column(String(256), name="service_department", comment="业务部门")
    template_id = Column(String(128), name="template_id", comment="模板id")
    platform_code = Column(String(64), name="platform_code", comment="平台code")
    create_time = Column(DateTime, default=func.now(), name="create_time", comment="创建时间")
    create_user = Column(String(32), name="create_user", comment="创建人")
    update_time = Column(DateTime, server_onupdate=func.now(), name="update_time", comment="更新时间")
    update_user = Column(String(32), name="update_user", comment="update_user")
    is_delete = Column(Boolean, name="is_delete", comment="是否删除", default=False)


class OptionalLog(Base):
    __tablename__ = "optional_log"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True, nullable=False, name="id", comment="主键")
    template_id = Column(String(128), name="template_id", comment="模板id")
    colum = Column(String(128), name="colum", comment="字段名称")
    is_true = Column(Boolean, name="is_true", comment="是否展示")

    def to_dict(self):
        return {
            "id": self.id,
            "template_id": self.template_id,
            "colum": self.colum,
            "is_true": self.is_true
        }
