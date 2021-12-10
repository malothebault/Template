#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser
import random

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

try:
    import constants as cn
except ImportError:
    import tournoi.constants as cn


class ListOfName:
    def __init__(self, parent):
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

        self.list_adjectives = [
            "Cute",
            "Mad",
            "Happy",
            "Angry",
            "Starving",
        ]

        self.list_animals = [
            "Elephants",
            "Crocodiles",
            "Dogs",
            "Cats",
            "Chickens",
            "Tigers",
            "Lions",
            "Cows"
        ]


    def select_random(self):
        adj = random.choice(self.list_adjectives)
        ani = random.choice(self.list_animals)
        return "The " + adj + " " + ani
