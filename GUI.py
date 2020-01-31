import wx, wx.lib.mixins.inspection
from string import ascii_uppercase
from os.path import realpath, dirname, join

class m2ngulaud(wx.Panel):
   "Mängu ajal kasutatav paneel, nupud flickerivad, peab teistesse state'idess bitmappe panema"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]
      self.SetBackgroundColour('#222222')
      # self.SetMinSize((1006, 491))

      tagasibtn = wx.Button(self, label='Tagasi')
      tagasibtn.Bind(wx.EVT_BUTTON, self.kinni)
      sizer = wx.BoxSizer()
      self.laudSizer = wx.BoxSizer()
      sizer.Add(tagasibtn)

      self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL))
      self.laudSizer.AddStretchSpacer()
      self.parent.coords = self.TeeLaud()
      self.laudSizer.Add(self.parent.coords,1, wx.CENTER)
      self.laudSizer.Add(self.TeeLaud(True), 1, wx.CENTER)
      self.laudSizer.AddStretchSpacer()
      sizer.Add(self.laudSizer, 0, wx.CENTER|wx.EXPAND)
      self.SetSizer(sizer)
   
   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()

   def TeeLaud(self, AI=False):
      "Mängu ruudustik tegemine"
      
      grid = wx.GridSizer(11, 11, 0, 0)
      cells = []
      grid.Add(wx.StaticText(self))
      grid.AddMany([(wx.StaticText(self, label=str(num)),0,wx.ALIGN_CENTER) for num in range(1, 11)])
      if AI:
         pool = 'C'
      else: 
         pool = ''
      text = 0
      size = int(wx.DisplaySize()[1] * 0.5 / 10)
      size = (size, size)
      for i in range(110):
         if i in [x for x in range(0, 100, 11)]:
            cells.append((wx.StaticText(self, label=list(ascii_uppercase)[i//11]),0, wx.ALIGN_CENTER))
            text += 1
         else:
            name = str(i-text) + pool
            #bitmap=wx.StandardPaths.Get().GetDataDir()+ peaks olema exe puhul vist
            if i in (3, 19, 30, 69, 85):
               btn = wx.BitmapButton(self, size=size, bitmap=wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),'aship.png')).Rescale(50,50), wx.BITMAP_TYPE_PNG), name=name)
            else:
               btn = wx.BitmapButton(self, size=size, bitmap=wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),'meri.png')).Rescale(50,50), wx.BITMAP_TYPE_PNG), name=name)
            btn.name = name
            if not AI:
               btn.Bind(wx.EVT_BUTTON, self.coord)
            cells.append((btn,0))
      # for cell in cells:
      #    print(cell)
      #    if isinstance(cell[0], wx._core.StaticText):
      #       cell[0].SetForegroundColour('#5e97bf')
      #       print('värvitud')
      grid.AddMany(cells)
      for cell in grid.GetChildren():
         cell = cell.GetWindow()
         if isinstance(cell, wx._core.StaticText):
            cell.SetForegroundColour('#5e97bf')
      return grid
   
   def coord(self, event):
      "Edastab (kuhugi?) ruudustikule tehtud kliki koordinaadid: [y, x]"
      name = event.GetEventObject().name
      if len(name) == 1:
         return print([0, int(name[0])])
      return print([int(name[0]), int(name[1])])

class MainMenu(wx.Panel):
   "Põhimenuu paneel"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.SetBackgroundColour('#222222')
      self.parent = args[0]
      sizer = wx.BoxSizer()
      vsizer = wx.BoxSizer(wx.VERTICAL)

      m2ngibtn = wx.Button(self, label='Mängi', style=wx.BORDER_NONE)
      m2ngibtn.Bind(wx.EVT_BUTTON, self.m2ngi)
      m2ngibtn.SetBackgroundColour('#DCAB4F')

      kinnibtn = wx.Button(self, label='Kinni', style=wx.BORDER_NONE)
      kinnibtn.Bind(wx.EVT_BUTTON, lambda a: self.parent.Close())
      kinnibtn.SetBackgroundColour('#DCAB4F')
      
      sizer.AddStretchSpacer(prop=3)
      vsizer.AddStretchSpacer(prop=30)
      vsizer.Add(m2ngibtn,10,wx.CENTER|wx.EXPAND)
      vsizer.AddStretchSpacer(prop=1)
      vsizer.Add(kinnibtn,10,wx.CENTER|wx.EXPAND)
      vsizer.AddStretchSpacer(prop=30)
      sizer.Add(vsizer, 2, wx.EXPAND)
      sizer.AddStretchSpacer(prop=3)
      self.SetSizer(sizer)

   def m2ngi(self, event):
      self.Hide()
      self.parent.laud.Show()
      self.parent.Layout()

class MainFrame(wx.Frame):
   "Akna raam, mille sees on paneelid"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      # self.size = kwargs['size']
      
      self.InitUI()
      self.Centre()
      self.Show()
      

   def InitUI(self):
      paneelisizer = wx.BoxSizer()
      self.menu = MainMenu(self)
      self.laud = m2ngulaud(self)
      self.laud.Hide()
      paneelisizer.AddMany([(self.menu,1,wx.EXPAND),(self.laud,1,wx.EXPAND)])
      self.SetSizer(paneelisizer)

class app(wx.App):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE ^ wx.RESIZE_BORDER
      size = wx.DisplaySize()
      self.MF = MainFrame(None, title='Laevade pommitamine', style=style, size=size)
      wx.lib.inspection.InspectionTool().Show()
      self.MainLoop()
   
def m2nguseis(gui):
   "BROKEN"
   children = gui.MF.laud.laudSizer.GetChildren()
   for child in children:
      child = child.GetWindow()
      name = child.name
      if len(name) == 1:
         print([0, int(name[0])])
      print([int(name[0]), int(name[1])])
   

if __name__ == '__main__':
   gui = app()
   # m2nguseis(gui)