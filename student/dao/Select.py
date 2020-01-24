#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 8:26
# @Author  : 李金哲
# @Site    : 
# @File    : Select.py
# @Software: PyCharm
from .OperationWind import OperationWind
from _pycache_.model import Model
import wx
import wx.grid


class Select(OperationWind):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(Select, self).__init__(*args, **kw)
        # 创建学生信息网格
        self.stu_grid = self.CreateGrid()
        # 添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(self.stu_grid, 0, wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 30)

    def CreateGrid(self):
        # 连接数据库
        mod = Model('stu')
        # 获取s表中的学生信息
        stu_data = mod.findAll()

        column_names = ('学号', '姓名', '年龄', '性别', '院系', '专业', '班级', '年级')
        key_word = ('id', 'name', 'age', 'sex', 'Sdept', 'profession', 'classid', 'grade')

        stu_grid = wx.grid.Grid(self.pnl)
        stu_grid.CreateGrid(len(stu_data), len(stu_data[0]) - 1)
        for row in range(len(stu_data)):
            # 确保网格序列号与数据库学生的学号一直
            stu_grid.SetRowLabelValue(row, str(stu_data[row]['id']))
            for col in range(1, len(column_names)):
                stu_grid.SetColLabelValue(col - 1, column_names[col])
                stu_grid.SetCellValue(row, col - 1, str(stu_data[row][key_word[col]]))
        stu_grid.AutoSize()
        return stu_grid

    def ClickButton(self, event):
        num = event.GetId()
        if num == 10:
            pass
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
