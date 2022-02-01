#!/usr/bin/python3

import os
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite

import constants as cn
import welcome as wl
import page_one
import page_two

class Stack(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.parent = parent
        
        self.main_file = {"name": "", "path": ""}

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(250)
        
        self.welcome = wl.Welcome(self)
        self.page_one = page_one.PageOneClass(self)
        self.page_two = page_two.PageTwoClass(self)

        self.stack.add_titled(self.welcome, "welcome", "Welcome")
        self.stack.add_titled(self.page_one, "page_one", "Page One")
        self.stack.add_titled(self.page_two, "page_two", "Page Two")

        self.pack_start(self.stack, True, True, 0)
