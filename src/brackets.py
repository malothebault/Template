#!/usr/bin/python3

import gi
import subprocess
import os
import locale
import gettext

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite, GObject, Gdk

try:
    import constants as cn
    import teams as tm
    import handler as hd
except ImportError:
    import escapade.constants as cn
    import escapade.teams as tm
    import escapade.handler as hd
    
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

class Brackets(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self, parent):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent
        self._ = _
        self.set_border_width(80)
        
        # higher values make movement more performant
        # lower values make movement smoother
        self.SENSITIVITY = 1

        self.EvMask = Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.BUTTON1_MOTION_MASK

        self.offsetx = 0
        self.offsety = 0
        self.px = 0
        self.py = 0
        self.maxx = 0
        self.maxy = 0

        # fixed container
        self.fixed = Gtk.Fixed()
        self.add(self.fixed)

        # buttons
        self.fixed.put(self.make_button("A button"), 50, 50)
        self.fixed.put(self.make_button("Another button"), 250, 100)

    def Min(self, a, b):
        if  b < a:
            return b
        return a

    def Max(self, a, b):
        if b > a:
            return b
        return a

    def RoundDownToMultiple(self, i, m):
        return i/m*m

    def RoundToNearestMultiple(self, i, m):
        if i % m > m / 2:
            return (i/m+1)*m
        return i/m*m


    def button_press_event(self, widget, event):
        if event.button == 1:
            p = widget.get_parent()
            # offset == distance of parent widget from edge of screen ...
            # global offsetx, offsety
            self.offsetx, self.offsety =  p.get_window().get_position()
            # plus distance from pointer to edge of widget
            self.offsetx += event.x
            self.offsety += event.y
            # maxx, maxy both relative to the parent
            # note that we're rounding down now so that these max values don't get
            # rounded upward later and push the widget off the edge of its parent.
            
            self.maxx = self.RoundDownToMultiple(p.get_allocation().width - widget.get_allocation().width, self.SENSITIVITY)
            self.maxy = self.RoundDownToMultiple(p.get_allocation().height - widget.get_allocation().height, self.SENSITIVITY)


    def motion_notify_event(self, widget, event):
        # x_root,x_root relative to screen
        # x,y relative to parent (fixed widget)
        # px,py stores previous values of x,y

        # get starting values for x,y
        x = event.x_root - self.offsetx
        y = event.y_root - self.offsety
        # make sure the potential coordinates x,y:
        #   1) will not push any part of the widget outside of its parent container
        #   2) is a multiple of SENSITIVITY
        x = self.RoundToNearestMultiple(self.Max(self.Min(x, self.maxx), 0), self.SENSITIVITY)
        y = self.RoundToNearestMultiple(self.Max(self.Min(y, self.maxy), 0), self.SENSITIVITY)
        if x != self.px or y != self.py:
            self.px = x
            self.py = y
            self.fixed.move(widget, x, y)

    def make_button(self, text):
        b = Gtk.Button.new_with_label(text)
        b.set_events(self.EvMask)
        b.connect("button_press_event", self.button_press_event)
        b.connect("motion_notify_event", self.motion_notify_event)
        b.show()
        return b
    
    
# import fitz

# src_pdf_filename = 'source.pdf'
# dst_pdf_filename = 'destination.pdf'
# img_filename = 'barcode.jpg'

# # http://pymupdf.readthedocs.io/en/latest/rect/
# # Set position and size according to your needs
# img_rect = fitz.Rect(100, 100, 120, 120)

# document = fitz.open(src_pdf_filename)

# # We'll put image on first page only but you could put it elsewhere
# page = document[0]
# page.insertImage(img_rect, filename=img_filename)

# # See http://pymupdf.readthedocs.io/en/latest/document/#Document.save and
# # http://pymupdf.readthedocs.io/en/latest/document/#Document.saveIncr for
# # additional parameters, especially if you want to overwrite existing PDF
# # instead of writing new PDF
# document.save(dst_pdf_filename)

# document.close()

