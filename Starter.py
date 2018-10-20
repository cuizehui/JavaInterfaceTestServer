#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

from twisted.internet import protocol, reactor
from time import ctime, sleep
import json
import threading
from ScriptManager import *
import socket

PORT = 9999
SEPERATE = '\r\n'

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 监听连接连入
class JCProtocol(protocol.Protocol):

    def __init__(self):
        self.number = ''
        self.beginTime = 0
        self.start = False
        self.buffer = ''
        self.packages = []
        self.mutex = threading.Lock()
        self.scriptManger = ScriptManager(self.aysnSendData)

    def connectionMade(self):
        print('********连接进入')
        self.start = True
        self.beginTime = time.time()
        reactor.callInThread(self.run)

    def connectionLost(self, reason):
        print('********连接断开')
        self.start = False

    def dataReceived(self, data):
        self.buffer += data.decode('utf-8')
        self.dealData()

    # 处理数据
    def dealData(self):
        while True:
            index = self.buffer.find(SEPERATE)
            if index != -1:
                package = self.buffer[0:index]
                print(package)
                try:
                    self.mutex.acquire()
                    self.packages.append(json.loads(package))
                except:
                    print('json parse error')
                    self.transport.loseConnection()
                finally:
                    self.mutex.release()
                self.buffer = self.buffer[index + len(SEPERATE):]
            else:
                break

    # 脚本线程中执行
    def run(self):
        while self.start:
            obj = None
            # 处理包
            self.mutex.acquire()
            if len(self.packages) > 0:
                obj = self.packages[0]
                self.packages.pop(0)
            self.mutex.release()

            self.scriptManger.run(obj)

            sleep(1)

    def aysnSendData(self, data):
        if data == 'close':
            reactor.callFromThread(lambda: self.transport.loseConnection())
        else:
            reactor.callFromThread(lambda: self.transport.write(data.encode('utf-8')))


factory = protocol.Factory()
factory.protocol = JCProtocol

print(get_host_ip(), '等待连接。。。')
reactor.listenTCP(PORT, factory)
reactor.run()
