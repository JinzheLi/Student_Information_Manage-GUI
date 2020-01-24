from dao.enter import User
import wx

if __name__ == '__main__':
    app = wx.App()
    enter = User(None, title="学生信息管理系统", size=(1024, 668))
    enter.Show()
    app.MainLoop()
