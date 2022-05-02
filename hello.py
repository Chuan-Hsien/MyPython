#/usr/bin/python
import wx
class MyFrame(wx.Frame):
    def __init__(self,*argc, **kwargc):
        super().__init__(*argc, **kwargc)
        self.InitUI()
    def InitUI(self):
        self.Centre()

def main():
    app=wx.App()
    win=MyFrame(None, title='HelloWorld')
    win.Show()
    app.MainLoop()

if __name__=='__main__':
    main()
    