#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 17:38
# @Author  : 李金哲
# @Site    : 
# @File    : Add.py
# @Software: PyCharm

from .OperationWind import OperationWind
from _pycache_.model import Model
import wx
import wx.grid


class Add(OperationWind):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Add, self).__init__(*args, **kw)
        # 创建添加学生信息输入框、添加按钮
        self.stu_id = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_name = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_age = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_gender = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_sde = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_pro = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_class = wx.TextCtrl(self.pnl, size=(210, 20))
        self.stu_grade = wx.TextCtrl(self.pnl, size=(210, 20))
        self.add_button = wx.Button(self.pnl, label="添加", size=(80, 20))
        self.update_button = wx.Button(self.pnl, label="修改", size=(80, 20))
        # 为添加按钮组件绑定事件处理
        self.add_button.Bind(wx.EVT_BUTTON, self.AddButton)
        # 为修改按钮组件绑定事件处理
        self.update_button.Bind(wx.EVT_BUTTON, self.UpdateButton)

        # 创建静态框
        input_id = wx.StaticBox(self.pnl, label="学  号")
        input_name = wx.StaticBox(self.pnl, label="姓  名")
        input_age = wx.StaticBox(self.pnl, label="年  龄")
        input_gender = wx.StaticBox(self.pnl, label="性  别")
        input_sde = wx.StaticBox(self.pnl, label="学  院")
        input_pro = wx.StaticBox(self.pnl, label="专  业")
        input_class = wx.StaticBox(self.pnl, label="班  级")
        inputu_grade = wx.StaticBox(self.pnl, label="年  级")

        # 创建水平方向box布局管理器
        hsbox_id = wx.StaticBoxSizer(input_id, wx.HORIZONTAL)
        hsbox_name = wx.StaticBoxSizer(input_name, wx.HORIZONTAL)
        hsbox_age = wx.StaticBoxSizer(input_age, wx.HORIZONTAL)
        hsbox_gender = wx.StaticBoxSizer(input_gender, wx.HORIZONTAL)
        hsbox_sde = wx.StaticBoxSizer(input_sde, wx.HORIZONTAL)
        hsbox_pro = wx.StaticBoxSizer(input_pro, wx.HORIZONTAL)
        hsbox_class = wx.StaticBoxSizer(input_class, wx.HORIZONTAL)
        hsbox_grade = wx.StaticBoxSizer(inputu_grade, wx.HORIZONTAL)

        # 添加到hsbox布局管理器
        hsbox_id.Add(self.stu_id, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_name.Add(self.stu_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_age.Add(self.stu_age, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_gender.Add(self.stu_gender, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_sde.Add(self.stu_sde, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_pro.Add(self.stu_pro, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_class.Add(self.stu_class, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_grade.Add(self.stu_grade, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(hsbox_id, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_name, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_age, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_gender, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_sde, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_pro, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_class, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(hsbox_grade, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(self.add_button, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)
        self.vsbox_show_operation.Add(self.update_button, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 5)

        self.menu()

    def AddButton(self, event):
        key_word = {'id': self.stu_id.GetValue(), 'name': self.stu_name.GetValue(), 'age': self.stu_age.GetValue(),
                    'sex': self.stu_gender.GetValue(), 'Sdept': self.stu_sde.GetValue(), 'profession': self.stu_pro.GetValue(),
                    'classid': self.stu_class.GetValue(), 'grade': self.stu_grade.GetValue()}
        # 连接数据库
        mod = Model('stu')
        # 保存学生信息,获取保存结果
        if mod.save(key_word) > 0:
            class App(wx.Frame):
                """报错窗口"""
                def __init__(self):
                    wx.Frame.__init__(self, None, -1, '消息窗口', size=(250, 100))
                    panel = wx.Panel(self, -1)
                    wx.StaticText(panel, -1, '学生信息添加成功！！', pos=(70, 20))
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
                    wx.StaticText(panel, -1, '学生信息添加失败！！', pos=(70, 20))
                    self.Center()

            app = wx.App()
            frame = App()
            frame.Show(True)
            app.MainLoop()

    def UpdateButton(self, event):
        key_word = {'id': self.stu_id.GetValue(), 'name': self.stu_name.GetValue(), 'age': self.stu_age.GetValue(),
                    'sex': self.stu_gender.GetValue(), 'Sdept': self.stu_sde.GetValue(),
                    'profession': self.stu_pro.GetValue(),
                    'classid': self.stu_class.GetValue(), 'grade': self.stu_grade.GetValue()}
        # 连接数据库
        mod = Model('stu')
        # 保存学生信息,获取保存结果
        if mod.update(key_word) > 0:
            class App(wx.Frame):
                """报错窗口"""

                def __init__(self):
                    wx.Frame.__init__(self, None, -1, '消息窗口', size=(250, 100))
                    panel = wx.Panel(self, -1)
                    wx.StaticText(panel, -1, '学生信息修改成功！！', pos=(70, 20))
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
                    wx.StaticText(panel, -1, '学生信息修改失败！！', pos=(70, 20))
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
            pass

        elif num == 12:
            print("删除操作！")
            from .Delete import Delete
            add_wind = Delete(None, title="学生信息管理系统", name=self.GetName(), size=(1024, 668))
            add_wind.Show()
            self.Close()

        elif num == 13:
            self.Close()
