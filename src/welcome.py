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
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

import constants as cn

class Welcome(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent

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

        '''Here we are creating a new Welcome Widget from the Granite library'''
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new(
            _("Welcome"),
            cn.App.application_description
        )

        '''Let's populate the Welcome menu actions.'''
        welcome.append(
            "document-new", # the action icon (a valid icon name)
            _('New tournament'), # the action name
            _('Open a new tournament window') # the action description
        )
        welcome.append(
            "document-open-recent",
            _('Open recent tournament'),
            _('Open a recent Tournament session from file')
        )

        '''Here we are connecting the on_welcome_activated method to the
        activated signal of the Welcome Widget, so this will be triggered
        when an action is activated'''
        welcome.connect("activated", self.on_welcome_activated)

        self.parent.parent.hbar.hbar_save_file.set_sensitive(False)
        self.parent.parent.hbar.hbar_print.set_sensitive(False)

        '''Do you remember the Box we were talking about at the beginning?
        Here, we add the Welcome Widget to this.'''
        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        '''The activated signal return an index with the activated item, we
        will use this to perform different actions'''
        self.parent.parent.hbar.hbar_save_file.set_sensitive(True)
        self.parent.parent.hbar.hbar_print.set_sensitive(True)
        if index == 0:
            # New Tournament
            self.parent.stack.set_visible_child_name("initialisation")
        else:
            # Open Recent
            self.parent.stack.set_visible_child_name("brackets")
