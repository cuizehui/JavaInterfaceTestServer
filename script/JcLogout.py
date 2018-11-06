import json

from script.Base import Base


class JcLogout(Base):

    def __init__(self, sendData):
        Base.__init__(self, sendData)
        self.TAG = 'JcLogout'

    def run(self, data):
        if self.state == 0:
            self.sendData(
                json.dumps({
                    "type": "command",
                    "module": "client",
                    "method": "logout",
                    "params": [],
                    "return": "bool"}) +
                '\r\n')
            self.log('发送 logout 命令')
            self.state = 1
        elif self.state == 1:
            if data:
                self.showData(data)
                if data['type'] == 'command' and data['method'] == 'logout' and data['return'] is False:
                    self.log('logout 调用成功')
                    return 2
                else:
                    self.log('等待 logout 结果')
                    self.state = 2
        elif self.state == 2:
            if data:
                self.showData(data)
                if data['type'] == 'callback' and data['method'] == 'onLogout':
                    self.log('logout 成功')
                    return 1

        if self.isTimeout(10) is True:
            self.log('超时')
            return 2

        return 0
