import json
from abc import ABC, abstractmethod
import time


class Base(ABC):

    def __init__(self, sendData):
        self.sendData = sendData
        self.beginTime = time.time()
        self.state = 0
        self.TAG = 'Base'

    @abstractmethod
    def run(self, data):
        pass

    def isTimeout(self, timeout):
        return time.time() > self.beginTime + timeout

    def refreshTime(self):
        self.beginTime = time.time()

    def log(self, content):
        print(self.TAG, self.state, content)

    def showData(self, data):
        print(self.TAG, 'data=', data)

    def creatCommand(self, command):
        """
        创建测试命令
        :param command: 测试参数字典
        :return: 测试命令
        """
        return json.dumps(
            {"type": command[0], "module": command[1], "method": command[2], "params": command[3],
             "return": command[4]}) + '\r\n'

    def waitMethod(self, data, method):
        """
        判断是否是需要校验的方法
        :param data: 校验数据
        :param method: 方法名
        :return: 校验结果
        """
        return data['type'] == 'command' and data['method'] == method

    def waitCallBack(self, data, callback):
        """
        判断是否是需要校验的回调
        :param data: 校验数据
        :param callback: 回调名
        :return: 校验结果
        """
        if data['type'] == 'callback' and data['method'] == callback:
            return True
        else:
            return False

    def checkResult(self, data):
        """
        检查调用结果
        :param data: 校验数据
        :return: 调用结果
        """
        if data['return'] is True:
            return True
        else:
            return False
