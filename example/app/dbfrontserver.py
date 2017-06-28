# -*- coding:utf-8 -*-

from gfirefly.server.globalobject import GlobalObject


def doWhenStop():
    """
        服务器关闭前的处理
    """
    print "###############"
    print "server stop"


GlobalObject().stophandler = doWhenStop
