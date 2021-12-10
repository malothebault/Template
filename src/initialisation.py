#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite, Gdk

try:
    import constants as cn
    import listofname as ln
    import brackets as bk
except ImportError:
    import tournoi.constants as cn
    import tournoi.listofname as ln
    import tournoi.brackets as bk

class Initialisation(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
        self.listofname = ln.ListOfName(self)
        self.parent = parent
        self.nb = 2
        self.returned_list = []

        ########### TRANSLATION ##############
        try:
           current_locale, encoding = locale.getdefaultlocale()
           locale_path = os.path.join(
               os.path.abspath(
                   os.path.dirname(__file__)
               ), 
               'locale'
           )
           translate = gettext.translation(
               cn.App.application_shortname, 
               locale_path, 
               [current_locale] 
           )
           _ = translate.gettext
        except FileNotFoundError:
           _ = str
        self._ = _
        ######################################

        self.set_border_width(80)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        grid = Gtk.Grid.new()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(35)
        grid.set_column_spacing(35)
        
        # Widgets creation
        scroll_w = Gtk.ScrolledWindow.new(None, None)
        self.listbox = Gtk.ListBox.new()
        self.listbox.get_style_context().add_class('config-list-box')
        scroll_w.add(self.listbox)
        validate_button = Gtk.Button.new_with_label(_("Validate"))
        validate_button.get_style_context().add_class('suggested-action')
        validate_button.connect("clicked", self.on_validate_clicked)
        nb_team_button = Gtk.SpinButton.new_with_range(2,8,1)
        nb_team_button.connect("value_changed", self.on_spin_button_value_changed)
        random_team_attributes = Gtk.Button.new_with_label(_("Random team names and colors"))
        random_team_attributes.connect("clicked", self.on_random_team_attributes_clicked)
        
        self.row_list = []
        self.box_list = []
        for i in range(self.nb):
            self.new_row(i)
        
        # Attach widgets to the grid
        grid.attach(nb_team_button, 0, 0, 1, 1)
        grid.attach(random_team_attributes, 1, 0, 1, 1)
        grid.attach(scroll_w, 0, 1, 2, 4)
        grid.attach(validate_button, 1, 5, 1, 1)
        
        self.pack_start(grid, True, False, 0)
        
    def on_spin_button_value_changed(self, widget):
        nbr = widget.get_value_as_int()
        if nbr > self.nb:
            self.nb = nbr
            self.new_row(self.nb - 1)
            self.listbox.show_all()
        elif nbr < self.nb:
            self.remove_row(self.nb - 1)
            self.listbox.show_all()
            self.nb = nbr
        else:
            None

    def on_validate_clicked(self, widget):
        for i in self.box_list:
            child = i.get_children()
            text = child[0].get_text()
            color = child[1].get_color()
            self.returned_list.append({'name':text, 'color':color})
        self.parent.brackets = bk.Brackets(self.parent, self.returned_list)
        self.parent.stack.add_titled(self.parent.brackets, "brackets", "Brackets")
        self.parent.brackets.show_all()
        self.parent.stack.set_visible_child_name("brackets")
        
    def on_random_team_attributes_clicked(self, widget):
        for i in self.box_list:
            child = i.get_children()
            child[0].set_text(self.listofname.select_random())
        
    def get_nb_team(self):
        return self.nb
    
    def new_row(self, i):
        self.row_list.append(Gtk.ListBoxRow())
        self.box_list.append(Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100))
        self.box_list[i].set_border_width(10)
        entry = Gtk.Entry()
        entry.set_placeholder_text("Team name")
        color = Gtk.ColorButton.new_with_rgba(Gdk.RGBA(255, 255, 255, 255))
        self.box_list[i].pack_start(entry, True, True, 0)
        self.box_list[i].pack_end(color, False, False, 0)
        self.row_list[i].add(self.box_list[i])
        self.listbox.add(self.row_list[i])
    
    def remove_row(self, i):
        self.listbox.remove(self.row_list[i])
        del self.box_list[i]
        del self.row_list[i]
