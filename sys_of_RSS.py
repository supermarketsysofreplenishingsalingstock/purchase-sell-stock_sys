# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"自动售货机系统（登录）", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"账号：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_LEFT_DOWN, self.login )
		self.m_button2.Bind( wx.EVT_LEFT_DOWN, self.gotosignup )
		self.m_button3.Bind( wx.EVT_BUTTON, self.logclear )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def login( self, event ):
		event.Skip()

	def gotosignup( self, event ):
		event.Skip()

	def logclear( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"进销存管理系统——注册", pos = wx.DefaultPosition, size = wx.Size( 500,333 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		bSizer10.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"姓名：            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer11.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl9, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"职位：            ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer12.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl11, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"输入密码：      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"再次输入密码：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer14.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl12, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button10, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer16, 1, wx.EXPAND, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,80 ), 0 )
		bSizer10.Add( self.m_textCtrl8, 0, wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button9.Bind( wx.EVT_LEFT_DOWN, self.signup )
		self.m_button10.Bind( wx.EVT_LEFT_DOWN, self.quit_action )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def signup( self, event ):
		event.Skip()

	def quit_action( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame7
###########################################################################

class MyFrame7 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"进货", pos = wx.DefaultPosition, size = wx.Size( 516,343 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"供应商名称     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer32.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer32.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"商品名称*       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		bSizer321.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer321.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer321, 1, wx.EXPAND, 5 )

		bSizer322 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText282 = wx.StaticText( self, wx.ID_ANY, u"商品编号        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText282.Wrap( -1 )

		bSizer322.Add( self.m_staticText282, 0, wx.ALL, 5 )

		self.m_textCtrl182 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 250,-1 ), 0 )
		bSizer322.Add( self.m_textCtrl182, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer322, 1, wx.EXPAND, 5 )

		bSizer323 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText283 = wx.StaticText( self, wx.ID_ANY, u"进货数量*       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )

		bSizer323.Add( self.m_staticText283, 0, wx.ALL, 5 )

		self.m_textCtrl183 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer323.Add( self.m_textCtrl183, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer323, 1, wx.EXPAND, 5 )

		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"生产日期        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		bSizer182.Add( self.m_staticText122, 0, wx.ALL, 5 )

		self.m_textCtrl132 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		bSizer182.Add( self.m_textCtrl132, 0, wx.ALL, 5 )

		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		bSizer182.Add( self.m_staticText132, 0, wx.ALL, 5 )

		self.m_textCtrl142 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer182.Add( self.m_textCtrl142, 0, wx.ALL, 5 )

		self.m_staticText142 = wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		bSizer182.Add( self.m_staticText142, 0, wx.ALL, 5 )

		self.m_textCtrl152 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		bSizer182.Add( self.m_textCtrl152, 0, wx.ALL, 5 )

		self.m_staticText152 = wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		bSizer182.Add( self.m_staticText152, 0, wx.ALL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 35,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer182.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer182.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer182.Add( self.m_textCtrl34, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"分", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer182.Add( self.m_staticText41, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer182, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"保质期           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer18.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		bSizer18.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer18.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer18.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer18.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		bSizer18.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer18.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer18.Add( self.m_textCtrl35, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"小时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer18.Add( self.m_staticText42, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer18, 1, wx.EXPAND, 5 )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"保质期至        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer181.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_textCtrl131 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		bSizer181.Add( self.m_textCtrl131, 0, wx.ALL, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"年", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer181.Add( self.m_staticText131, 0, wx.ALL, 5 )

		self.m_textCtrl141 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer181.Add( self.m_textCtrl141, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		bSizer181.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_textCtrl151 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		bSizer181.Add( self.m_textCtrl151, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		bSizer181.Add( self.m_staticText151, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer181, 1, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer2.Add( self.m_button21, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button22, wx.GBPosition( 0, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button23, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"提交", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gbSizer2.Add( self.m_button24, wx.GBPosition( 1, 12 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer31.Add( gbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"新订单", pos = wx.DefaultPosition, size = wx.Size( 475,585 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer324 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText284 = wx.StaticText( self, wx.ID_ANY, u"（会员号）     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText284.Wrap( -1 )

		bSizer324.Add( self.m_staticText284, 0, wx.ALL, 5 )

		self.m_textCtrl184 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer324.Add( self.m_textCtrl184, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer324, 1, wx.EXPAND, 5 )

		bSizer322 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText282 = wx.StaticText( self, wx.ID_ANY, u"商品编号        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText282.Wrap( -1 )

		bSizer322.Add( self.m_staticText282, 0, wx.ALL, 5 )

		self.m_textCtrl182 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 250,-1 ), 0 )
		bSizer322.Add( self.m_textCtrl182, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer322, 1, wx.EXPAND, 5 )

		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"商品名*          ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		bSizer321.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer321.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer321, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"规格              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer32.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer32.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer323 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText283 = wx.StaticText( self, wx.ID_ANY, u"数量*             ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )

		bSizer323.Add( self.m_staticText283, 0, wx.ALL, 5 )

		self.m_textCtrl183 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer323.Add( self.m_textCtrl183, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer323, 1, wx.EXPAND, 5 )

		bSizer325 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText285 = wx.StaticText( self, wx.ID_ANY, u"单价*             ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText285.Wrap( -1 )

		bSizer325.Add( self.m_staticText285, 0, wx.ALL, 5 )

		self.m_textCtrl185 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer325.Add( self.m_textCtrl185, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer325, 1, wx.EXPAND, 5 )

		bSizer326 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText286 = wx.StaticText( self, wx.ID_ANY, u"总价              ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText286.Wrap( -1 )

		bSizer326.Add( self.m_staticText286, 0, wx.ALL, 5 )

		self.m_textCtrl186 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer326.Add( self.m_textCtrl186, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer326, 1, wx.EXPAND, 5 )

		bSizer327 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText287 = wx.StaticText( self, wx.ID_ANY, u"（折扣）        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText287.Wrap( -1 )

		bSizer327.Add( self.m_staticText287, 0, wx.ALL, 5 )

		self.m_textCtrl187 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer327.Add( self.m_textCtrl187, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer327, 1, wx.EXPAND, 5 )

		bSizer329 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText289 = wx.StaticText( self, wx.ID_ANY, u"经办人员        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText289.Wrap( -1 )

		bSizer329.Add( self.m_staticText289, 0, wx.ALL, 5 )

		self.m_textCtrl189 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer329.Add( self.m_textCtrl189, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer329, 1, wx.EXPAND, 5 )

		bSizer3210 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2810 = wx.StaticText( self, wx.ID_ANY, u"员工编号        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2810.Wrap( -1 )

		bSizer3210.Add( self.m_staticText2810, 0, wx.ALL, 5 )

		self.m_textCtrl1810 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer3210.Add( self.m_textCtrl1810, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer3210, 1, wx.EXPAND, 5 )

		self.m_textCtrl63 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,50 ), 0 )
		bSizer31.Add( self.m_textCtrl63, 0, wx.ALL, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer2.Add( self.m_button21, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button22, wx.GBPosition( 0, 18 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"添加商品", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button23, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"提交", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gbSizer2.Add( self.m_button24, wx.GBPosition( 1, 18 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer31.Add( gbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"添加供应商", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"供应商名称*    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer32.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer32.Add( self.m_textCtrl18, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer322 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText282 = wx.StaticText( self, wx.ID_ANY, u"供应商编号     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText282.Wrap( -1 )

		bSizer322.Add( self.m_staticText282, 0, wx.ALL, 5 )

		self.m_textCtrl182 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 250,-1 ), 0 )
		bSizer322.Add( self.m_textCtrl182, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer322, 1, wx.EXPAND, 5 )

		bSizer323 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText283 = wx.StaticText( self, wx.ID_ANY, u"制造商名称     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )

		bSizer323.Add( self.m_staticText283, 0, wx.ALL, 5 )

		self.m_textCtrl183 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer323.Add( self.m_textCtrl183, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer323, 1, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"上一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer2.Add( self.m_button21, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"下一页", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button22, wx.GBPosition( 0, 18 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"添加商品", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button23, wx.GBPosition( 1, 8 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"提交", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gbSizer2.Add( self.m_button24, wx.GBPosition( 1, 18 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer31.Add( gbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer48.Add( self.m_dataViewListCtrl1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer48 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame8
###########################################################################

class MyFrame8 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"进销存管理系统——总功能", pos = wx.DefaultPosition, size = wx.Size( 500,398 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"功能总览", wx.DefaultPosition, wx.Size( 500,40 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		bSizer36.Add( self.m_staticText40, 0, wx.ALL, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		self.m_button28 = wx.Button( self, wx.ID_ANY, u"新增进货", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button28.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		bSizer38.Add( self.m_button28, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"新增订单", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		bSizer38.Add( self.m_button29, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"新增报损", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

		bSizer38.Add( self.m_button30, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer37.Add( bSizer38, 1, wx.EXPAND, 5 )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"员工管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"供应商管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button20, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"商品管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"进货管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"订单管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"报损管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.m_button24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer37.Add( bSizer39, 1, wx.EXPAND, 5 )


		bSizer36.Add( bSizer37, 1, wx.EXPAND, 5 )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer43.Add( self.m_staticText41, 0, wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer43.Add( self.m_staticText42, 0, wx.ALL, 5 )


		bSizer36.Add( bSizer43, 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_button33 = wx.Button( self, wx.ID_ANY, u"个人信息管理", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button33, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer40.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_button34 = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button34, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer40.Add( bSizer42, 1, wx.EXPAND, 5 )


		bSizer36.Add( bSizer40, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer36 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button28.Bind( wx.EVT_LEFT_DOWN, self.add_replenish )
		self.m_button29.Bind( wx.EVT_LEFT_DOWN, self.add_order )
		self.m_button30.Bind( wx.EVT_LEFT_DOWN, self.add_damage )
		self.m_button19.Bind( wx.EVT_LEFT_DOWN, self.employee_manage )
		self.m_button20.Bind( wx.EVT_LEFT_DOWN, self.supplier_manage )
		self.m_button21.Bind( wx.EVT_LEFT_DOWN, self.item_manage )
		self.m_button22.Bind( wx.EVT_LEFT_DOWN, self.replenish_manage )
		self.m_button24.Bind( wx.EVT_LEFT_DOWN, self.damage_manage )
		self.m_button33.Bind( wx.EVT_LEFT_DOWN, self.personalinfo_manage )
		self.m_button34.Bind( wx.EVT_LEFT_DOWN, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_replenish( self, event ):
		event.Skip()

	def add_order( self, event ):
		event.Skip()

	def add_damage( self, event ):
		event.Skip()

	def employee_manage( self, event ):
		event.Skip()

	def supplier_manage( self, event ):
		event.Skip()

	def item_manage( self, event ):
		event.Skip()

	def replenish_manage( self, event ):
		event.Skip()

	def damage_manage( self, event ):
		event.Skip()

	def personalinfo_manage( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()


