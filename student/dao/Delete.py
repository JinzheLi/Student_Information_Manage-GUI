#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 21:09
# @Author  : 李金哲
# @Site    : 
# @File    : Delete.py
# @Software: PyCharm
from .Select import Select
from _pycache_.model import Model
import wx
import wx.grid


class Delete(Select):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Delete, self).__init__(*args, **kw)
        # 创建删除信息输入框、删除按钮
        self.del_id = wx.TextCtrl(self.pnl, pos=(407, 78), size=(210, 25))
        self.del_button = wx.Button(self.pnl, label="删除", pos=(625, 78), size=(80, 25))
        # 为删除按钮组件绑定事件处理
        self.del_button.Bind(wx.EVT_BUTTON, self.DelButton)

        # 创建静态框
        sb_del = wx.StaticBox(self.pnl, label="请选择需要删除的学生学号")
        # 创建水平方向box布局管理器
        hsbox_del = wx.StaticBoxSizer(sb_del, wx.HORIZONTAL)
        # 添加到hsbox_name布局管理器
        hsbox_del.Add(self.del_id, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(hsbox_del, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.menu()

    def DelButton(self, event):
        # 连接数据库
        mod = Model('stu')
        # 获取删除学生信息
        del_id = self.del_id.GetValue()

        # 删除学生信息
        if mod.delete(str(del_id)) > 0:
            class App(wx.Frame):
                """报错窗口"""
                def __init__(self):
                    wx.Frame.__init__(self, None, -1, '消息窗口', size=(250, 100))
                    panel = wx.Panel(self, -1)
                    wx.StaticText(panel, -1, '学生信息删除成功！！', pos=(70, 20))
                    self.Center()

            app = wx.App()
            frame = App()
            frame.Show(True)
            app.MainLoop()

        else:
            class App(wx.Frame):
                """报错窗口"""
                def __init__(self):
                    wx.Frame.__init__(self, None, -1, '消息窗口', size=(250, 100))
                    panel = wx.Panel(self, -1)
                    wx.StaticText(panel, -1, '学生信息删除失败！！', pos=(70, 20))
                    self.Center()

            app = wx.App()
            frame = App()
            frame.Show(True)
            app.MainLoop()

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
            pass

        elif num == 13:
            self.Close()
