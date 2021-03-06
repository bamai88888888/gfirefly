# -*- coding:utf-8 -*-

import time
from socket import AF_INET, SOCK_STREAM, socket
import struct


HOST = "localhast"
PORT=1000
BUFSIZE = 1024
ADDR = (HOST, PORT)
client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)


def sendData(sendstr, commandId):
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I', HEAD_0, HEAD_1, HEAD_2, HEAD_3, ProtoVersion,
                       ServerVersion, len(sendstr) + 4, commandId)
    senddata = data+ sendstr
    return senddata


def resolveRecvdata(data):
    head = struct.unpack('!sssss3I', data[:17])
    length = head[6]
    data = data[17:17+length]
    return data

s1 = time.time()


def start():
    for commandId in (100, 200, 300):
        print "---------------"
        print "send commandId:", commandId
        client.sendall(sendData('asdfe', commandId))
        print resolveRecvdata(client.recv(BUFSIZE))

start()
