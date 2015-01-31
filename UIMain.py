# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 657,731 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer13 = wx.GridSizer( 0, 3, 0, 0 )
        
        m_choice_pro_typeChoices = []
        self.m_choice_pro_type = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_pro_typeChoices, 0 )
        self.m_choice_pro_type.SetSelection( 0 )
        self.m_choice_pro_type.SetToolTipString( u"产品类型" )
        
        gSizer13.Add( self.m_choice_pro_type, 0, wx.ALL, 5 )
        
        m_choice_pro_classChoices = []
        self.m_choice_pro_class = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_pro_classChoices, 0 )
        self.m_choice_pro_class.SetSelection( 0 )
        self.m_choice_pro_class.SetToolTipString( u"产品种类" )
        
        gSizer13.Add( self.m_choice_pro_class, 0, wx.ALL, 5 )
        
        m_choice_pro_targetChoices = []
        self.m_choice_pro_target = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_pro_targetChoices, 0 )
        self.m_choice_pro_target.SetSelection( 0 )
        self.m_choice_pro_target.SetToolTipString( u"产品名称" )
        
        gSizer13.Add( self.m_choice_pro_target, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( gSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        gSizer14 = wx.GridSizer( 0, 3, 0, 0 )
        
        self.m_buttonA = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer14.Add( self.m_buttonA, 0, wx.ALL, 5 )
        
        self.m_buttonB = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer14.Add( self.m_buttonB, 0, wx.ALL, 5 )
        
        self.m_buttonC = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer14.Add( self.m_buttonC, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( gSizer14, 1, wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer6 )
        self.m_panel1.Layout()
        bSizer6.Fit( self.m_panel1 )
        self.m_notebook1.AddPage( self.m_panel1, u"Product", False )
        self.m_panel4 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer5.SetFlexibleDirection( wx.BOTH )
        fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Files" ), wx.VERTICAL )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_textCtrl_source = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.m_textCtrl_source.SetMinSize( wx.Size( 400,-1 ) )
        
        fgSizer1.Add( self.m_textCtrl_source, 0, wx.ALL, 5 )
        
        self.m_buttonsel_source = wx.Button( self.m_panel4, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_buttonsel_source, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer11.SetFlexibleDirection( wx.BOTH )
        fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_textCtrl_refo = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self.m_textCtrl_refo.SetMinSize( wx.Size( 400,-1 ) )
        
        fgSizer11.Add( self.m_textCtrl_refo, 0, wx.ALL, 5 )
        
        self.m_buttonsel_refo = wx.Button( self.m_panel4, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer11.Add( self.m_buttonsel_refo, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( fgSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        fgSizer5.Add( sbSizer1, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button_start = wx.Button( self.m_panel4, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer5.Add( self.m_button_start, 0, wx.ALL|wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer3.Add( fgSizer5, 0, wx.EXPAND, 5 )
        
        self.m_textCtrl_LOG = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer3.Add( self.m_textCtrl_LOG, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer3 )
        self.m_panel4.Layout()
        bSizer3.Fit( self.m_panel4 )
        self.m_notebook1.AddPage( self.m_panel4, u"Translate", True )
        
        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_choice_pro_type.Bind( wx.EVT_CHOICE, self.Select_ProType )
        self.m_choice_pro_class.Bind( wx.EVT_CHOICE, self.Select_ProClass )
        self.m_choice_pro_target.Bind( wx.EVT_CHOICE, self.Select_ProTarget )
        self.m_buttonsel_source.Bind( wx.EVT_BUTTON, self.SelectTranslateSource )
        self.m_buttonsel_refo.Bind( wx.EVT_BUTTON, self.SelectTranslateRefo )
        self.m_button_start.Bind( wx.EVT_BUTTON, self.StartTranslate )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Select_ProType( self, event ):
        event.Skip()
    
    def Select_ProClass( self, event ):
        event.Skip()
    
    def Select_ProTarget( self, event ):
        event.Skip()
    
    def SelectTranslateSource( self, event ):
        event.Skip()
    
    def SelectTranslateRefo( self, event ):
        event.Skip()
    
    def StartTranslate( self, event ):
        event.Skip()
    

