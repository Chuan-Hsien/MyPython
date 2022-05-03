#/usr/bin/python
import wx
class MyFrame(wx.Frame):
    def __init__(self,*argc, **kwargc):
        super().__init__(*argc, **kwargc)
        self.InitUI()

    def InitUI(self):
        xbar=wx.MenuBar()
        xmenu=wx.Menu()
        xitem=xmenu.Append(wx.ID_ABORT,"&Quit","Program END")
        self.Bind(wx.EVT_MENU, self.onQuit, xitem)
        xitem=xmenu.Append(wx.ID_ANY,"&Info","Get information")
        self.Bind(wx.EVT_MENU, self.onInfo, xitem)
        xbar.Append(xmenu, title="&File")
        self.SetMenuBar(xbar)
        #self.CreateStatusBar()
        self.statusBar=wx.StatusBar(self)
        self.statusBar.SetStatusText("ChiuCS ERP")
        self.SetStatusBar(self.statusBar)

        #x=wx.Panel(self)
        self.btn1=wx.Button(self, label="Click btn1!")
        self.Bind(wx.EVT_BUTTON, self.OnClock, self.btn1)
        self.btn2=wx.Button(self, label="Click btn2!")
        self.Bind(wx.EVT_BUTTON, self.OnClock, self.btn2)
        x=wx.BoxSizer(wx.VERTICAL)
        x.Add(self.btn1)
        x.Add(self.btn2)
        self.SetSizer(x)
        self.Centre()
    def onQuit(self, event):
        ret=wx.MessageBox("Are You Sure?","QUIT!",wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if ret==wx.YES or ret==wx.OK:
            self.Close()
        else:
            pass
    def onInfo(self, e):
        n=self.statusBar.GetFieldsCount()
        print(n)
    def OnClock(self, e):
        print('Clock!')
        print(self)
        obj=e.GetEventObject()
        print(obj.GetLabel())
        if obj == self.btn1:
            print('btn1')
        print(e.GetId())
        print(e.GetEventType())
        print(wxEVT_BUTTON)
        #ret = wx.MessageBox("Clicked", "Info!", wx.OK|wx.ICON_EXCLAMATION)
        #ret = wx.MessageBox("Clicked", "Info!", wx.OK|wx.ICON_ERROR)
        #ret = wx.MessageBox("Clicked", "Info!", wx.OK|wx.ICON_INFORMATION)
        #ret = wx.MessageBox("Clicked", "Info!", wx.OK|wx.ICON_EXCL)

def main():
    app=wx.App()
    win=MyFrame(None, title='HelloWorld')
    win.Show()
    app.MainLoop()

if __name__=='__main__':
    main()
    