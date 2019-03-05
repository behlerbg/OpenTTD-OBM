#! python3
## OBM_generator_GUI.py
## tkinter based GUI for creating an OBM file for OpenTTD
## Brett Behler 03.05.2019

import tkinter as tk
from tkinter import ttk
import openttd_obm_generator as obm
import os

## Event Commands

def add_track(track, style):
    pass
    #add track to style list

def remove_track(track, style):
    pass
    #remove track from style list

def get_directory():
    pass
    #tk.filedialog

def switch_style(style):
    pass
    #switch between old, new, ezy styles and update style list

def popupmessage(message):
    pass
    #display popup window with relevant error information

def new_obm():
    pass
    #if OBMApp.obm_data, popup overwrite warning
    #else, OMBApp.set_obm = obm.OBMData()

def open_obm():
    pass
    #tkinter filedialog
    #read data
    #OBMApp.set_obm(name, shortname, version, description)
    #OBMAApp.obm_data.write_lists(theme, old, new, ez)

def save_obm():
    pass
    #validate_data()
    #tkinter filedialog
    #if True, save obm file in directory
    #else, popupmessage

def validate_data(OBMData):
    pass
    #if valid, True
    #else, False

def quit_program():
    if not app.has_saved:
        pass
        #popupmessage changes lost warning
    else:
        raise SystemExit

## Main App


class OBMApp(tk.Tk):
    '''Main tkinter app.

    Methods:
        __init__(self):
        create_widgets(self):
        set_obm(self, OBMData):
        get_track_list():

    '''
    def __init__(self):
        """Doc string text
        
        Arguments:
            
        
        Keyword Arguments:
            
        
        Returns:
            
        
        Raises:
            
        """
        tk.Tk.__init__(self)
        tk.Tk.wm_iconbitmap(self)
        tk.Tk.wm_title(self, 'OBM File Generator')
        self.track_list = []
        self.music_dir = ''
        self.openttd_dir = ''
        self.obm_data = None
        self.has_saved = False

        self.container = tk.Frame(self)
        self.container.pack(side='top', fill='both', expand=True)

        self.create_widgets()

    def create_widgets(self):
        """Creates and configures all of the GUI widgets."""

        # Menubar Configuration
        menubar = tk.Menu(self.container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=new_obm)
        filemenu.add_command(label='Open...', command=open_obm)
        filemenu.add_command(label='Save', command=save_obm)
        filemenu.add_command(label='Save As...', command=save_obm)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit_program)
        menubar.add_cascade(label='File', menu=filemenu)

        menubar.add_command(label='Help', command=lambda: popupmessage('test'))

        tk.Tk.config(self, menu=menubar)

        # Button Configuration

        # Textbox Configuration

    def set_obm(self, *args, **kwargs):
        self.obm_data = obm.OBMData(*args, **kwargs)

    #def get_track_list(self, directory):
        #for f in directory, add if .mid, .midi, or .gm
    

if __name__ == '__main__':
    app = OBMApp()
    app.geometry('800x600')
    app.mainloop()