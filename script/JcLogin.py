import json

from script.Base import Base


class JcLogin(Base):

    def __init__(self, sendData):
        Base.__init__(self, sendData)
        self.TAG = 'JcLogin'

    def run(self, data):
        # 发送登陆命令
        if self.state == 0:
            self.sendData(
                json.dumps({
                    "type": "command",
                    "module": "client",
                    "method": "login",
                    "params": [
                        {"string": "test001"},
                        {"string": "234234354"}],
                    "return": "bool"}) +
                '\r\n')
            self.log('发送 login 命令')
            self.state += 1
        # 等待登陆结果
        elif self.state == 1:
            if data:
                self.showData(data)
                if data['type'] == 'command' and data['method'] == 'login' and data['return'] is False:
                    self.log('login 调用失败')
                    return 2
                else:
                    self.log('等待 login 结果')
                    self.state += 1

        elif self.state == 2:
            if data:
                self.showData(data)
                if data['type'] == 'callback' and data['method'] == 'onLogin':
                    if data['arg0'] is True:
                        self.log('login 成功')
                        self.sendData(
                            json.dumps({
                                "type": "command",
                                "module": "client",
                                "method": "getState",
                                "params": [],
                                "return": "int"}) +
                            '\r\n')
                        self.log('发送 getState 命令')
                        self.state += 1
                    else:
                        self.log('login 失败')
                        return 2
        elif self.state == 3:
            if data:
                self.showData(data)
                if data['type'] == 'command' and data['method'] == 'getState':
                    if data['return'] == 3:
                        self.log('getState 获取值匹配')
                    else:
                        self.log('getState 获取值不匹配')
                    self.sendData(
                        json.dumps({
                            "type": "command",
                            "module": "client",
                            "method": "getUserId",
                            "params": [],
                            "return": "string"}) +
                        '\r\n')
                    self.log('发送 getUserId 命令')
                    self.state += 1
        elif self.state == 4:
            if data:
                self.showData(data)
                if data['type'] == 'command' and data['method'] == 'getUserId':
                    if data['return'] == 'test001':
                        self.log('getUserId 获取值匹配')
                        return 1
                    else:
                        self.log('getUserId 获取值不匹配')
                        return 1

        if self.isTimeout(30) is True:
            self.log('超时')
            return 2

        return 0
