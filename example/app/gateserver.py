# -*- coding:utf-8 -*-
from gfirefly.server.globalobject import GlobalObject, rootserviceHandle


@rootserviceHandle
def gatehandle(data):
    print "gatehandle:", data
    return "gate ok"


@rootserviceHandle
def game1handle(data):
    print "gate forward to game1"
    return GlobalObject().root.callChild("game1", "game1end", data)
