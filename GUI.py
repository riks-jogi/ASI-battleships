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

      self.aship = wx.StaticBitmap(self, bitmap=self.loadbmp('aship.png'))
      self.aship.Bind(wx.EVT_LEFT_DOWN, self.lmbdown)
      self.Bind(wx.EVT_LEFT_UP, self.lmbup)
      self.Bind(wx.EVT_MOTION, self.motion)
      sizer.Add(self.aship)

      self.dragbmp = wx.DragImage(self.loadbmp('aship.png'))
      # s.Move()

      self.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL))
      self.laudSizer.AddStretchSpacer()
      self.laudSizer.Add(self.TeeLaud(),1, wx.SHAPED)
      self.laudSizer.Add(self.TeeLaud(True), 1, wx.SHAPED)
      self.laudSizer.AddStretchSpacer()
      sizer.Add(self.laudSizer, 0, wx.CENTER)
      self.SetSizer(sizer)

   def lmbdown(self, event):
      print('lmbdown')
      self.dragbmp.BeginDrag((0,0), self)
      self.dragbmp.Show()

   def lmbup(self, event):
      print('lmbup')
      self.dragbmp.EndDrag()

   def motion(self, event):
      print('motion')

   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()

   def TeeLaud(self, AI=False):
      "Mängu ruudustik tegemine"
      
      grid = wx.GridSizer(11, 11, 0, 0)
      cells = []
      
      size = int(wx.DisplaySize()[1] * 0.5 / 10)
      size = (size, size)
      grid.Add(wx.StaticText(self))
      
      for num in range(1,11):
         sizer = wx.BoxSizer()
         text = wx.StaticText(self, label=str(num))
         sizer.Add(text, 1, wx.ALIGN_CENTER|wx.SHAPED)
         grid.Add(sizer, 0, wx.EXPAND)
      # grid.AddMany([(wx.StaticText(self, label=str(num)), 0, wx.EXPAND) for num in range(1, 11)])
      if AI:
         pool = 'C'
      else: 
         pool = ''
      text = 0
      for i in range(110):
         if i in [x for x in range(0, 100, 11)]:
            cells.append((wx.StaticText(self, label=list(ascii_uppercase)[i//11]),0,wx.ALIGN_CENTER|wx.EXPAND))
            text += 1
         else:
            name = str(i-text) + pool
            #bitmap=wx.StandardPaths.Get().GetDataDir()+ peaks olema exe puhul vist
            if i in (3, 19, 30, 69, 85):
               btn = wx.BitmapButton(self, size=size, bitmap=self.loadbmp('aship.png'), name=name)
            else:
               btn = wx.BitmapButton(self, size=size, bitmap=wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),'meri.png')).Rescale(50,50), wx.BITMAP_TYPE_PNG), name=name)
            btn.name = name
            if AI:
               btn.Bind(wx.EVT_BUTTON, self.coord)
            cells.append((btn, 0, wx.EXPAND))
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
      "Edastab (kuhugi?) ruudustikule tehtud kliki koordinaadid: [row, column]"
      btn =  event.GetEventObject()
      btn.Disable()
      name = btn.name
      if len(name) == 2:
         return print([0, int(name[0])])
      return print([int(name[0]), int(name[1])])

   def loadbmp(self,file, bmp=True): 
      size = int(wx.DisplaySize()[1] * 0.5 / 10)
      size = (size, size)
      if bmp:
         return wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),file)).Rescale(size[0],size[0]))
      img = wx.Image(join(dirname(realpath(__file__)),file))
      img.Rescale(size[0],size[0])
      return img


class MainMenu(wx.Panel):
   "Põhimenuu paneel"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.SetBackgroundColour('#222222')
      self.parent = args[0]
      tsize = int(wx.DisplaySize()[1]*0.03)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      sizer = wx.BoxSizer()
      vsizer = wx.BoxSizer(wx.VERTICAL)

      self.nimi = False
      nimi = wx.TextCtrl(self)
      nimi.SetMaxLength(20)
      nimi.SetLabel('Nimi')
      nimi.Bind(wx.EVT_TEXT, self.name)

      self.tase = False
      tase = wx.ComboBox(self, value='Raskustase', choices=['Kerge','Keskmine','Raske'])
      tase.SetEditable(False)
      tase.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.raskus)

      m2ngibtn = wx.Button(self, label='Mängi', style=wx.BORDER_NONE)
      m2ngibtn.Bind(wx.EVT_BUTTON, self.m2ngi)
      m2ngibtn.SetBackgroundColour('#DCAB4F')

      kinnibtn = wx.Button(self, label='Kinni', style=wx.BORDER_NONE)
      kinnibtn.Bind(wx.EVT_BUTTON, lambda a: self.parent.Close())
      kinnibtn.SetBackgroundColour('#DCAB4F')
      
      sizer.AddStretchSpacer(prop=3)
      vsizer.AddStretchSpacer(prop=30)
      vsizer.Add(nimi,5,wx.EXPAND)     # fontsize upscalib kõike, peaks eraldi fondid panema
      vsizer.AddStretchSpacer(prop=1)
      vsizer.Add(tase,5,wx.EXPAND)
      vsizer.AddStretchSpacer(prop=1)
      vsizer.Add(m2ngibtn,10,wx.EXPAND)
      vsizer.AddStretchSpacer(prop=1)
      vsizer.Add(kinnibtn,10,wx.EXPAND)
      vsizer.AddStretchSpacer(prop=30)
      sizer.Add(vsizer, 2, wx.EXPAND)
      sizer.AddStretchSpacer(prop=3)
      self.SetSizer(sizer)

   def name(self, event):
      "annab m2ngija nime str()'ina"
      obj = event.GetEventObject()
      if obj.GetValue() == '':
         self.nimi = False
      else:
         self.nimi = obj.GetValue()
      return print(self.nimi)
   
   def raskus(self, event):
      "annab rasustaseme str()'ina"
      obj = event.GetEventObject()
      if obj.GetValue() != 'Raskustase':
         self.tase = obj.GetValue()
      return print(self.tase)

   def m2ngi(self, event):
      print(self.tase, self.nimi)
      if self.tase and self.nimi:
         self.Hide()
         self.parent.laud.Show()
         self.parent.Layout()

class MainFrame(wx.Frame):
   "Akna raam, mille sees on paneelid"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      # self.size = kwargs['size']
      self.SetBackgroundColour('#222222')
      
      self.InitUI()
      self.Centre()
      self.Show()
      self.resizing = False

      self.Bind(wx.EVT_SIZE, self.OnSize)
      self.Bind(wx.EVT_IDLE, self.OnIdle)

   def InitUI(self):
      paneelisizer = wx.BoxSizer()
      self.menu = MainMenu(self)
      self.laud = m2ngulaud(self)
      self.laud.Hide()
      paneelisizer.AddMany([(self.menu,1,wx.EXPAND),(self.laud,1,wx.EXPAND)])
      self.SetSizer(paneelisizer)

   def OnSize(self, event):
      self.resizing = True
      # self.Layout()
      # self.laud.Update()
      # self.Refresh()
      # if self.resizing:
      #    self.Freeze()
      #    self.Layout()
      #    self.Thaw()
      # self.resizing = False
      

   def OnIdle(self, event):
      # print(event)
      if self.resizing:
         self.resizing = False
         self.Freeze()
         self.Layout()
         self.Thaw()


class app(wx.App):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      style = wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE
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