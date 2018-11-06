#!/usr/bin/python
# -*- coding: UTF-8 -*-

import importlib
import logging
import os
import time


class ScriptManager(object):

    def __init__(self, sendData):
        self.runscripts = ['JcInit', 'JcLogin', 'JcCall', 'JcLogout']
        self.sendData = sendData
        self.scripts = []
        self.runModule = None
        self.createOutFile()
        self.loadScripts()
        self.chooseScript()

    # 获得所有脚本
    def loadScripts(self):
        names = os.listdir(os.path.split(os.path.realpath(__file__))[0] + "/script/")
        for i in range(0, len(names)):
            print(names[i])
            if names[i].find('Jc') == 0:
                self.scripts.append(names[i].replace('.py', ''))

    def setScript(self, script):
        if script not in self.scripts:
            print('找不到脚本')
            return False
        module = importlib.import_module('script.%s' % script)
        module_cls = getattr(module, script)
        self.runModule = module_cls(self.sendData)
        print('启动script', script)
        logging.info('启动script ' + str(script))
        return True

    def run(self, data):
        if self.runModule:
            ret = self.runModule.run(data)
            if ret != 0:
                self.runModule = None
            if ret == 1:
                self.chooseScript()
            elif ret == 2:
                print("script 执行失败")
                logging.info('script 执行失败 ')
        elif data:
            print(data)
            if 'run-script' in data:
                self.setScript(data['run-script'])

    def chooseScript(self):
        if len(self.runscripts) > 0:
            self.setScript(self.runscripts[0])
            self.runscripts.pop(0)
        else:
            print("script 脚本结束")
            logging.info("script 脚本结束")

    def createOutFile(self):
        folder = os.path.exists('out')
        if not folder:
            os.makedirs('out', mode=0o777)
        else:
            print
            "---  There is this folder!  ---"
        if os.path.exists(os.getcwd() + "/out"):
            # 创建Log日志
            localtime = time.localtime(time.time())
            times = str(localtime.tm_mon) + str(localtime.tm_mday) + str(localtime.tm_hour) + str(localtime.tm_min)
            open(os.getcwd() + '/out/' + times + '_test.log', mode='a').close()
            logging.basicConfig(level=logging.DEBUG, filename=os.getcwd() + '/out/' + times + '_test.log')
        else:
            logging.basicConfig(level=logging.DEBUG)
