#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin <send@mirko.pm>

   This file is part of ElementaryPython.

    ElementaryPython is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ElementaryPython is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ElementaryPython.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
import webbrowser
import os
import locale
import gettext
import constants as cn

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
######################################

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

import constants as cn

class Headerbar(Gtk.HeaderBar):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):

        Gtk.HeaderBar.__init__(self)
        self.parent = parent
        self._ = _

        '''Here we are setting some parameters for the HeaderBar
        <https://developer.gnome.org/gtk3/stable/GtkHeaderBar.html>'''
        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        '''NEW DOCUMENT BUTTON'''
        self.hbar_new_file = Gtk.ToolButton() # a new instance
        self.hbar_new_file.set_icon_name( # setting the button icon name
            "document-new" 
        ) 
        self.hbar_new_file.connect( # connecting our method to the clicked signal
            "clicked", 
            self.on_hbar_new_file_clicked
        )
        self.pack_start( # packing the button to the start of the HeaderBar
            self.hbar_new_file
        )
        
        '''OPEN DOCUMENT BUTTON'''
        self.hbar_open_file = Gtk.ToolButton() # a new instance
        self.hbar_open_file.set_icon_name( # setting the button icon name
            "document-open" 
        ) 
        self.hbar_open_file.connect( # connecting our method to the clicked signal
            "clicked", 
            self.on_hbar_open_file_clicked
        )
        self.pack_start( # packing the button to the start of the HeaderBar
            self.hbar_open_file
        )
        
        '''SAVE DOCUMENT BUTTON'''
        self.hbar_save_file = Gtk.ToolButton() # a new instance
        self.hbar_save_file.set_icon_name( # setting the button icon name
            "document-save" 
        ) 
        self.hbar_save_file.connect( # connecting our method to the clicked signal
            "clicked", 
            self.on_hbar_save_file_clicked
        )
        self.pack_start( # packing the button to the start of the HeaderBar
            self.hbar_save_file
        )
        
        '''Another button, this can be used for choosing Application colors'''
        # self.hbar_color = Gtk.ColorButton.new_with_rgba(
        #     Gdk.RGBA(222, 222, 222, 255)
        # )
        # self.hbar_color.connect(
        #     "color_set", 
        #     self.on_hbar_color_color_set
        # )
        # self.pack_end(self.hbar_color)
        
        '''THEME BUTTON'''
        self.hbar_theme = Gtk.ToolButton()
        self.hbar_theme.set_icon_name("weather-clear-night") 
        self.hbar_theme.connect(
            "clicked",
            self.on_hbar_theme_switcher
        )
        self.pack_end(self.hbar_theme)

    '''ACTIONS'''
    def on_hbar_new_file_clicked(self, widget):
        self.parent.stack.set_visible_child_name("initialisation")
        
    def on_hbar_open_file_clicked(self, widget):
        dialog = Gtk.FileChooserNative.new("Please choose a file",
                                            self.parent,
                                            Gtk.FileChooserAction.OPEN,
                                            "Open",
                                            "Cancel")
        response = dialog.run()
        print(response)
        if response == Gtk.ResponseType.ACCEPT:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.parent.main_file["name"] = dialog.get_filename()[::-1].split("/", 1)[0][::-1]
            self.parent.main_file["path"] = dialog.get_filename()
            self.parent.stack.set_visible_child_name("initialisation")
        dialog.destroy() 
    
    def on_hbar_save_file_clicked(self, widget):
        None

    # def on_hbar_color_color_set(self, widget):
    #     print("Hi")
    #     cn.Colors.primary_color = widget.get_rgba().to_string()

    #     stylesheet = f"""
    #         @define-color colorPrimary {cn.Colors.primary_color};
    #         @define-color textColorPrimary {cn.Colors.primary_text_color};
    #         @define-color textColorPrimaryShadow {cn.Colors.primary_text_shadow_color};
    #     """

    #     style_provider = Gtk.CssProvider()
    #     style_provider.load_from_data(bytes(stylesheet.encode()))
    #     Gtk.StyleContext.add_provider_for_screen(
    #         Gdk.Screen.get_default(), 
    #         style_provider,
    #         Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    #     )
    
    def on_hbar_theme_switcher(self, widget):
        theme = self.settings.get_property(
            "gtk-application-prefer-dark-theme"
        )
        self.settings.set_property(
            "gtk-application-prefer-dark-theme", 
            not theme # theme is a bool, we are reversing it
        )
