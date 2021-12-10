#!/usr/bin/python3


from gi.repository import Gtk, Granite, Gdk
import gi
import subprocess
import os
import locale
import gettext
import webbrowser
import random

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')


try:
    import constants as cn
except ImportError:
    import tournoi.constants as cn


class Handler:
    def __init__(self, parent, list_of_teams):

        self.list_of_teams = list_of_teams
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

        self._list_to_return = []
        next_power_of_2, nb_of_round, nb_of_box = self.nb_of_round(
            self.get_nb_of_teams())
        nb_of_ghosts = next_power_of_2 - self.get_nb_of_teams()

        for i in range(next_power_of_2):
            if i < nb_of_ghosts:
                team = Team(_("Ghost ")+str(i+1))
                self._list_to_return.append(team)
            else:
                team = Team(list_of_teams[i - nb_of_ghosts].get('name'),
                            list_of_teams[i - nb_of_ghosts].get('color'))
                self._list_to_return.append(team)

        random.shuffle(self._list_to_return)
        for team in self._list_to_return:
            i = self._list_to_return.index(team)
            team.coordinate = (i % 2, (i//2)*2)

        for i in range(nb_of_box - len(self._list_to_return)):
            not_a_team = NotATeam()
            not_a_team.coordinate = (i, (i//2)*2 + 1)
            self._list_to_return.append(not_a_team)

        # i = 0
        # while (len(self._list_to_return) < nb_of_box) / 2:
        #     if ((i//2)*2) % 2 == 0:
        #         self._list_to_return[i].coordinate = (
        #             i % 2, (i//2)*2)  # Col, Row
        #         self._list_to_return[-(i+1)].coordinate = (i % 2, (i//2)*2)

    def get_nb_of_teams(self):
        return len(self.list_of_teams)

    @property
    def list_to_return(self):
        return self._list_to_return

    @staticmethod
    def nb_of_round(x):
        if x == 0:
            next_power_of_2 = 1
            nb_of_round = 1
            nb_of_box = 2
        else:
            next_power_of_2 = (2**(x - 1).bit_length())
            nb_of_round = (x - 1).bit_length()
            nb_of_box = 0
            for n in range(nb_of_round):
                nb_of_box += 2**n
        return (next_power_of_2, nb_of_round, nb_of_box)


class Team:
    def __init__(self, name, color=Gdk.RGBA(255, 255, 255, 255)):
        self.name = name  # Name
        self._coordinate = (0, 0)  # Coordinate
        self.color = color  # Color
        self.score = 0  # Score
        self.box = Gtk.Box()  # Button
        ICON_SIZE = Gtk.IconSize.MENU
        team_name_label = Gtk.Label(self.name)
        self.box.pack_start(team_name_label, True, True, 0)
        edit_button = Gtk.Button.new_from_icon_name(
            "accessories-text-editor-symbolic", ICON_SIZE)
        edit_button.connect('clicked', self.on_edit_button_clicked)
        self.box.pack_end(edit_button, False, False, 6)
        delete_button = Gtk.Button.new_from_icon_name(
            "edit-delete-symbolic", ICON_SIZE)
        delete_button.get_style_context().add_class('destructive-action')
        delete_button.valign = Gtk.Align.CENTER
        delete_button.connect('clicked', self.on_delete_button_clicked)
        self.box.pack_end(delete_button, False, False, 6)

    @ property
    def coordinate(self):
        return self._coordinate

    @ coordinate.setter
    def coordinate(self, value):
        self._coordinate = value

    def on_edit_button_clicked(self, widget):
        print("edit")

    def on_delete_button_clicked(self, widget):
        print("delete")


class NotATeam:
    def __init__(self):
        self._coordinate
        self.box = Gtk.Box()  # Button

    @ property
    def coordinate(self):
        return self._coordinate

    @ coordinate.setter
    def coordinate(self, value):
        self._coordinate = value
