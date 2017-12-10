#!/usr/bin/env python
# -*- encoding: utf-8  -*-

""" 
@version: v1.0 
@author: jayzhen 
@license: Apache Licence  
@contact: jayzhen_testing@163.com 
@site: http://blog.csdn.net/u013948858 
@software: PyCharm 
@time: 2017/7/27 23:29 
"""
import os
import re


class ApkController(object):
    """
    初始化就先确认存放apk文件的路径。
    """
    def __init__(self):
        # absp = os.getcwd()
        absp = "C:\\"
        apkp = os.path.join(absp, "apks")
        if not os.path.exists(apkp):
            os.mkdir(apkp)
        self.result_dir = apkp

    '''
    getLatestApk就是获取当前文件夹下的最新apk文件，并返回该文件的绝对路径和文件名。
    '''
    def get_latest_apk(self, apklist):
        if apklist is None:
            return None
        st = apklist.sort(key=lambda fn: os.path.getmtime(self.result_dir+"\\"+fn) if not os.path.isdir(self.result_dir + "\\" + fn) else 0)
        # d=datetime.datetime.fromtimestamp(os.path.getmtime(result_dir+"\\"+apklist[-1]))
        # print d
        fname = apklist[-1]
        fpath = os.path.join(self.result_dir,fname)
        return fpath, fname
    '''
    apklsit是获取当前文件夹下的所有apk文件，返回一个list。
    '''
    def apk_list(self):
        filelist = os.listdir(self.result_dir)
        apklist = []
        for fapk in filelist:
            if re.search(r'\.apk$', fapk):
                apklist.append(fapk)
        return apklist
    '''
    因为该模块会与apk在同一级文件夹下，所以知道文件名后，通过追加路径的方式，返回绝对路径。
    '''
    def apk_abs_path(self, apkName):
        try:
            abspath = os.path.join(self.result_dir,apkName)
            if not os.path.exists(abspath):
                # easygui.msgbox('>>>None apk file to REMOVE')
                wx.MessageDialog(None, 'None apk file to REMOVE', style=wx.OK | wx.CANCEL | wx.CENTRE).ShowModal()
                return None
        except TypeError, e:
            # easygui.msgbox('You cant choices one apk file for install ,so apkAbsPath happend TypeError')
            wx.MessageDialog(None, 'You cant choices one apk file for install ,so apkAbsPath happend TypeError', style=wx.OK | wx.CANCEL | wx.CENTRE).ShowModal()
            return None
        return abspath
    '''
    参数apk是apk的绝对路径，使用aapt命令来获取apk的包名，当然需要配置好aapt的环境变量。
    '''
    def get_apk_package_name(self, apk):
        try:
            if apk is not None:
                res = os.popen("aapt dump badging %s" % apk).read()
                if res is None or len(res) < 0:
                    return None
                # reg = "package\: name\=\'(.*?)'"
                reg = "package: name='(.*?)'"
                regc = re.compile(reg)
                res = re.findall(regc, res)
                if res is not None and len(res) > 0:
                    pname = str(res[0])
                wx.LogMessage("the apk's package name is [%s]" % pname)
                return pname
            else:
                return None
        except Exception, e:
            wx.LogMessage("An error occurred environment variable on aapt")
    '''
    使用python的os中的remove方法来删除指定路径的文件，删除之前先判断是否存在该文件。
    '''
    def delete_apk(self, apkpath):
        if os.path.exists(apkpath):
            os.remove(apkpath)
            if not os.path.exists(apkpath):
                return True
