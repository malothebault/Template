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

class Teams:
    def __init__(self, nb_of_teams):
        self.nb_of_teams = nb_of_teams
    
    def create(self):
        None
