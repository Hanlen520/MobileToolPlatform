#!/usr/bin/env python
# -*- coding=utf8 -*-


class CustomFlaskErr(Exception):

    # 默认的返回码
    status_code = 400

    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self ,status_code=None, message=None, return_code=False, payload=None):
        Exception.__init__(self)
        self.message = message
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict(self.payload or ())
        # 增加 dict key: return code
        rv['code'] = self.status_code
        # 增加 dict key: message, 具体内容由常量定义文件中通过 return_code 转化而来
        rv['message'] = self.message
        rv['status'] = self.return_code
        return rv