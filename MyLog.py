# -*- coding: utf-8 -*-
'''
File Name: MyLog
Created on 2015年1月31日 上午11:21:24

@author: jay
'''
import logging,time
class MyLogHandler(logging.Handler):
    def __init__(self,obj):
        logging.Handler.__init__(self)
        self.Object = obj

    def emit(self,record):
        if record.levelno<self.level: return
        tstr = time.strftime('%H:%M:%S')
        #self.Object.AppendText("[%s][%s]%s %s\n"%(tstr,record.levelname,record.filename,record.getMessage()));
        self.Object.AppendText("[%s][%s] %s\n"%(tstr,record.levelname,record.getMessage()))
