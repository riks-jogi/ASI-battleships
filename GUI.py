import wx, wx.lib.mixins.inspection
from string import ascii_uppercase

class m2ngulaud(wx.Panel):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]
      self.SetBackgroundColour('#333333')
      # self.SetMinSize((1006, 491))
      laudSizer = wx.BoxSizer(wx.HORIZONTAL)

      tagasibtn = wx.Button(self, label='Tagasi')
      tagasibtn.Bind(wx.EVT_BUTTON, self.kinni)
      laudSizer.Add(tagasibtn)

      self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL))
      laudSizer.AddMany([self.TeeLaud(), self.TeeLaud()])
      self.SetSizer(laudSizer)
   
   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()

   def TeeLaud(self):
      "Peab ümber tegema absolute pos'iga"
      grid = wx.GridSizer(11, 11, 1, 1)
      cells = [wx.StaticText(self)]
      cells += [wx.StaticText(self, label=str(num)) for num in range(1, 11)]
      for i in range(110):
         if i in [x for x in range(0, 100, 11)]:
            cells.append(wx.StaticText(self, label=list(ascii_uppercase)[i//11]))
         else:   
            cells.append((wx.Button(self, size=(40,40), name=str(i)), 1, wx.EXPAND))
      grid.AddMany(cells)
      return grid


class MainMenu(wx.Panel):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]

      sizer = wx.BoxSizer(wx.VERTICAL)
      m2ngibtn = wx.Button(self, label='Mängi')
      m2ngibtn.Bind(wx.EVT_BUTTON, self.m2ngi)

      kinnibtn = wx.Button(self, label='Kinni')
      kinnibtn.Bind(wx.EVT_BUTTON, lambda a: self.parent.Close())
      sizer.AddStretchSpacer()
      sizer.AddMany([(m2ngibtn,0,wx.CENTER), (kinnibtn,0,wx.CENTER)])
      sizer.AddStretchSpacer()

      self.SetSizer(sizer)

   def m2ngi(self, event):
      self.Hide()
      self.parent.laud.Show()
      self.parent.Layout()

class MainFrame(wx.Frame):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      # self.size = kwargs['size']
      
      self.InitUI()
      self.Centre()
      self.Show()

   def InitUI(self):
      fsizer = wx.BoxSizer()
      self.menu = MainMenu(self)
      self.laud = m2ngulaud(self)
      self.laud.Hide()
      #proportion = 1 - expandib vertically; flag=wx.EXPAND - expandib horizontali
      fsizer.AddMany([(self.menu,1,wx.EXPAND),(self.laud,1,wx.EXPAND)])
      self.SetSizer(fsizer)



def gui():
   app = wx.App()
   #style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER  #ei saa resizeda aken
   
   display = wx.DisplaySize()
   size = (int(display[0]*0.5), int(display[1]*0.5))  # Aken tuleb poole väiksem main monitor resost
   
   MainFrame(None, title='Laevade pommitamine', size=size)
   wx.lib.inspection.InspectionTool().Show()
   app.MainLoop()

if __name__ == '__main__':
   gui()