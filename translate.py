# -*- coding: utf-8 -*-
'''
File Name: translate
Created on 2015年1月31日 上午11:13:54

@author: jay
'''
import os,logging
class Translate(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.log = logging.getLogger('main.translate') 
        
    def StartTranslate(self,srcfile,reffile):
        self.log.info("Translate file"+srcfile+" refer file"+reffile)
        if not self.Open(srcfile):
            return False
        
        self.Read()
        self.Close()
        
            
    def selftest(self):
        self.StartTranslate("Translate.txt", "")
    
if __name__=="__main__":
    tl=Translate(None)
    tl.selftest()