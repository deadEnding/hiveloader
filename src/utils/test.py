#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from FileUtils import FileUtils
from TimeLimitExecutor import TimeLimitExecutor


class Task(object):

    def __init__(self, n):
        super(Task, self).__init__()
        self.n = n

    def run(self, x):
        time.sleep(20)
        print self.n + 10 + x


if __name__ == '__main__':
    # print FileUtils.countRow('/home/deadend/code/java/basic/')
    t = Task(2)
    exe = TimeLimitExecutor(10, t.run, args=(3, ))
    exe.execute()