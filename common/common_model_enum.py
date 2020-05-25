#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：why
@file_name: common_model_enum.py
@create date: 2019-10-27 14:39 
@github https://github.com/why19970628
@csdn https://blog.csdn.net/weixin_43746433
@file_description：
"""

from enum import Enum, unique


@unique
class modelEnum(Enum):
    """
    请求模块枚举类
    """

    user = {'root': 'users', 'body': 'user'}
    department = {'root': 'departments', 'body': 'department'}
    role = {'root': 'roles', 'body': 'role'}
    user_group = {'root': 'user_groups', 'body': 'user_group'}
    login = {'root': 'logins', 'body': 'login'}
    permission = {'root': 'permissions', 'body': 'permission'}
    role_permission = {'root': 'role_permissions', 'body': 'role_permission'}
