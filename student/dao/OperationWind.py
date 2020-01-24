#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 22:31
# @Author  : 李金哲
# @Site    :
# @File    : OperationWind.py
# @Software: PyCharm
import wx
import wx.grid


class OperationWind(wx.Frame):
    """
    操作界面
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(OperationWind, self).__init__(*args, **kw)

        # 设置窗口屏幕居中
        self.Center()
        # 创建窗口
        self.pnl = wx.Panel(self)
        # 调用操作界面函数
        self.OperationInterface()

    def OperationInterface(self):
        # 创建窗口
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # 设置字体属性
        title = wx.StaticText(self.pnl, label='管理员:' + self.GetName() + ' 欢迎光临本系统')
        font = title.GetFont()
        font.PointSize += 30
        font = font.Bold()
        title.SetFont(font)
        # 添加静态文本到vbox布局管理器
        self.vbox.Add(title, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=5)

        # 创建静态框
        sb_button = wx.StaticBox(self.pnl, label="选择操作")
        # 创建垂直方向box布局管理器
        vsbox_button = wx.StaticBoxSizer(sb_button, wx.VERTICAL)
        # 创建操作按钮、绑定事件处理
        check_button = wx.Button(self.pnl, id=10, label="查询、修改学生信息", size=(150, 50))
        add_button = wx.Button(self.pnl, id=11, label="添加学生信息", size=(150, 50))
        delete_button = wx.Button(self.pnl, id=12, label="删除学生信息", size=(150, 50))
        quit_button = wx.Button(self.pnl, id=13, label="退出系统", size=(150, 50))
        self.Bind(wx.EVT_BUTTON, self.ClickButton, id=10, id2=13)

        # 添加操作按钮到vsbox布局管理器
        vsbox_button.Add(check_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(add_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(delete_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vsbox_button.Add(quit_button, 0, wx.EXPAND | wx.BOTTOM, 200)
        # 创建静态框
        sb_show_operation = wx.StaticBox(self.pnl, label="显示/操作窗口", size=(800, 500))

        # 创建垂直方向box布局管理器
        self.vsbox_show_operation = wx.StaticBoxSizer(sb_show_operation, wx.VERTICAL)

        # 创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        hbox.Add(vsbox_button, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(self.vsbox_show_operation, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 将hbox添加到垂直box
        self.vbox.Add(hbox, proportion=0, flag=wx.CENTER)

        self.pnl.SetSizer(self.vbox)

    def menu(self):
        """设置菜单栏"""
        # 创建一个菜单栏
        menuBar = wx.MenuBar()
        # 创建一个菜单
        fileMenu = wx.Menu()
        # 创建一个子菜单
        editMenu = wx.Menu()
        # 创建三个子菜单的菜单项目
        selectItem = wx.MenuItem(editMenu, id=10, text="查询", kind=wx.ITEM_NORMAL)
        insertItem = wx.MenuItem(editMenu, id=11, text="插入", kind=wx.ITEM_NORMAL)
        updateItem = wx.MenuItem(editMenu, id=11, text="修改", kind=wx.ITEM_NORMAL)
        delItem = wx.MenuItem(editMenu, id=12, text="删除", kind=wx.ITEM_NORMAL)
        editMenu.Append(selectItem)
        editMenu.Append(insertItem)
        editMenu.Append(updateItem)
        editMenu.Append(delItem)

        # 把子菜单添加到菜单中
        fileMenu.Append(wx.ID_ANY, "基础操作", editMenu)
        # 添加一行线
        fileMenu.AppendSeparator()
        # 添加退出操作
        quit = wx.MenuItem(fileMenu, id=13, text="Quit\tCtrl+Q", kind=wx.ITEM_NORMAL)
        fileMenu.Append(quit)

        # 将 fileMenu 菜单添加到菜单栏中
        menuBar.Append(fileMenu, title='菜单')
        # 创建操作按钮、绑定事件处理
        self.Bind(wx.EVT_MENU, self.ClickButton)
        self.SetMenuBar(menuBar)

    def ClickButton(self, event):
        num = event.GetId()
        if num == 10:
            print("查询操作！")

            from .Select import Select
            select_wind = Select(None, title="学生信息管理系统", name=self.GetName(), size=(1024, 668))
            select_wind.menu()
            select_wind.Show()
            self.Close()

        elif num == 11:
            print("添加操作！")
            from .Add import Add
            add_wind = Add(None, title="学生信息管理系统", name=self.GetName(), size=(1024, 668))
            add_wind.Show()
            self.Close()

        elif num == 12:
            print("删除操作！")
            from .Delete import Delete
            add_wind = Delete(None, title="学生信息管理系统", name=self.GetName(), size=(1024, 668))
            add_wind.Show()
            self.Close()

        elif num == 13:
            self.Close()
