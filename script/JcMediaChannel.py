import json

from script.Base import Base


class JcMediaChannel(Base):

    def __init__(self, sendData):
        super().__init__(sendData)
        self.sendData = sendData
        self.TAG = 'JcMediaChannel'

    def run(self, data):
        if self.state == 0:

            self.sendData(self.creatCommand(
                command=["command", "mediaChannel", "join", [{"string": "test100"}, {"map": [{"password": "123456"}]}],
                         "bool"]))
            self.state += 1
        elif self.state == 1:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'join'):
                    if self.checkResult(data):
                        self.log("join 调用成功")
                    else:
                        self.log("join 调用失败")

        if self.isTimeout(60) is True:
            self.log('超时')
            return 2
