#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
操作文件的工具类

@author: zhangzichao
@date: 2016-09-06
'''

import os
import glob
import shutil
import commands


class FileUtils(object):

    """
    统计文件行数
    @return 不存在返回0，出错返回-1
    """
    @staticmethod
    def countFileRow(path):
        if not os.path.isfile(path):
            return 0

        countCmd = "wc -l %s | grep -v total | awk '{sum += $1};END {print sum}'|awk '{print $1}'" % path
        count = commands.getstatusoutput(countCmd)[1]
        if count.isdigit():
            return int(count)
        else:
            return -1

    """
    删除目录下的隐藏文件
    """
    @staticmethod
    def rmHiddenFile(dirPath):
        if not os.path.isdir(dirPath):
            return

        rmCmd = "rm %s/.*"
        return os.system(rmCmd) == 0

    """
    对目录下的文件添加扩展名
    @param dirPath: 目录路径
    @param extension: 扩展名
    """
    @staticmethod
    def addExtension(dirPath, extension):
        if not os.path.isdir(dirPath):
            return

        files = os.listdir(dirPath)
        for fl in files:
            path = os.path.join(dirPath, fl)
            if os.path.isfile(path):
                os.rename(path, path + "." + extension)

    """
    将srcDirPath目录下匹配pattern的文件备份到dstDirPath
    @param srcDirPath: 源目录
    @param dstDirPath: 备份目录
    @param pattern: 备份的文件，支持通配符
    """
    @staticmethod
    def backup(srcDirPath, dstDirPath, pattern="*"):
        if not os.path.isdir(srcDirPath):
            return

        if not os.path.isdir(dstDirPath):
            os.makedirs(dstDirPath)

        for path in glob.iglob(os.path.join(srcDirPath, pattern)):
            if os.path.isfile(path):
                shutil.copy(path, dstDirPath)
