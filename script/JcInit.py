from script.Base import Base
import json


class JcInit(Base):

    def __init__(self, sendData):
        Base.__init__(self, sendData)
        self.TAG = 'JcInit'

    # 0表示运行中 1表示成功 2表示失败
    def run(self, data):
        # 发送初始命令
        if self.state == 0:
            self.sendData(
                json.dumps({
                    "type": "command",
                    "method": "initialize",
                    "params": [
                        {"string": "6c06d1b0d9015e47ec144097"}
                    ],
                    "return": "bool"}) +
                '\r\n')
            self.log('发送初始化命令')
            self.state += 1
        # 等待初始结果
        elif self.state == 1:
            if data:
                print(self.TAG, 'data=', data)
                if data['type'] == 'command' and data['method'] == 'initialize':
                    if data['return'] is False:
                        self.log('初始失败')
                        return 2
                    else:
                        self.log('初始成功')
                        return 1

        if self.isTimeout(10) is True:
            self.log('超时')
            return 2

        return 0
