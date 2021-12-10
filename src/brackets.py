#!/usr/bin/python3


import gi
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('OsmGpsMap', '1.0')

from gi.repository import Gtk, Granite, GObject
from gi.repository import OsmGpsMap as osm

print(f"using library: {osm.__file__} (version {osm._version})")

try:
    import constants as cn
    import teams as tm
    import handler as hd
except ImportError:
    import escapade.constants as cn
    import escapade.teams as tm
    import escapade.handler as hd

class Brackets(Gtk.Box):

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

        # https://github.com/nzjrs/osm-gps-map/blob/master/examples/mapviewer.py
        m = osm.Map()
        m.layer_add(
            osm.MapOsd(show_dpad=True,
                       show_zoom=True,
                       show_crosshair=True)
        )
        m.set_property("map-source", osm.MapSource_t.OPENSTREETMAP)
        m.layer_add(self.DummyLayer())
        self.add(m)
        
    class DummyLayer(GObject.GObject, osm.MapLayer):
        def __init__(self):
            GObject.GObject.__init__(self)

        def do_draw(self, gpsmap, gdkdrawable):
            pass

        def do_render(self, gpsmap):
            pass

        def do_busy(self):
            return False

        def do_button_press(self, gpsmap, gdkeventbutton):
            return False