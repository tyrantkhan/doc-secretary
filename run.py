import sys

import wx

import about


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=wx.GetApp().GetTopWindow(), title="DocSecretary")
        panel = MainPanel(self)
        self.SetSize(600, 400)

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "&Exit")

        view_menu = wx.Menu()
        view_menu.Append(wx.ID_ANY, "&Patients")
        view_menu.Append(wx.ID_ANY, "&Appointments")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "&About")
        help_menu.Append(wx.ID_ANY, "&License")
        help_menu.Append(wx.ID_ANY, "&Help")

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(view_menu, "&View")
        menu_bar.Append(help_menu, "&Help")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, id=wx.ID_EXIT, handler=lambda event: sys.exit(0))
        self.Bind(wx.EVT_MENU, id=wx.ID_ABOUT, handler=lambda event: about.about_dialog(self))

        self.Show()


class MainPanel(wx.Panel):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent=parent)
        self.parent = parent

        view_button = wx.Button(parent=self, label="View patients")
        appts_button = wx.Button(parent=self, label="Appointments")

        top_sizer = wx.BoxSizer(wx.VERTICAL)  # Root sizer
        button_sizer = wx.BoxSizer(wx.VERTICAL)

        button_sizer.Add(view_button, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)
        button_sizer.Add(appts_button, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        top_sizer.Add(button_sizer, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)
        top_sizer.SetSizeHints(self.parent)
        self.SetSizerAndFit(top_sizer)

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
