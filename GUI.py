from os.path import dirname, join, realpath
from random import randint
from string import ascii_uppercase

import wx, wx.lib.scrolledpanel
import wx.lib.mixins.inspection


class storypan(wx.Panel):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]
      size = wx.DisplaySize()
      tsize = int(size[1]*0.023)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      

      sizer = wx.BoxSizer()
      
      text = """
      Kurjad sead on ühe paganama kiire korvetti sokutanud teie tagalasse moosi varastama.
      Me ei saa neil põgeneda lasta, kähku moosivarusid päästma!!!
      """
      txt = wx.StaticText(self, label=text)
      txt.SetForegroundColour('#5e97bf')
      
      m2ngibtn = wx.Button(self, label='Järele neile!', style=wx.BORDER_NONE)
      m2ngibtn.Bind(wx.EVT_BUTTON, self.m2ngi)
      m2ngibtn.SetBackgroundColour('#DCAB4F')
      
      sizer.Add(m2ngibtn,0,wx.LEFT)
      sizer.Add(txt)
      self.SetSizer(sizer)

   def m2ngi(self, event):
      self.Hide()
      self.parent.laud.Show()
      self.parent.Layout()

class shop(wx.Panel):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]
      size = wx.DisplaySize()
      tsize = int(size[1]*0.023)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))

      sizer = wx.BoxSizer()
      
      tagasibtn = wx.Button(self, label='Tagasi', style=wx.BORDER_NONE)
      tagasibtn.Bind(wx.EVT_BUTTON, self.kinni)
      tagasibtn.SetBackgroundColour('#DCAB4F')

      sizer.Add(tagasibtn)
      self.SetSizer(sizer)
   
   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()

class infop(wx.lib.scrolledpanel.ScrolledPanel):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.parent = args[0]
      size = wx.DisplaySize()
      tsize = int(size[1]*0.023)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      
      sizer = wx.BoxSizer(wx.VERTICAL)
      h1sizer = wx.BoxSizer()
      h2sizer = wx.BoxSizer()
      
      txt = "Mängu on loonud 1}{nd grupp: Mihkel, Richard, Taeri, Georg."
      tegijad = wx.StaticText(self, label=txt)
      tegijad.SetForegroundColour('#5e97bf')
      
      tagasibtn = wx.Button(self, label='Tagasi', style=wx.BORDER_NONE)
      tagasibtn.Bind(wx.EVT_BUTTON, self.kinni)
      tagasibtn.SetBackgroundColour('#DCAB4F')

      loret = """*insert epically long heroic lore here*
      *insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*
      *insert epically long heroic lore here**insert epically long heroic lore here*"""
      lore = wx.StaticText(self, label=loret)
      lore.SetForegroundColour('#5e97bf')

      h1sizer.Add(tagasibtn)
      h1sizer.AddStretchSpacer(1)
      h1sizer.Add(tegijad,1,wx.CENTER)
      h1sizer.AddStretchSpacer(1)
      # h2sizer.AddStretchSpacer()
      h2sizer.Add(lore)
      # h2sizer.AddStretchSpacer(5)
      sizer.Add(h1sizer,1)
      sizer.AddStretchSpacer()
      sizer.Add(h2sizer,4,wx.ALIGN_CENTER)
      self.SetSizer(sizer)
      self.parent.Unbind(wx.EVT_SIZE)
      self.parent.Unbind(wx.EVT_IDLE)
      self.SetupScrolling(scroll_x=False)

   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()

class m2ngulaud(wx.Panel):
   "Mängu ajal kasutatav paneel, nupud flickerivad, peab teistesse state'idess bitmappe panema"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.parent = args[0]
      self.dragging = False
      self.snaparea = False
      self.lastsnap = False
      self.splaced = 0
      self.sinked = 0
      self.hits = [[] for x in range(5)]
      self.usedcoord = []
      self.laevad = []
      self.ori = 'v'
      size = wx.DisplaySize()
      tsize = int(size[1]*0.02)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      self.SetBackgroundColour('#222222')
      
      self.Bind(wx.EVT_LEFT_UP, self.lmbup)
      self.Bind(wx.EVT_MOTION, self.motion)
      self.Bind(wx.EVT_MOUSEWHEEL, self.mwheel)
      
      tagasibtn = wx.Button(self, label='Välju', style=wx.BORDER_NONE)
      tagasibtn.Bind(wx.EVT_BUTTON, self.kinni)
      tagasibtn.SetBackgroundColour('#DCAB4F')
      self.sizer = wx.BoxSizer()
      self.vsizer = wx.BoxSizer(wx.VERTICAL)
      paat1 = wx.BoxSizer(wx.VERTICAL)
      paat2 = wx.BoxSizer(wx.VERTICAL)
      paat3 = wx.BoxSizer(wx.VERTICAL)
      paath = wx.BoxSizer()
      lvsize = wx.BoxSizer(wx.VERTICAL)
      lpeal = wx.BoxSizer()
      lall = wx.BoxSizer()
      self.laudSizer = wx.BoxSizer()

      self.paat_bot_h = self.loadbmp('paat_bot_h.png')
      self.paat_mid_h = self.loadbmp('paat_mid_h.png')
      self.paat_top_h = self.loadbmp('paat_top_h.png')
      self.paat_bot_v = self.loadbmp('paat_bot_v.png')
      self.paat_mid_v = self.loadbmp('paat_mid_v.png')
      self.paat_top_v = self.loadbmp('paat_top_v.png')
      self.sulpsti = self.loadbmp('sulpsti.png')
      self.meri = (self.loadbmp('meri1.png'), self.loadbmp('meri2.png'), self.loadbmp('meri3.png'))
      self.hit = (self.loadbmp('meri1_hit.png'), self.loadbmp('meri2_hit.png'), self.loadbmp('meri3_hit.png'))
      self.paat_bot_hit_h = self.loadbmp('paat_bot_hit_h.png')
      self.paat_mid_hit_h = self.loadbmp('paat_mid_hit_h.png')
      self.paat_top_hit_h = self.loadbmp('paat_top_hit_h.png')
      self.paat_bot_hit_v = self.loadbmp('paat_bot_hit_v.png')
      self.paat_mid_hit_v = self.loadbmp('paat_mid_hit_v.png')
      self.paat_top_hit_v = self.loadbmp('paat_top_hit_v.png')

      paat1.Add(self.teeLaev(3))
      paat2.Add(self.teeLaev(2))
      paat3.Add(self.teeLaev(1))
      paat3.Add(self.teeLaev(1))
      paat2.Add(self.teeLaev(0))
      
      paath.AddStretchSpacer()
      paath.Add(paat3)
      paath.Add(paat2)
      paath.Add(paat1)
      paath.AddStretchSpacer()

      emeri = wx.StaticText(self, label='Sinu meri')
      emeri.SetForegroundColour('#5e97bf')
      emeri.SetFont(wx.Font(int(tsize*1.5), wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      vmeri = wx.StaticText(self, label='Radar')
      vmeri.SetForegroundColour('#5e97bf')
      vmeri.SetFont(wx.Font(int(tsize*1.5), wx.DECORATIVE,wx.NORMAL,wx.NORMAL))

      self.tulem = wx.StaticText(self)
      self.tulem.SetForegroundColour('#5e97bf')
      self.tulem.SetFont(wx.Font(int(tsize*2), wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      
      self.vsizer.Add(tagasibtn,1,wx.EXPAND)
      self.vsizer.Add(paath,10,wx.EXPAND)

      self.grid = self.TeeLaud()
      self.laudSizer.Add(self.grid,7, wx.SHAPED)
      self.laudSizer.AddStretchSpacer()
      self.egrid = self.TeeLaud(True)
      self.laudSizer.Add(self.egrid, 7, wx.SHAPED)
      self.sizer.Add(self.vsizer,1,wx.EXPAND)
      lpeal.Add(emeri,1,wx.EXPAND)
      lpeal.AddStretchSpacer(5)
      lpeal.Add(vmeri,1,wx.EXPAND)
      lall.Add(self.tulem,1,wx.EXPAND)
      lvsize.AddStretchSpacer()
      lvsize.Add(lpeal,1,wx.CENTER)
      lvsize.Add(self.laudSizer,1,wx.CENTER)
      lvsize.AddStretchSpacer()
      lvsize.Add(lall,2,wx.CENTER)
      self.sizer.Add(lvsize, 5)
      self.SetSizer(self.sizer)
      self.Layout()

   def teeLaev(self, mids):
      vsizer = wx.BoxSizer(wx.VERTICAL)
      bot = wx.StaticBitmap(self, bitmap=self.paat_bot_v)
      top = wx.StaticBitmap(self, bitmap=self.paat_top_v)
      bot.dragbmp = wx.DragImage(self.paat_bot_v)
      top.dragbmp = wx.DragImage(self.paat_top_v)
      bot.Bind(wx.EVT_LEFT_DOWN, self.lmbdown)
      top.Bind(wx.EVT_LEFT_DOWN, self.lmbdown)
      self.laevad.append({bot:None})
      vsizer.Add(top)
      for x in range(mids):
         mid = wx.StaticBitmap(self, bitmap=self.paat_mid_v)
         mid.dragbmp = wx.DragImage(self.paat_mid_v)
         mid.Bind(wx.EVT_LEFT_DOWN, self.lmbdown)
         self.laevad[-1][mid] = None
         vsizer.Add(mid)
      self.laevad[-1][top] = None
      vsizer.Add(bot)
      return vsizer

   def lmbdown(self, event):
      obj = event.GetEventObject()
      for laev in range(len(self.laevad)):
         if obj in self.laevad[laev]:
            for osa in self.laevad[laev]:
               osa.Hide()
            self.sizer.Add(obj.GetSize())
            pos = self.ScreenToClient(wx.GetMousePosition()) - obj.GetPosition()
            obj.dragbmp.BeginDrag(pos, self)
            obj.dragbmp.Show()
            self.dragging = obj

   def lmbup(self, event):
      if self.dragging:
         self.dragging.dragbmp.EndDrag()
         self.dragging = False
         self.lastsnap = False
         self.ori = 'v'
         self.splaced += 1
         if self.splaced == 5:
            self.splaced = True

   def motion(self, event):
      if self.dragging:
         pos = event.GetPosition()
         children = self.grid.GetChildren()
         if not self.snaparea:
            self.snaparea = []
            size = children[12].GetWindow().GetSize()[0] * 0.2
            for btn in children:
               btn = btn.GetWindow()
               if isinstance(btn, wx._core.StaticBitmap):
                  btnpos = btn.GetPosition()
                  self.snaparea.append((btnpos[0]-size,btnpos[1]-size,btnpos[0]+size*4,btnpos[1]+size*4))
         
         for snap in self.snaparea:
            if pos[0] > snap[0] and pos[0] < snap[2] and pos[1] > snap[1] and pos[1] < snap[3]:
               size = (snap[2]- snap[0])*0.2
               for child in range(len(children)):
                  childobj = children[child].GetWindow()
                  if isinstance(childobj, wx._core.StaticBitmap) and childobj.GetPosition() == (int(snap[0]+size),int(snap[1]+size)):
                     if not self.lastsnap or self.lastsnap[self.dragtile][0] != childobj:
                        for laev in range(5):
                           if self.dragging in self.laevad[laev]:
                              self.dragtile = list(self.laevad[laev].keys()).index(self.dragging)
                              if self.ori == 'v' and child+11*self.dragtile-11*(len(self.laevad[laev])-1) >= 12 and child+11*self.dragtile <= 120:
                                 for i in range(len(self.laevad[laev])):
                                    tile = child+11*i-11*(len(self.laevad[laev])-1)
                                    tiles = (tile+1, tile-1, tile+11, tile+11+1, tile+11-1, tile-11, tile-11+1, tile-11-1)
                                    values = []
                                    for ship in self.laevad:
                                       if self.dragging not in ship:
                                          values += ship.values()
                                    for check in tiles:
                                       if check in values:
                                          return
                                 self.dragging.dragbmp.Hide()
                                 if self.lastsnap:
                                    for i in self.lastsnap:
                                       i[0].SetBitmap(i[1])
                                 self.lastsnap = []
                                 keys = list(self.laevad[laev].keys())
                                 for i in range(len(keys)):
                                    widg = children[child+11*self.dragtile-i*11].GetWindow()
                                    self.lastsnap.append((widg,widg.GetBitmap()))
                                    widg.SetBitmap(keys[i].GetBitmap())
                                    self.laevad[laev][keys[i]] = child+11*self.dragtile-i*11
                                 
                              if self.ori == 'h' and len(children) >= child-self.dragtile+len(self.laevad[laev]):
                                 for none in [x for x in range(11,112,11)] + [x for x in range(11)]: # kas nonetype on laeva tee peal esimese ja viimase vahel
                                    if none in range(child-self.dragtile, child-self.dragtile+len(self.laevad[laev])):
                                       return
                                 for i in range(len(self.laevad[laev])):
                                    tile = child-i+len(self.laevad[laev])-1
                                    tiles = (tile+1, tile-1, tile+11, tile+11+1, tile+11-1, tile-11, tile-11+1, tile-11-1)
                                    values = []
                                    for ship in self.laevad:
                                       if self.dragging not in ship:
                                          values += ship.values()
                                    for check in tiles:
                                       if check in values:
                                          return
                                 self.dragging.dragbmp.Hide()
                                 if self.lastsnap:
                                    for i in self.lastsnap:
                                       i[0].SetBitmap(i[1])
                                 self.lastsnap = []
                                 keys = list(self.laevad[laev].keys())
                                 for i in range(len(keys)):
                                    widg = children[child-self.dragtile+i].GetWindow()
                                    self.lastsnap.append((widg, widg.GetBitmap()))
                                    widg.SetBitmap(keys[i].GetBitmap())
                                    self.laevad[laev][keys[i]] = child-self.dragtile+i
                              return
                     return
            else:
               self.dragging.dragbmp.Move(pos)

   def mwheel(self, event):
      if self.lastsnap:
         if self.ori =='h':
            self.ori = 'v'
         else:
            self.ori = 'h'
         if self.dragging:
            pos = event.GetPosition()
            children = self.grid.GetChildren()
            if not self.snaparea:
               self.snaparea = []
               size = children[12].GetWindow().GetSize()[0] * 0.2
               for btn in children:
                  btn = btn.GetWindow()
                  if isinstance(btn, wx._core.StaticBitmap):
                     btnpos = btn.GetPosition()
                     self.snaparea.append((btnpos[0]-size,btnpos[1]-size,btnpos[0]+size*4,btnpos[1]+size*4))
            for snap in self.snaparea:
               if pos[0] > snap[0] and pos[0] < snap[2] and pos[1] > snap[1] and pos[1] < snap[3]:
                  size = (snap[2]- snap[0])*0.2
                  for child in range(len(children)):
                     childobj = children[child].GetWindow()
                     if isinstance(childobj, wx._core.StaticBitmap) and childobj.GetPosition() == (int(snap[0]+size),int(snap[1]+size)):
                        if self.lastsnap:
                           for laev in range(5):
                              if self.dragging in self.laevad[laev]:
                                 self.dragtile = list(self.laevad[laev].keys()).index(self.dragging)
                                 allowed = False
                                 if self.ori == 'v' and child+11*self.dragtile-11*(len(self.laevad[laev])-1) >= 12 and child+11*self.dragtile <= 120:
                                    for i in range(len(self.laevad[laev])):
                                       tile = child+11*i-11*(len(self.laevad[laev])-1)
                                       tiles = (tile+1, tile-1, tile+11, tile+11+1, tile+11-1, tile-11, tile-11+1, tile-11-1)
                                       values = []
                                       for ship in self.laevad:
                                          if self.dragging not in ship:
                                             values += ship.values()
                                       for check in tiles:
                                          if check in values:
                                             if self.ori == 'h':
                                                self.ori = 'v'
                                             else:
                                                self.ori = 'h'
                                             return
                                    allowed = True
                                    if self.lastsnap:
                                       for i in self.lastsnap:
                                          i[0].SetBitmap(i[1])
                                    self.lastsnap = []
                                    keys = list(self.laevad[laev].keys())
                                    for i in range(len(keys)):
                                       widg = children[child+11*self.dragtile-i*11].GetWindow()
                                       self.lastsnap.append((widg,widg.GetBitmap()))
                                       widg.SetBitmap(keys[i].GetBitmap())
                                       self.laevad[laev][keys[i]] = child+11*self.dragtile-i*11

                                 if self.ori == 'h' and len(children) >= child-self.dragtile+len(self.laevad[laev]):
                                    for none in [x for x in range(11,112,11)] + [x for x in range(11)]: # kas nonetype on laeva tee peal esimese ja viimase vahel
                                       if none in range(child-self.dragtile, child-self.dragtile+len(self.laevad[laev])):
                                          if self.ori == 'h':
                                             self.ori = 'v'
                                          else:
                                             self.ori = 'h'
                                          return
                                    for i in range(len(self.laevad[laev])):
                                       tile = child-i+len(self.laevad[laev])-1
                                       tiles = (tile+1, tile-1, tile+11, tile+11+1, tile+11-1, tile-11, tile-11+1, tile-11-1)
                                       values = []
                                       for ship in self.laevad:
                                          if self.dragging not in ship:
                                             values += ship.values()
                                       for check in tiles:
                                          if check in values:
                                             if self.ori == 'h':
                                                self.ori = 'v'
                                             else:
                                                self.ori = 'h'
                                             return
                                    allowed = True
                                    if self.lastsnap:
                                       for i in self.lastsnap:
                                          i[0].SetBitmap(i[1])
                                    self.lastsnap = []
                                    keys = list(self.laevad[laev].keys())
                                    for i in range(len(keys)):
                                       widg = children[child-self.dragtile+i].GetWindow()
                                       self.lastsnap.append((widg, widg.GetBitmap()))
                                       widg.SetBitmap(keys[i].GetBitmap())
                                       self.laevad[laev][keys[i]] = child-self.dragtile+i
                                 if allowed:
                                    break
                                 else:
                                    if self.ori == 'h':
                                       self.ori = 'v'
                                    else:
                                       self.ori = 'h'
                                    return
                        break

         if self.ori == 'v':
            for laev in range(5):
               if self.dragging in self.laevad[laev]:
                  osad = list(self.laevad[laev].keys())
                  self.lastsnap[0][0].SetBitmap(self.paat_bot_v)
                  osad[0].SetBitmap(self.paat_bot_v)
                  self.lastsnap[-1][0].SetBitmap(self.paat_top_v)
                  osad[-1].SetBitmap(self.paat_top_v)
                  if len(self.lastsnap) > 2:
                     for osa in range(1, len(osad)-1):
                        self.lastsnap[osa][0].SetBitmap(self.paat_mid_v)
                        osad[osa].SetBitmap(self.paat_mid_v)
                  break
         else:
            for laev in range(5):
               if self.dragging in self.laevad[laev]:
                  osad = list(self.laevad[laev].keys())
                  self.lastsnap[0][0].SetBitmap(self.paat_bot_h)
                  osad[0].SetBitmap(self.paat_bot_h)
                  self.lastsnap[-1][0].SetBitmap(self.paat_top_h)
                  osad[-1].SetBitmap(self.paat_top_h)
                  if len(self.lastsnap) > 2:
                     for osa in range(1, len(osad)-1):
                        self.lastsnap[osa][0].SetBitmap(self.paat_mid_h)
                        osad[osa].SetBitmap(self.paat_mid_h)
                  break

   def kinni(self, event):
      self.Hide()
      self.parent.menu.Show()
      self.parent.Layout()
      for child in self.grid.GetChildren():
         child = child.GetWindow()
         if isinstance(child, wx._core.StaticBitmap):
            child.SetBitmap(self.meri[randint(0,2)])
      for laev in self.laevad:
         for osa in laev:
            osa.Show()
            laev[osa] = None
         laev = list(laev.keys())
         laev[0].SetBitmap(self.paat_bot_v)
         laev[-1].SetBitmap(self.paat_top_v)
         if len(laev) > 2:
            for osa in laev[1:-1]:
               osa.SetBitmap(self.paat_mid_v)
      for child in self.egrid.GetChildren():
         child = child.GetWindow()
         if isinstance(child, wx._core.StaticBitmap):
            child.SetBitmap(self.meri[randint(0,2)])
      self.dragging = False
      self.snaparea = False
      self.lastsnap = False
      self.splaced = 0
      self.sinked = 0
      self.hits = [[] for x in range(5)]
      self.usedcoord = []

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
         text.SetForegroundColour('#5e97bf')
         sizer.AddStretchSpacer()
         sizer.Add(text, 0, wx.ALIGN_CENTER)
         sizer.AddStretchSpacer()
         grid.Add(sizer, 0, wx.EXPAND)
      if AI:
         pool = 'C'
      else: 
         pool = ''
      text = 0
      for i in range(110):
         if i in [x for x in range(0, 100, 11)]:
            sizer = wx.BoxSizer()
            txt = wx.StaticText(self, label=list(ascii_uppercase)[i//11])
            txt.SetForegroundColour('#5e97bf')
            sizer.AddStretchSpacer()
            sizer.Add(txt, 0, wx.ALIGN_CENTER)
            sizer.AddStretchSpacer()
            cells.append((sizer, 0, wx.EXPAND))
            text += 1
         else:
            name = str(i-text) + pool
            if AI:
               btn = wx.StaticBitmap(self, size=size, bitmap=self.meri[randint(0,2)], name=name)
               btn.Bind(wx.EVT_LEFT_DOWN, self.coord)
            else:
               btn = wx.StaticBitmap(self, size=size, bitmap=self.meri[randint(0,2)], name=name)
               btn.Bind(wx.EVT_LEFT_DOWN, self.lmbdown)
            btn.name = name 
            cells.append((btn, 0, wx.EXPAND))
      grid.AddMany(cells)
      for cell in grid.GetChildren():
         cell = cell.GetWindow()
         if isinstance(cell, wx._core.StaticText):
            cell.SetForegroundColour('#5e97bf')
      return grid
   
   def coord(self, event):
      "Edastab ruudustikule tehtud kliki koordinaadid: [column, row]"
      btn =  event.GetEventObject()
      name = btn.name
      if type(self.splaced) != int and len(name) == 2:
         if (0, int(name[0])) not in self.usedcoord:
            self.usedcoord.append((0, int(name[0])))
            # lask = playerLasi(0, int(name[0]))
            print([0, int(name[0])])
         else:
            return
      elif type(self.splaced) != int and (int(name[0]), int(name[1])) not in self.usedcoord:
         self.usedcoord.append((int(name[0]), int(name[1])))
         # lask = playerLasi(int(name[0]), int(name[1]))
         print([int(name[0]), int(name[1])])
      else:
         return
      lask = 1
      if lask == 0:
         btn.SetBitmap(self.sulpsti)
      elif lask in range(1,6):
         children = self.egrid.GetChildren()
         for child in range(len(children)):
            tile = children[child].GetWindow()
            if tile == btn:
               leidis = False
               for laev in self.hits:
                  if len(children) > child+1 and children[child+1].GetWindow() in laev:
                     laev.append(btn)
                     if lask == 1:
                        btn.SetBitmap(self.hit[randint(0,2)])
                     leidis = True
                  elif children[child-1].GetWindow() in laev:
                     laev.append(btn)
                     if lask == 1:
                        btn.SetBitmap(self.hit[randint(0,2)])
                     leidis = True
                  elif len(children) > child+11 and children[child+11].GetWindow() in laev:
                     laev.append(btn)
                     if lask == 1:
                        btn.SetBitmap(self.hit[randint(0,2)])
                     leidis = True
                  elif children[child-11].GetWindow() in laev:
                     laev.append(btn)
                     if lask == 1:
                        btn.SetBitmap(self.hit[randint(0,2)])
                     leidis = True
                  if leidis and lask in range(2, 6):
                     jrj = []
                     for osa in laev:
                        for child in range(len(children)):
                           if osa == children[child].GetWindow():
                              jrj.append(child)
                     jrj.sort()
                     print(jrj)
                     if jrj[0]+1 == jrj[1] and len(jrj) == lask:
                        self.hits.remove(laev)
                        children[jrj[0]].GetWindow().SetBitmap(self.paat_bot_hit_h)
                        children[jrj[-1]].GetWindow().SetBitmap(self.paat_top_hit_h)
                        if len(jrj) > 2:
                           for osa in range(jrj[1],jrj[-1]):
                              children[osa].GetWindow().SetBitmap(self.paat_mid_hit_h)
                        break
                     elif len(jrj) == lask:
                        self.hits.remove(laev)
                        children[jrj[0]].GetWindow().SetBitmap(self.paat_top_hit_v)
                        children[jrj[-1]].GetWindow().SetBitmap(self.paat_bot_hit_v)
                        if len(jrj) > 2:
                           for osa in range(jrj[1],jrj[-1], 11):
                              children[osa].GetWindow().SetBitmap(self.paat_mid_hit_v)
                        break
                     else:
                        # leidis = False
                        break
               if len(self.hits) == 0:
                  self.tulem.SetLabel('Võitsid!')
                  return
               if not leidis:
                  for laev in self.hits:
                     
                     if len(laev) == 0:
                        laev.append(btn)
                        btn.SetBitmap(self.hit[randint(0,2)])
                        break
               break

      elif lask == 6:
         self.tulem.SetLabel('Võitsid!')
      # ailask = aiLask()
      ailask = (2,0)
      lask = 12 + 11 * ailask[0] + ailask[1]
      for laev in self.laevad:
         leidis = False
         for osa in laev:
            if lask == laev[osa]:
               # laev[osa] == str(lask)
               osad = list(laev.values())
               osad.sort()
               leidis = True
               print('leidis laeva',osad[0]+1,osad[1])
               if osad[0]+1 == osad[1]:
                  if lask == osad[0]:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_bot_hit_h)
                  elif lask == osad[-1]:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_top_hit_h)
                  else:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_mid_hit_h)
               else:
                  if lask == osad[0]:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_top_hit_v)
                  elif lask == osad[-1]:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_bot_hit_v)
                  else:
                     self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.paat_mid_hit_v)
               self.sinked += 1
               if self.sinked == 17:
                  self.tulem.SetLabel('Kaotasid')
               break
         if not leidis:
            self.grid.GetChildren()[lask].GetWindow().SetBitmap(self.sulpsti)
         break

   def loadbmp(self,file, bmp=True, scale=True): 
      size = int(wx.DisplaySize()[1] * 0.5 / 10)
      size = (size, size)
      if bmp and scale:
         return wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),'images',file)).Rescale(size[0],size[0]))
      elif bmp:
         return wx.Bitmap(wx.Image(join(dirname(realpath(__file__)),'images',file)))
      img = wx.Image(join(dirname(realpath(__file__)),file))
      if scale:
         img.Rescale(size[0],size[0])
      return img

class MainMenu(wx.Panel):
   "Põhimenuu paneel"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.SetBackgroundColour('#222222')
      self.parent = args[0]
      size = wx.DisplaySize()
      tsize = int(size[1]*0.023)
      self.SetFont(wx.Font(tsize, wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      vsizer = wx.BoxSizer(wx.VERTICAL)
      sizer = wx.BoxSizer()
      menusizer = wx.BoxSizer(wx.VERTICAL)

      head = wx.StaticText(self, label='Laevade pommitamine',style=wx.ALIGN_CENTRE)
      head.SetFont(wx.Font(int(tsize*3.5), wx.DECORATIVE,wx.NORMAL,wx.NORMAL))
      head.SetForegroundColour('#5e97bf')
      
      self.nimi = False
      nimi = wx.TextCtrl(self)
      nimi.SetMaxLength(20)
      nimi.SetLabel('Nimi')
      nimi.Bind(wx.EVT_TEXT, self.name)

      self.tase = False
      tase = wx.ComboBox(self, value='Raskustase', choices=['Kerge','Keskmine','Raske'])
      tase.SetEditable(False)
      tase.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.raskus)

      storybtn = wx.Button(self, label='3. Maailmasõda', style=wx.BORDER_NONE)
      storybtn.Bind(wx.EVT_BUTTON, self.story)
      storybtn.SetBackgroundColour('#DCAB4F')
      
      m2ngibtn = wx.Button(self, label='Kiirmäng', style=wx.BORDER_NONE)
      m2ngibtn.Bind(wx.EVT_BUTTON, self.m2ngi)
      m2ngibtn.SetBackgroundColour('#DCAB4F')

      poebtn = wx.Button(self, label='Pood', style=wx.BORDER_NONE)
      poebtn.Bind(wx.EVT_BUTTON, self.pood)
      poebtn.SetBackgroundColour('#DCAB4F')

      info = wx.Button(self, label='Infonurk', style=wx.BORDER_NONE)
      info.Bind(wx.EVT_BUTTON, self.info)
      info.SetBackgroundColour('#DCAB4F')

      kinnibtn = wx.Button(self, label='Kinni', style=wx.BORDER_NONE)
      kinnibtn.Bind(wx.EVT_BUTTON, lambda a: self.parent.Close())
      kinnibtn.SetBackgroundColour('#DCAB4F')
      
      menusizer.Add(nimi,10,wx.EXPAND)     # fontsize upscalib kõike, peaks eraldi fondid panema
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(tase,10,wx.EXPAND)
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(storybtn,17,wx.EXPAND)
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(m2ngibtn,17,wx.EXPAND)
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(poebtn, 17, wx.EXPAND)
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(info,17,wx.EXPAND)
      menusizer.AddStretchSpacer(prop=1)
      menusizer.Add(kinnibtn,17,wx.EXPAND)

      sizer.AddStretchSpacer(prop=3)
      sizer.Add(menusizer, 2, wx.EXPAND)
      sizer.AddStretchSpacer(prop=3)
      
      vsizer.AddStretchSpacer()
      vsizer.Add(head,1,wx.EXPAND)
      vsizer.AddStretchSpacer()
      vsizer.Add(sizer,1,wx.EXPAND)
      vsizer.AddStretchSpacer(3)
      self.SetSizer(vsizer)

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
      if self.tase and self.nimi or True:
         self.Hide()
         self.parent.laud.Show()
         self.parent.Layout()
   
   def story(self, event):
      print(self.tase, self.nimi)
      if self.tase and self.nimi or True:
         self.Hide()
         self.parent.story.Show()
         self.parent.Layout()

   def pood(self, event):
      self.Hide()
      self.parent.cashshop.Show()
      self.parent.Layout()
   
   def info(self, event):
      self.Hide()
      self.parent.infopan.Show()
      self.parent.Layout()

class MainFrame(wx.Frame):
   "Akna raam, mille sees on paneelid"
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.SetBackgroundColour('#222222')
      
      self.InitUI()
      self.Centre()
      self.Show()
      self.resizing = False

      self.Bind(wx.EVT_SIZE, self.OnSize)
      self.Bind(wx.EVT_IDLE, self.OnIdle)

   def InitUI(self):
      self.paneelisizer = wx.BoxSizer()
      self.menu = MainMenu(self)
      self.story = storypan(self)
      self.story.Hide()
      self.laud = m2ngulaud(self)
      self.laud.Hide()
      self.cashshop = shop(self)
      self.cashshop.Hide()
      self.infopan = infop(self, style=wx.VSCROLL)
      self.infopan.Hide()
      self.paneelisizer.AddMany([(self.menu,1,wx.EXPAND),(self.story,1,wx.EXPAND),(self.laud,1,wx.EXPAND),(self.cashshop,1,wx.EXPAND),(self.infopan,1,wx.EXPAND)])
      self.SetSizer(self.paneelisizer)

   def OnSize(self, event):
      if self.infopan.IsShown():
         # print('jooksis')
         size = self.GetSize()
         vsize = self.GetVirtualSize()
         self.SetVirtualSize((size[0],vsize[1]))
      else:
         self.resizing = True
         self.laud.snaparea = False

   def OnIdle(self, event):
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

if __name__ == '__main__':
   gui = app()