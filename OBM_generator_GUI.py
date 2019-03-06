#! python3
## OBM_generator_GUI.py
## tkinter based GUI for creating an OBM file for OpenTTD
## Brett Behler 03.05.2019

import tkinter as tk
from tkinter import ttk
import openttd_obm_generator as obm
import os

## Global Variables

LARGE_FONT = ('fixedsys', 12)
MEDIUM_FONT = ('fixedsys', 10)
SMALL_FONT = ('fixedsys', 8)

## Event Commands

def add_track(track, style):
    pass
    #add track to style list

def remove_track(track, style):
    pass
    #remove track from style list

def clear_style(style):
    pass

def get_directory():
    pass
    #tk.filedialog
    #return directory
        
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
        import_tracks():

    '''
    def __init__(self):
        """Doc string text
        
        Arguments:
            
        
        Keyword Arguments:
            
        
        Returns:
            
        
        Raises:
            
        """
        tk.Tk.__init__(self)
        tk.Tk.configure(self, bg='#838582')
        tk.Tk.wm_iconbitmap(self)
        tk.Tk.wm_title(self, 'OBM File Generator')
        self.track_list = []
        self.style_list = []
        self.music_dir = ''
        self.openttd_dir = ''
        self.obm_data = None
        self.has_saved = False
        self.cur_style = None
        self.cur_track = None

        self.container = tk.Frame(self, bg='#838582')
        # self.container.grid(row=0, column=0, sticky='NSEW')

        self.create_widgets()

    def create_widgets(self):
        """Creates and configures all of the GUI widgets."""

        global LARGE_FONT
        global MEDIUM_FONT
        global SMALL_FONT

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

        # Metadata Configuration

        tk.Label(self, text='OBM Metadata', font=LARGE_FONT).grid(row=0, column=0, columnspan=5, sticky='NW', padx=5, pady=10)

        tk.Label(self, text='Name:', font=MEDIUM_FONT).grid(row=1, column=0, sticky='NW', padx=5, pady=1)
        self.meta_name = tk.Entry(self)
        self.meta_name.grid(row=1, column=1, columnspan=4, sticky='NEW')
        self.meta_name.insert(0, 'Music Pack Name')

        tk.Label(self, text='Shortname:', font=MEDIUM_FONT).grid(row=2, column=0, sticky='NW', padx=5, pady=1)
        self.meta_shortname = tk.Entry(self)
        self.meta_shortname.grid(row=2, column=1, columnspan=4, sticky='NEW')
        self.meta_shortname.insert(0, 'XXXX')

        tk.Label(self, text='Version:', font=MEDIUM_FONT).grid(row=3, column=0, sticky='NW', padx=5, pady=1)
        self.meta_version = tk.Entry(self)
        self.meta_version.grid(row=3, column=1, columnspan=4, sticky='NEW')
        self.meta_version.insert(0, '0.0.1')

        tk.Label(self, text='Description:', font=MEDIUM_FONT).grid(row=4, column=0, sticky='NW', padx=5, pady=1)
        self.meta_description = tk.Entry(self)
        self.meta_description.grid(row=4, column=1, columnspan=4, sticky='NEW')
        self.meta_description.insert(0, 'A short description for the music pack')

        tk.Label(self, text='Origin:', font=MEDIUM_FONT).grid(row=5, column=0, sticky='NW', padx=5, pady=1)
        self.meta_origin = tk.Entry(self)
        self.meta_origin.grid(row=5, column=1, columnspan=4, sticky='NEW')
        self.meta_origin.insert(0, 'https://')


        # Midifile Configuration
        tk.Label(self, text='Track Information: ', font=LARGE_FONT).grid(row=6, column=0, sticky='NW', padx=5, pady=10)
        self.track_label = tk.Label(self, font=LARGE_FONT)
        self.track_label.grid(row=6, column=1, columnspan=3, sticky='NEW', pady=10)

        tk.Label(self, text='Name:', font=MEDIUM_FONT).grid(row=7, column=0, padx=5, pady=1, sticky='NW')
        self.track_name = tk.Entry(self)
        self.track_name.grid(row=7, column=1, columnspan=4, sticky='NEW')
        self.track_name.insert(0, 'Name of current track')

        # Style Configuration
        tk.Label(self, text='Track Index', font=LARGE_FONT).grid(row=8, column=0, sticky='NW', padx=5, pady=10)
        import_btn = ttk.Button(self, text='Import...', command=self.import_tracks)
        import_btn.grid(row=8, column=1, sticky='NW', pady=10, padx=5)

        tk.Label(self, text='Program', font=LARGE_FONT).grid(row=8, column=3, sticky='NW', padx=5, pady=10)
        self.style_label = tk.Label(self, font=LARGE_FONT)
        self.style_label.grid(row=8, column=4, sticky='NE', padx=5, pady=10)

        self.track_listbox = tk.Listbox(self, bg='#101010', fg='#a0c2de', width=40)
        self.track_listbox.grid(row=9, column=0, columnspan=2, rowspan=7, sticky='NSEW', padx=5)

        self.style_listbox = tk.Listbox(self, bg='#101010', fg='#a0c2de', width=40)
        self.style_listbox.grid(row=9, column=3, columnspan=2, rowspan=7, sticky='NSEW', padx=5)

        self.old_btn = tk.Button(self, text='Old Style', command=lambda: switch_style('old'))
        self.old_btn.grid(row=9, column=2, sticky='NSEW', padx=10, pady=10)

        self.new_btn = tk.Button(self, text='New Style', command=lambda: switch_style('new'))
        self.new_btn.grid(row=10, column=2, sticky='NSEW', padx=10, pady=10)

        self.ezy_btn = tk.Button(self, text='Ezy Street', command=lambda: switch_style('ezy'))
        self.ezy_btn.grid(row=11, column=2, sticky='NSEW', padx=10, pady=10)

        tk.Label(self, text='').grid(row=12, column=2, sticky='NSEW')

        self.add_btn = tk.Button(self, text='ADD >>', command=add_track, font=SMALL_FONT, bg='#838582', fg='#101010')
        self.add_btn.grid(row=13, column=2, sticky='NSEW', padx=10, pady=10)

        self.ezy_btn = tk.Button(self, text='<< REMOVE', command=remove_track, font=SMALL_FONT, bg='#838582', fg='#101010')
        self.ezy_btn.grid(row=14, column=2, sticky='NSEW', padx=10, pady=10)

        self.ezy_btn = tk.Button(self, text='Clear', command=clear_style, font=SMALL_FONT, bg='#838582', fg='#101010')
        self.ezy_btn.grid(row=15, column=2, sticky='NSEW', padx=10, pady=10)

        

    def set_obm(self, *args, **kwargs):
        self.obm_data = obm.OBMData(*args, **kwargs)

    def import_tracks(self):
        directory = get_directory()
        for f in os.listdir(directory):
            if os.path.isfile(f) and (
                f[-3:] == '.gm' or
                f[-4:] == '.mid' or
                f[-5:] == '.midi'
            ):
                self.track_list.append(f)

    def update(self):
        self.track_listbox.delete(0, END)
        for track in self.track_list:
            self.track_listbox.insert(END, track)
        self.style_listbox.delete(0, END)
        for track in self.style_list:
            self.style_listbox.insert(END, track)

    

if __name__ == '__main__':
    app = OBMApp()
    app.geometry('600x650')
    app.mainloop()
