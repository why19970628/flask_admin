#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：why
@file_name: resource.py
@create date: 2019-10-27 13:28 
@github https://github.com/why19970628
@csdn https://blog.csdn.net/weixin_43746433
@file_description：
"""
from flask_restful import Api

from api.department.interface_department import interfaceDepartment
from api.department.interface_department_staff import interfaceDepartmentStaff
from api.login.interface_login import interfaceLogin
from api.role.interface_permission import interfacePermission
from api.role.interface_role import interfaceRole
from api.role.interface_role_permission import interfaceRolePermission
from api.user.interface_basic import interfaceUserBasic
from api.user.interface_password import interfacePassword
from api.user.interface_user import interfaceUser
from api.user_group.interface_user_group import interfaceUserGroup
from api.user_group.interface_user_group_role import interfaceUserGroupRole
from api.user_group.interface_user_group_staff import interfaceUserGroupStaff

api = Api()

# 部门管理
api.add_resource(
    interfaceDepartment,
    '/why/<version>/department',
    '/why/<version>/department/<int:dpt_id>'
)


api.add_resource(
    interfaceDepartmentStaff,
    '/why/<version>/department/staff/<int:dpt_id>'
)

# 用户
api.add_resource(
    interfaceUser,
    '/why/<version>/user',
    '/why/<version>/user/<int:user_id>',

)

# 密码
api.add_resource(
    interfacePassword,
    '/why/<version>/user/<int:user_id>/password'
)

# 基本信息修改
api.add_resource(
    interfaceUserBasic,
    '/why/<version>/user/<int:user_id>/base/info'
)

# 角色
api.add_resource(
    interfaceRole,
    '/why/<version>/role',
    '/why/<version>/role/<int:role_id>'
)
#  角色权限
api.add_resource(
    interfaceRolePermission,
    '/why/<version>/role/<role_id>/permission'
)
# 权限
api.add_resource(
    interfacePermission,
     '/why/<version>/permission'
)

# 用户组
api.add_resource(
    interfaceUserGroup,
    '/why/<version>/user/group',
    '/why/<version>/user/group/<int:group_id>'
)


api.add_resource(
    interfaceUserGroupStaff,
    '/why/<version>/user/group/<int:group_id>/staff'
)

# 获取用户组的角色信息
api.add_resource(
    interfaceUserGroupRole,
    '/why/<version>/user/group/<int:group_id>/role'
)

api.add_resource(
    interfaceLogin,
    '/why/<version>/login'
)