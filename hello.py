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

        x=wx.Panel(self)
        wx.Button(x, label="Click ME!", pos=(10,10), size=(100,100))

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

def main():
    app=wx.App()
    win=MyFrame(None, title='HelloWorld')
    win.Show()
    app.MainLoop()

if __name__=='__main__':
    main()
    