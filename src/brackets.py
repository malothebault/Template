#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

try:
    import constants as cn
    import teams as tm
    import handler as hd
except ImportError:
    import tournoi.constants as cn
    import tournoi.teams as tm
    import tournoi.handler as hd

class Brackets(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent, init_list):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent
        self.init_list = init_list
        # print(self.init_list)
        icon_size = Gtk.IconSize.MENU

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
        
        brackets = Gtk.Grid.new()
        brackets.set_column_homogeneous(True)
        brackets.set_row_homogeneous(True)
        brackets.set_row_spacing(35)
        brackets.set_column_spacing(35)
        
        WIDTH = 1
        HEIGHT = 1
        if self.init_list != []:
            handler = hd.Handler(self, self.init_list)  ## A ajouter
            handler_list = handler.list_to_return
            for team in handler_list:
                brackets.attach(team.box,team.coordinate[0],team.coordinate[1],WIDTH,HEIGHT)
                
        self.pack_start(brackets, True, True, 0)
        

