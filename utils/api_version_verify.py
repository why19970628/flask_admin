#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：why
@file_name: api_version_verify.py
@create date: 2019-10-27 14:15 
@github https://github.com/why19970628
@csdn https://blog.csdn.net/weixin_43746433
@file_description：api版本验证
"""

from functools import wraps

from flask import request

from common.common_request_process import req


def api_version(func):
    """
    API版本验证装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        xml = request.args.get('format')
        # 验证api版本
        verify_result, version_res = req.verify_version(kwargs.get('version'), xml)
        if not verify_result:
            return version_res
        return func(*args, **kwargs)

    return wrapper
