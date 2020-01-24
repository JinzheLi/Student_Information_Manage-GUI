import wx
import wx.grid
from _pycache_.model import Model


# 创建学生信息管理系统登录界面类
class User(wx.Frame):
    """
    登录界面
    """

    # 初始化登录界面
    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)
        # 设置窗口屏幕居中
        self.Center()
        # 创建窗口
        self.pnl = wx.Panel(self)
        # 调用登录界面函数
        self.Enter()

    def Enter(self):
        # 创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 创建静态文本，设置字体属性
        title = wx.StaticText(self.pnl, label="学生信息管理系统")
        font = title.GetFont()
        font.PointSize += 30
        font = font.Bold()
        title.SetFont(font)

        # 添加静态文本到vbox布局管理器
        vbox.Add(title, proportion=0, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=180)
        # 创建静态框
        sb_username = wx.StaticBox(self.pnl, label="用户名")
        sb_password = wx.StaticBox(self.pnl, label="密  码")
        # 创建水平方向box布局管理器
        hsbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hsbox_password = wx.StaticBoxSizer(sb_password, wx.HORIZONTAL)
        # 创建用户名、密码输入框
        self.id = wx.TextCtrl(self.pnl, size=(210, 25))
        self.password = wx.TextCtrl(self.pnl, size=(210, 25), style=wx.TE_PASSWORD)
        # 添加用户名和密码输入框到hsbox布局管理器
        hsbox_username.Add(self.id, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox_password.Add(self.password, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 将水平box添加到垂直box
        vbox.Add(hsbox_username, proportion=0, flag=wx.CENTER)
        vbox.Add(hsbox_password, proportion=0, flag=wx.CENTER)
        # 创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        # 创建登录按钮、绑定事件处理
        login_button = wx.Button(self.pnl, label="登录", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON, self.Button)
        # 添加登录按钮到hbox布局管理器
        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        # 将水平box添加到垂直box
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)

        # 设置面板的布局管理器vbox
        self.pnl.SetSizer(vbox)

    def Button(self, event):
        # 连接数据库
        mod = Model('users')
        # 获取数据库中的全部管理用户
        userlist = mod.findAll()
        # 定义标记对象
        flag = False
        user = None
        for data in userlist:
            if str(data['id']) == self.id.GetValue() and data['password'] == self.password.GetValue():
                user = data['user']
                flag = True
                break
        if flag is False:
            print("用户名或密码错误！")

            class App(wx.Frame):
                """报错窗口"""
                def __init__(self):
                    wx.Frame.__init__(self, None, -1, '消息窗口', size=(250, 100))
                    panel = wx.Panel(self, -1)
                    wx.StaticText(panel, -1, '用户名或密码错误！', pos=(70, 20))
                    self.Center()

            app = wx.App()
            frame = App()
            frame.Show()
            app.MainLoop()

        else:
            print("登录成功！")
            from .OperationWind import OperationWind
            operation = OperationWind(None, title="学生信息管理系统", name=user, size=(1024, 668))
            operation.menu()
            operation.Show()
            self.Close()
