import wx
import wx.adv


def about_dialog(parent):
    """An about dialog
    Args:
        parent (wx.Window): The parent window
    """
    license_text = """
    Copyright (C) DocSecretary Authors 2018
    DocSecretary is licensed under Creative Commons Attribution-NonCommercial 3.0 license.
    
    You may not use this code or application except in compliance with the License.
    You may obtain a copy of the License at:
    https://creativecommons.org/licenses/by-nc/3.0/
    
    You are free to use DocSecretary for your personal or non-profit uses.
    If you are a for profit entity (like a doctor's office), You can get the author's
    permission to use DocSecretary for commercial websites by paying a fee."""

    about_info = wx.adv.AboutDialogInfo()
    about_info.SetName("DocSecretary")
    about_info.SetVersion("v1.0")
    about_info.SetCopyright("Copyright (C) DocSecretary Authors 2018")
    about_info.SetDescription("An Application to Manage Patients and their Appointments.")
    about_info.SetWebSite("https://github.com/tyrantkhan/doc-secretary", "GitHub repository")
    about_info.SetLicense(license_text)
    wx.adv.AboutBox(about_info, parent)
