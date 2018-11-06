import json

from script.Base import Base


class JcCall(Base):

    def __init__(self, sendData):
        super().__init__(sendData)
        self.TAG = 'JcCall'
        self.callitem = {}

        # 0表示运行中 1表示成功 2表示失败

    def run(self, data):
        # 发送初始命令
        if self.state == 0:
            # call接口测试
            self.sendData(self.creatCommand(
                command=["command", "call", "call", [{"string": "test100"}, {"bool": True}, {'string': ''}],
                         "bool"]))
            self.log('发送 call 命令')
            self.state += 1
        elif self.state == 1:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'call'):
                    if self.checkResult(data):
                        self.log('等待接通')
                        self.state += 1
                    else:
                        self.log('call 调用失败')
                        return 2

        elif self.state == 2:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['state'] == 3:
                        # mute接口测试
                        self.sendData(self.creatCommand(
                            command=["command", "call", "mute", [{"callitem": self.callitem}], "bool"]))
                        self.log('调用mute接口')
                        self.state += 1
        elif self.state == 3:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'mute'):
                    if self.checkResult(data):
                        self.log('等待静音')
                        self.state += 1
                    else:
                        self.log('mute 调用失败')
                        return 2
        elif self.state == 4:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['mute']:
                        # hold接口测试
                        self.sendData(self.creatCommand(
                            command=["command", "call", "hold", [{"callitem": self.callitem}], "bool"]))
                        self.log('调用 hold')
                        self.state += 1
        elif self.state == 5:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'hold'):
                    if self.checkResult(data):
                        self.log('等待 hold')
                        self.state += 1
                    else:
                        self.log('hold 调用失败')
                        return 2
        elif self.state == 6:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['hold'] is True:
                        # enableUploadVideoStream接口测试
                        self.sendData(self.creatCommand(
                            command=["command", "call", "enableUploadVideoStream", [{"callitem": self.callitem}],
                                     "bool"]))
                        self.log('调用 enableUploadVideoStream')
                        self.state += 1
        elif self.state == 7:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'enableUploadVideoStream'):
                    if self.checkResult(data):
                        self.log("等待 enableUploadVideoStream")
                        self.state += 1
                    else:
                        self.log("enableUploadVideoStream 调用失败")
                        return 2
        elif self.state == 8:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['uploadVideoStreamSelf'] is False:
                        # audioRecord 开启接口测试
                        self.sendData(self.creatCommand(
                            command=["command", "call", "audioRecord",
                                     [{"callitem": data['arg0']}, {"bool": True}, {
                                         "string": '/storage/emulated/0/juphoon_cloud/audio_record/test100.wmv'}],
                                     "bool"]))
                        self.log('调用 audioRecord true 命令')
                        self.state += 1
        elif self.state == 9:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'audioRecord'):
                    if self.checkResult(data):
                        self.log("等待 audioRecord true")
                        self.state += 1
                    else:
                        self.log(" audioRecord true 调用失败")
                        return 2
        elif self.state == 10:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['audioRecord'] is True:
                        # audioRecord 关闭接口测试
                        self.sendData(self.creatCommand(command=["command", "call", "audioRecord",
                                                                 [{"callitem": data['arg0']}, {"bool": False},
                                                                  {"string": ''}],
                                                                 "bool"]))
                        self.log('调用 audioRecord False 命令')
                        self.state += 1
        elif self.state == 11:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'audioRecord'):
                    if self.checkResult(data):
                        self.log("等待 audioRecord False调用")
                        self.state += 1
                    else:
                        self.log(" audioRecord False调用失败")
                        return 2
        elif self.state == 12:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['audioRecord'] is False:
                        # sendMessage接口测试
                        self.sendData(self.creatCommand(command=["command", "call", "sendMessage",
                                                                 [{"callitem": data['arg0']}, {"string": 'text'},
                                                                  {"string": 'this is a testMessage'}, ],
                                                                 "bool"]))
                        self.log(" 调用 sendMessage")
                        self.state += 1
        elif self.state == 13:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'sendMessage'):
                    if self.checkResult(data):
                        # VideoRecord 开启录制远端视频流 接口测试
                        self.sendData(self.creatCommand(command=["command", "call", "videoRecord",
                                                                 [{"callitem": self.callitem}, {"bool": True},
                                                                  {"bool": True}, {"int": 640}, {"int": 360}, {
                                                                      "string": "/storage/emulated/0/juphoon_cloud/audio_record/test100_audio.wmv"}],
                                                                 "bool"]))
                        self.log('调用 remoteVideoRecord True')
                        self.state += 1
                    else:
                        self.log('sendMessage 调用失败')
                        return 2
        elif self.state == 14:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'videoRecord'):
                    if self.checkResult(data):
                        self.log('等待 remoteVideoRecord True')
                        self.state += 1
                    else:
                        self.log('remoteVideoRecord True 调用失败')
                        return 2
        elif self.state == 15:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['remoteVideoRecord'] is True:
                        # VideoRecord 关闭录制远端视频流 接口测试
                        self.sendData(self.creatCommand(command=["command", "call", "videoRecord",
                                                                 [{"callitem": data['arg0']}, {"bool": False},
                                                                  {"bool": True}, {"int": 0}, {"int": 0}, {
                                                                      "string": ""}],
                                                                 "bool"]))
                        self.log("调用 remoteVideoRecord False")
                        self.state += 1
        elif self.state == 16:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'videoRecord'):
                    if self.checkResult(data):
                        self.log("等待 remoteVideoRecord False")
                        self.state += 1
                    else:
                        self.log("remoteVideoRecord False 调用失败")
                        return 2
        elif self.state == 17:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemUpdate'):
                    self.callitem = json.loads(data['arg0'])
                    if self.callitem['remoteVideoRecord'] is False:
                        # getConference 接口测试
                        self.sendData(self.creatCommand(
                            command=["command", "call", "getConference", [],
                                     "bool"]))
                        self.log('调用 getConference 命令')
                        self.state += 1
        elif self.state == 18:
            if data:
                self.showData(data)
                if self.waitMethod(data, 'getConference'):
                    if self.checkResult(data):
                        self.log("当前会议为音频")
                        self.state += 1
                    else:

                        self.log("当前会议为视频")
                        self.state += 1
        elif self.state == 19:
            # term 接口测试
            self.sendData(self.creatCommand(
                command=["command", "call", "term", [{"callitem": self.callitem}, {"int": 0}, {"string": ''}, ],
                         "bool"]))
            self.log('调用 term 命令')
            self.state += 1

        elif self.state == 20:
            if data:
                self.showData(data)
                if self.waitCallBack(data, 'onCallItemRemove'):
                    self.log('term 成功')
                    return 1

        if self.isTimeout(60) is True:
            self.log('超时')
            return 2

        return 0
