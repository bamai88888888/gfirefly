# -*- coding:utf-8 -*-

from gfirefly.server.globalobject import GlobalObject, remoteserviceHandle


@remoteserviceHandle("gate")
def game1end(data):
    print "game1end handle", data
    return "game1end ok"
