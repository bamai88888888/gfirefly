# -*- coding:utf-8 -*-
from gfirefly.server.globalobject import GlobalObject, netserviceHandle


@netserviceHandle
def nethandle_100(_conn, data):
    """
    conn是LiberateProtocol的实例（netconnect/protoc.py）
    """
    print "handle_100:", data
    return "nethandle_100 ok"


@netserviceHandle
def nethandle_200(_conn, data):
    return GlobalObject().remote['gate'].callRemote("gatehandle", data)


@netserviceHandle
def nethandle_300(_conn, data):
    return GlobalObject().remote['gate'].callRemote("game1handke", data)
