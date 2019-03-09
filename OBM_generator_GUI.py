#! python3
# OBM_generator_GUI.py
# tkinter based GUI for creating an OBM file for OpenTTD
# Brett Behler 03.05.2019

import tkinter as tk
from tkinter import filedialog
import openttd_obm_generator as obm
import os

# Global Variables

LARGE_FONT = ('fixedsys', 14)
MEDIUM_FONT = ('fixedsys', 10)
SMALL_FONT = ('fixedsys', 6)
GREY = '#838582'
DRK_GREY = '#50524f'
LIGHT_GRAY = '#a8a8a8'
BLACK = '#101010'
BLUE = '#a0c2de'
RED = '#e60005'
YELLOW = '#e4b908'
LIGHT_YELLOW = '#faf36f'

# Event Commands


def popupinfo(message):
    popup = tk.Tk()
    popup.configure(bg=RED)
    popup.wm_title('Information')
    label = tk.Label(popup, text=message, font=MEDIUM_FONT)
    label.configure(bg=RED, fg=LIGHT_YELLOW)
    label.pack(side='top', fill='x', pady=20, padx=30)
    B1 = tk.Button(popup, text='OK', command=popup.destroy)
    B1.configure(bg=YELLOW, fg=BLACK, font=SMALL_FONT, width=10)
    B1.pack(side='right', padx=10, pady=10)


def new_obm():
    popupinfo('Not yet implemented.')


def open_obm():
    popupinfo('Not yet implemented.')


def validate_data(OBMData):
    pass
    # if valid, True
    # else, False


def quit_program():
    if not app.has_saved:
        pass
        # popupmessage changes lost warning
    else:
        raise SystemExit

# Main App


class OBMApp(tk.Tk):
    """Does these things.
    
    Instance Variables:
        
    
    Methods:
        
    
    """
    def __init__(self):
        """Doc string text

        Arguments:


        Keyword Arguments:


        Returns:


        Raises:

        """
        global GREY

        tk.Tk.__init__(self)
        tk.Tk.configure(self, bg=GREY)
        tk.Tk.minsize(self, width=819, height=650)
        tk.Tk.maxsize(self, width=819, height=650)
        tk.Tk.wm_iconbitmap(self)
        tk.Tk.wm_title(self, 'OBM File Generator')
        self.track_list = []
        self.style_list = []
        self.music_dir = ''
        self.openttd_dir = ''
        self.set_obm()
        self.has_saved = False
        self.cur_style = None
        self.confirm = None

        self.container = tk.Frame(self, bg=GREY)

        self.create_widgets()

    def create_widgets(self):
        """Create and configure all GUI widgets."""

        global LARGE_FONT
        global MEDIUM_FONT
        global SMALL_FONT
        global GREY
        global BLACK
        global BLUE

        # Menubar Configuration
        menubar = tk.Menu(self.container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New', command=new_obm)
        filemenu.add_command(label='Open...', command=open_obm)
        filemenu.add_command(label='Save',
                command=lambda: self.save_obm(self.openttd_dir))
        filemenu.add_command(label='Save As...', command=self.save_obm)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=quit_program)
        menubar.add_cascade(label='File', menu=filemenu)

        menubar.add_command(label='Help', command=lambda: popupinfo('test'))

        tk.Tk.config(self, menu=menubar)

        # Metadata Configuration

        tk.Label(self, text='OBM Metadata', font=LARGE_FONT, bg=GREY).grid(
            row=0, column=0, columnspan=5, sticky='NW', padx=5, pady=10)

        self.meta_name_val = tk.StringVar()
        tk.Label(self, text='Name:', font=MEDIUM_FONT, bg=GREY).grid(row=1,
                column=0, sticky='NW', padx=5, pady=1)
        self.meta_name = tk.Entry(self, textvariable=self.meta_name_val)
        self.meta_name.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.meta_name.grid(row=1, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.meta_name.insert(0, 'Music Pack Name')

        self.shortname_val = tk.StringVar()
        self.shortname_val.trace('w', self.limit_shortname)
        tk.Label(self, text='Shortname:', font=MEDIUM_FONT, bg=GREY).grid(
            row=2, column=0, sticky='NW', padx=5, pady=1)
        self.meta_shortname = tk.Entry(self, textvariable=self.shortname_val)
        self.meta_shortname.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.meta_shortname.grid(row=2, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.meta_shortname.insert(0, 'XXXX')

        self.version_val = tk.StringVar()
        tk.Label(self, text='Version:', font=MEDIUM_FONT, bg=GREY).grid(row=3,
                column=0, sticky='NW', padx=5, pady=1)
        self.meta_version = tk.Entry(self, textvariable=self.version_val)
        self.meta_version.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.meta_version.grid(row=3, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.meta_version.insert(0, '0.0.1')

        self.description_val = tk.StringVar()
        tk.Label(self, text='Description:', font=MEDIUM_FONT, bg=GREY).grid(
                row=4, column=0, sticky='NW', padx=5, pady=1)
        self.meta_description = tk.Entry(self,
                textvariable=self.description_val)
        self.meta_description.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.meta_description.grid(row=4, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.meta_description.insert(0, ('A short description'
                                        + 'for the music pack'))

        self.origin_val = tk.StringVar()
        tk.Label(self, text='Origin:', font=MEDIUM_FONT, bg=GREY).grid(row=5,
                column=0, sticky='NW', padx=5, pady=1)
        self.meta_origin = tk.Entry(self, textvariable=self.origin_val)
        self.meta_origin.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.meta_origin.grid(row=5, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.meta_origin.insert(0, 'https://')

        # Midifile Configuration
        tk.Label(self, text='Track Information: ', font=LARGE_FONT,
                bg=GREY).grid(row=6, column=0, sticky='NW', padx=5, pady=10)
        self.track_label = tk.Label(self, font=LARGE_FONT, bg=GREY)
        self.track_label.grid(row=6, column=1, columnspan=3, sticky='NW',
                pady=10, padx=5)

        self.track_name_val = tk.StringVar()
        tk.Label(self, text='Name:', font=MEDIUM_FONT, bg=GREY).grid(row=7,
                column=0, padx=5, pady=1, sticky='NW')
        self.track_name = tk.Entry(self, textvariable=self.track_name_val)
        self.track_name.config(bg=BLACK, fg=BLUE, font=MEDIUM_FONT,
                insertbackground='white')
        self.track_name.grid(row=7, column=1, columnspan=4, sticky='NEW',
                padx=5)
        self.track_name.insert(0, 'Name of current track')

        # Style Configuration
        tk.Label(self, text='TRACK INDEX', font=LARGE_FONT, bg=GREY).grid(
            row=8, column=0, sticky='NSE', padx=5, pady=10)
        self.import_btn = tk.Button(self, text='IMPORT...',
                command=self.import_tracks, width=15, font=SMALL_FONT, bg=GREY,
                fg=BLACK, disabledforeground=BLACK,
                activebackground=LIGHT_GRAY)
        self.import_btn.grid(row=8, column=1, sticky='NE', pady=10, padx=5)

        tk.Label(self, text='PROGRAM -', font=LARGE_FONT, bg=GREY).grid(row=8,
            column=3, sticky='NSE', padx=5, pady=10)
        self.style_label = tk.Label(self, font=LARGE_FONT, bg=GREY)
        self.style_label.grid(row=8, column=4, sticky='NSW', padx=5, pady=10)

        self.track_listbox = tk.Listbox(self, bg=BLACK, fg=BLUE, width=40,
                font=SMALL_FONT)
        self.track_listbox.grid(row=9, column=0, columnspan=2, rowspan=8,
                sticky='NSEW', padx=5)
        self.track_listbox.bind("<<ListboxSelect>>", func=self.track_text,
                add=True)
        self.track_listbox.bind("<Double-Button-1>", self.add_track, False)

        self.style_listbox = tk.Listbox(self, bg=BLACK, fg=BLUE, width=40,
                font=SMALL_FONT)
        self.style_listbox.grid(row=9, column=3, columnspan=2, rowspan=8,
                sticky='NSEW', padx=5)
        self.style_listbox.bind("<<ListboxSelect>>", func=self.track_text,
                add=True)
        self.style_listbox.bind("<Double-Button-1>", self.remove_track, False)

        self.theme_btn = tk.Button(self, text='THEME',
                command=lambda: self.switch_style('theme'), width=15,
                font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.theme_btn.grid(row=9, column=2, sticky='NSEW', padx=10, pady=10)

        self.old_btn = tk.Button(self, text='OLD STYLE',
                command=lambda: self.switch_style('old'), width=15,
                font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.old_btn.grid(row=10, column=2, sticky='NSEW', padx=10, pady=10)

        self.new_btn = tk.Button(self, text='NEW STYLE',
                command=lambda: self.switch_style('new'), width=15,
                font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.new_btn.grid(row=11, column=2, sticky='NSEW', padx=10, pady=10)

        self.ezy_btn = tk.Button(self, text='EZY STREET',
                command=lambda: self.switch_style('ezy'), width=15,
                font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.ezy_btn.grid(row=12, column=2, sticky='NSEW', padx=10, pady=10)

        tk.Label(self, text='', bg=GREY).grid(row=13, column=2, sticky='NSEW')

        self.add_btn = tk.Button(self, text='ADD >>', command=self.add_track,
                width=15, font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.add_btn.grid(row=14, column=2, sticky='NSEW', padx=10, pady=10)

        self.remove_btn = tk.Button(self, text='<< REMOVE',
                command=self.remove_track, width=15, font=SMALL_FONT, bg=GREY,
                fg=BLACK, activebackground=LIGHT_GRAY)
        self.remove_btn.grid(row=15, column=2, sticky='NSEW', padx=10, pady=10)

        self.clear_btn = tk.Button(self, text='CLEAR',
                command=self.clear_style, width=15, font=SMALL_FONT, bg=GREY,
                fg=BLACK, activebackground=LIGHT_GRAY)
        self.clear_btn.grid(row=16, column=2, sticky='NSEW', padx=10, pady=10)

        self.save_btn = tk.Button(self, text='SAVE OBM', command=self.save_obm,
                width=15, font=SMALL_FONT, bg=GREY, fg=BLACK,
                activebackground=LIGHT_GRAY)
        self.save_btn.grid(row=17, column=4, sticky='SE', padx=5, pady=10)

    def track_text(self, *args):
        if self.track_listbox.curselection():
            self.track_label['text'] = self.track_list[
                self.track_listbox.curselection()[0]]
        elif self.style_listbox.curselection():
            self.track_label['text'] = self.style_list[
                self.style_listbox.curselection()[0]]

    def limit_shortname(self, *args):
        """Set shortname_val to four characters. Capitalize letters."""
        text = self.meta_shortname.get()[:4]
        self.shortname_val.set(text.upper())

    def set_obm(self, *args, **kwargs):
        """Assign self.obm_data to new OBMData object."""
        self.obm_data = obm.OBMData(*args, **kwargs)

    def get_confirm(self, popup, answer):
        popup.destroy()
        if answer == 'yes':
            self.confirm = True
        else:
            self.confirm = False

    def popup_yes_no(self, question):
        self.confirm = None
        popup = tk.Tk()
        popup.configure(bg=RED)
        popup.wm_title('Information')
        label = tk.Label(popup, text=question, font=MEDIUM_FONT)
        label.configure(bg=RED, fg=LIGHT_YELLOW)
        label.pack(side='top', fill='x', pady=20, padx=30)
        y_btn = tk.Button(popup, text='YES',
                command=lambda: self.get_confirm(popup, 'yes'))
        y_btn.configure(bg=YELLOW, fg=BLACK, font=SMALL_FONT, width=10)
        y_btn.pack(side='right', padx=10, pady=10)
        n_btn = tk.Button(popup, text='NO',
                command=lambda: self.get_confirm(popup, 'no'))
        n_btn.configure(bg=YELLOW, fg=BLACK, font=SMALL_FONT, width=10)
        n_btn.pack(side='left', padx=10, pady=10)

    def switch_style(self, style):
        """Assign new self.style_list values based on chosen style."""
        self.cur_style = style
        self.style_list = []
        buttons = [self.theme_btn, self.old_btn, self.new_btn, self.ezy_btn]
        for button in buttons:
            button.config(relief=tk.RAISED, bg=GREY)
        if style == 'old':
            self.old_btn.config(relief=tk.SUNKEN, bg=LIGHT_GRAY)
            self.style_list = self.obm_data.old_style
            self.style_label['text'] = '"OLD STYLE"'
        elif style == 'new':
            self.new_btn.config(relief=tk.SUNKEN, bg=LIGHT_GRAY)
            self.style_list = self.obm_data.new_style
            self.style_label['text'] = '"NEW STYLE"'
        elif style == 'ezy':
            self.ezy_btn.config(relief=tk.SUNKEN, bg=LIGHT_GRAY)
            self.style_list = self.obm_data.ezy_street
            self.style_label['text'] = '"EZY STREET"'
        elif style == 'theme':
            self.theme_btn.config(relief=tk.SUNKEN, bg=LIGHT_GRAY)
            self.style_list = self.obm_data.theme
            self.style_label['text'] = '"THEME"'
        self.update()

    def import_tracks(self):
        """Append compatible files in chosen directory to self.track_list."""
        # if self.track_list:
        #     self.popup_yes_no("""This will erase current track list.
        #         Do you wish to continue?""")
        #     if self.confirm == False:
        #         return
        #     self.track_list = []
        self.music_dir = filedialog.askdirectory()
        for f in os.listdir(self.music_dir):
            if (os.path.isfile(os.path.join(self.music_dir, f))
                    and f[-3:] == '.gm'
                    or f[-4:] == '.mid'
                    or f[-5:] == '.midi'):
                self.track_list.append(f)
        self.import_btn.config(state=tk.DISABLED, bg=DRK_GREY)
        self.update()

    def add_track(self, *args):
        if self.track_listbox.curselection():
            track = self.track_list[self.track_listbox.curselection()[0]]
        else:
            return
        if ((self.cur_style in ['old', 'new', 'ezy']
                and len(self.style_list) >= 10)
                or (self.cur_style == 'theme' and len(self.style_list) >= 1)):
                    popupinfo('Current style full.')
                    return
        self.track_list.remove(track)
        if self.cur_style == 'old':
            self.obm_data.old_style.append(track)
        elif self.cur_style == 'new':
            self.obm_data.new_style.append(track)
        elif self.cur_style == 'ezy':
            self.obm_data.ezy_street.append(track)
        elif self.cur_style == 'theme':
            self.obm_data.theme.append(track)
        self.update()

    def remove_track(self, *args):
        if self.style_listbox.curselection():
            track = self.style_list[self.style_listbox.curselection()[0]]
        else:
            return
        self.track_list.append(track)
        if self.cur_style == 'old':
            self.obm_data.old_style.remove(track)
        elif self.cur_style == 'new':
            self.obm_data.new_style.remove(track)
        elif self.cur_style == 'ezy':
            self.obm_data.ezy_street.remove(track)
        elif self.cur_style == 'theme':
            self.obm_data.theme.remove(track)
        self.update()

    def clear_style(self):
        for track in self.style_list:
            self.track_list.append(track)
        if self.cur_style == 'old':
            self.obm_data.old_style.clear()
        elif self.cur_style == 'new':
            self.obm_data.new_style.clear()
        elif self.cur_style == 'ezy':
            self.obm_data.ezy_street.clear()
        elif self.cur_style == 'theme':
            self.obm_data.theme.clear()
        self.update()

    def update(self):
        """Update self.track_listbox and self.style_listbox to new values."""
        self.track_listbox.delete(0, tk.END)
        for track in self.track_list:
            self.track_listbox.insert(tk.END, track)
        self.style_listbox.delete(0, tk.END)
        for track in self.style_list:
            self.style_listbox.insert(tk.END, track)

    def save_obm(self, directory=None):
        if not directory:
            directory = filedialog.askdirectory()
        metadata = [self.meta_name.get(), self.meta_shortname.get(),
                self.meta_version.get(), self.meta_description.get(),
                self.meta_origin.get()]
        self.obm_data.meta_data = dict(zip(self.obm_data.meta_data.keys(),
                                           metadata))
        self.obm_data.create_file(obm_dir=directory, music_dir=self.music_dir)


if __name__ == '__main__':
    app = OBMApp()
    app.mainloop()
