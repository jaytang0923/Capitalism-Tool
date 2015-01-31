# -*- coding: utf-8 -*-
'''
File Name: Main
Created on 2015年1月29日 上午9:46:20

@author: jay
'''
import UIMain
import product
import wx,os,logging
import chardet
import MyLog,translate
class Main(UIMain.MainFrame):
    def __init__(self,parent):
        UIMain.MainFrame.__init__(self, parent)
        
        ###log
        self.log = logging.getLogger('main')    # 获取名为tst的logger   
        self.log.addHandler(MyLog.MyLogHandler(self.m_textCtrl_LOG))           # 为logger添加handler   
        self.log.setLevel(logging.DEBUG)  

        self.m_choice_pro_type.SetItems([u"全部"]+list(product.TGOODS))
        self.m_choice_pro_type.SetSelection(0)
        self.m_choice_pro_class.SetItems([u"全部"]+list(product.CLA))
        self.m_choice_pro_class.SetSelection(0)
        self.m_choice_pro_target.SetItems(list(product.ProNames))
        self.m_choice_pro_target.SetSelection(0)
        
        
    def settingtargetlist(self):
        protype=self.m_choice_pro_type.GetStringSelection()
        proclass=self.m_choice_pro_class.GetStringSelection()
        print protype,proclass
        #self.m_choice_pro_type
        prolist=[]
        if protype == u"全部" and proclass == u"全部":
            prolist=list(product.ProNames)
        else:
            for pro in product.AllProducts:
                if protype == product.AllProducts[pro][0] and ( proclass == product.AllProducts[pro][1] or proclass == u"全部"):
                    prolist.append(pro)
                elif proclass == product.AllProducts[pro][1] and ( protype == product.AllProducts[pro][0] or protype == u"全部"):
                    prolist.append(pro)
        
        self.m_choice_pro_target.SetItems(prolist)
        self.m_choice_pro_target.SetSelection(0)
    
    def ShowStuffTree(self):
        stuf=[self.m_buttonA,self.m_buttonB,self.m_buttonC]
        proname=self.m_choice_pro_target.GetString(self.m_choice_pro_target.GetSelection())
        print proname
        #pro=product.AllProNames[proname]
        substf=product.SubStuff[proname]
        print substf,len(substf[0])
        #for stu in pro[4]:
        for i in range(len(substf[0])):
            name,num=substf[0][i]
            print name,num
            
            stuf[i].SetLabelText(name+' '+str(num))
    
    def Select_ProType(self,event):
        self.settingtargetlist()
    def Select_ProClass( self, event ):
        self.settingtargetlist()
    def Select_ProTarget( self, event ):
        self.ShowStuffTree()
        
    def SelectTranslateSource( self, event ):
        path=None
        wildcard = "TXT File (*.txt)|*.txt|" \
            "All files (*.*)|*.*"
        dialog =wx.FileDialog(None,'Select The Source Translate File',os.getcwd(),'',wildcard,wx.OPEN)
        if dialog.ShowModal()==wx.ID_OK:
            path=dialog.GetPath()
            self.m_textCtrl_source.SetLabel(path)
            self.sourcefile=path
            self.log.info("Source File :"+path)
        dialog.Destroy()
    
    def SelectTranslateRefo( self, event ):
        path=None
        wildcard = "TXT File (*.txt)|*.txt|" \
            "All files (*.*)|*.*"
        dialog =wx.FileDialog(None,'Select The Old Translate File',os.getcwd(),'',wildcard,wx.OPEN)
        if dialog.ShowModal()==wx.ID_OK:
            path=dialog.GetPath()
            self.m_textCtrl_refo.SetLabel(path)
            self.refofile=path
            self.log.info("Refer File :"+path)
        dialog.Destroy()
    
    def StartTranslate( self, event ):
        self.log.info("Start Translate")
        translate.Translate(None).StartTranslate(self.sourcefile,self.refofile)
        
class mainapp(wx.App):
    def __init__(self,redirect=False,filename=None):
        wx.App.__init__(self,redirect, filename) 
                  
        
    def OnInit(self):
        self.frame=Main(None)  
        self.frame.Show()
        
        return True
    
    
if __name__ == '__main__':
    app=mainapp()
    app.MainLoop()