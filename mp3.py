import wx
import os



class MainWindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Text Editor++',size=(700,560),style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
        wx.Frame.CenterOnScreen(self)
        
       
        

     
        
         

        

        ##MENU AND STATUS BAR
        self.status = self.CreateStatusBar()
        self.status.SetStatusText('Ready')
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        view_menu = wx.Menu()
        help_menu = wx.Menu()

        #MENU ID'S
        ID_FILE_LOAD = 2
        ID_FILE_EXIT = 3

        ID_VIEW_SHOW_STATUSBAR = 4
        ID_HELP_ABOUT = 5

        ##FILE MENU
        file_menu.Append(ID_FILE_LOAD, "&Load...\tCtrl+L", "This will let you choose a song to load")
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_EXIT,"Exit","This will exit the program")

        ##VIEW MENU
        self.check_statusbar = view_menu.Append(ID_VIEW_SHOW_STATUSBAR,'Show Stat&usbar\tCtrl+U', "This will disable the statusbar", kind=wx.ITEM_CHECK)
        view_menu.Check(self.check_statusbar.GetId(),True)

        
        help_menu.Append(ID_HELP_ABOUT,"&About","About Text editor++")

        ##MENUBAR APPEND
        menubar.Append(file_menu,"File")
        menubar.Append(view_menu,"View")
        menubar.Append(help_menu,"Help")
        self.SetMenuBar(menubar)

        ##MENU ACTION BINDING
        self.Bind(wx.EVT_MENU, self.Load, None, 2)        
        self.Bind(wx.EVT_MENU, self.Close, None, 3)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.check_statusbar)
        self.Bind(wx.EVT_MENU, self.About, None, 5)

        ##FONTS
        font1 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        font2 = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        try:
            self.mc = wx.media.MediaCtrl(self)
        except NotImplementedError:
            raise

       
    
        
    def Close(self, event):
        box=wx.MessageDialog(None, 'Are you sure you want to exit?', 'Exit program?', wx.YES_NO)
        answer=box.ShowModal()
        if answer==wx.ID_YES:
            self.Destroy()

    def About(self, event):
        self.new = wx.Frame(parent=self, id=-1)
        self.new.Show()
        

    def selLoadFile(self, event):
            my_selection = self.myListBox.GetStringSelection()
            folder, filename = os.path.split(self.path)
            file_path = os.path.join(folder,my_selection)
            
            self.doLoadFile2(file_path)
            #self.doLoadFile2(my_selection)
           

    def Load(self, event):
        dlg = wx.FileDialog(self, "Choose a file", " ", "", "*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.path = path
            self.doLoadFile(self.path)
            dlg.Destroy() 

    def load2(self):
            my_selection = self.myListBox.GetStringSelection()
             
            folder, filename = os.path.split(self.path)
            file_path = os.path.join(folder,my_selection)
            self.doLoadFile2(file_path)
                         
             

    def doLoadFile(self, path):
        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)

        else:
            folder, filename = os.path.split(path)
            self.myListBox.Append(filename)
             
            self.mc.SetInitialSize()
             
    def doLoadFile2(self, file_path):
        if not self.mc.Load(file_path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % file_path, "ERROR", wx.ICON_ERROR | wx.OK)

        else:
            folder, filename = os.path.split(file_path)
             
            
            self.status.SetStatusText("Now start " +'%s' % file_path)
            self.mc.SetInitialSize()
             

   
    

    def ToggleStatusBar(self, e):
        if self.check_statusbar.IsChecked():
            self.status.Show()
            self.status.SetStatusText('Ready')
        else:
            self.status.Hide()

        ##RUN##

if __name__=='__main__':
        app=wx.App()
        frame=MainWindow(parent=None,id=-1)
        frame.Show()
        app.MainLoop()
