import wx,wx.html
import os
from arrangement import *
class myframe(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Infrastructure",size=(400,200))
        self.panel = wx.Panel(self)
        self.src_dir = wx.TextCtrl(self.panel, -1, pos= (10, 10), size = (300,-1))
        self.dest_dir = wx.TextCtrl(self.panel, -1, pos= (10, 80), size = (300,-1))
        self.button_move = wx.Button(self.panel, label = "Move", pos=(150,150), size = (90,-1))
        self.button_src_open = wx.Button(self.panel, label = "SrcOpen", pos=(310,10), size = (80,-1))
        self.button_dest_open = wx.Button(self.panel, label = "DstOpen", pos=(310,80), size = (80,-1))
        dirname = os.environ['HOME']
        self.src_dir.SetValue(dirname + '/Desktop')
        self.dest_dir.SetValue(dirname + '/Documents')
        self.Bind(wx.EVT_BUTTON, self.sopen, self.button_src_open)
        self.Bind(wx.EVT_BUTTON, self.dopen, self.button_dest_open)
        self.Bind(wx.EVT_BUTTON,self.arrang_move,self.button_move)
    def sopen(self,event):
        style=wx.OPEN
        fdialog=wx.DirDialog(self,'Open',style=style)
        if fdialog.ShowModal()==wx.ID_OK:
            self.path=fdialog.GetPath()
            self.src_dir.SetValue(self.path)
    def dopen(self,event):
        style=wx.OPEN
        fdialog=wx.DirDialog(self,'Open',style=style)
        if fdialog.ShowModal()==wx.ID_OK:
            self.path=fdialog.GetPath()
            self.dest_dir.SetValue(self.path)
    def arrang_move(self,event):
        src=self.src_dir.GetValue()
        dest=self.dest_dir.GetValue()
        src=src+"/"
        dest=dest+"/"
        arrange(src,dest)



if __name__=='__main__':
    app = wx.PySimpleApp()
    frame = myframe(None, -1)
    frame.Show()
    app.MainLoop()