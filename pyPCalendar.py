#! /usr/bin/python2
# coding=utf-8

import os
import gtk
import pango
import datetime
import cairo
from pyJCal import *


class pyPCalendar():
	def __init__(self):
		self._Winwo_bgImg =  './images/calendar_single.png'
				
		#Create Window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		
		#Set Signals
		self.window.connect("expose_event", self.expose)
		self.window.connect("destroy", gtk.main_quit)
		
		#Set Window PRoperties
		self.window.set_decorated(False)
		self.window.set_size_request(130, 141)
		self.window.move(1220,50)
		self.window.set_property('skip-taskbar-hint', True)
		self.window.set_transient_for(None)
		self.window.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DOCK)
		self.window.stick()
		self.window.set_keep_below(True)
		
		#Initialize colors, alpha transparency	
		self.window.set_app_paintable(True)
		self.gtk_screen = self.window.get_screen()
		colormap = self.gtk_screen.get_rgba_colormap()
		if colormap == None:
			colormap = self.gtk_screen.get_rgb_colormap()
		gtk.widget_set_default_colormap(colormap)
		if self.window.is_composited():
			self.supports_alpha = True
		else:
			self.supports_alpha = False
		
		self.w,self.h = self.window.get_size()
		
		
	def expose (self, widget, event):
		self.ctx = self.window.window.cairo_create()
		# set a clip region for the expose event, XShape stuff
		self.ctx.save()
		if self.supports_alpha == False:
			self.ctx.set_source_rgb(1, 1, 1)
		else:
			self.ctx.set_source_rgba(1, 1, 1, 0)
			
		self.ctx.set_operator (cairo.OPERATOR_SOURCE)
		self.ctx.paint()
		self.ctx.restore()
		self.ctx.rectangle(event.area.x, event.area.y,event.area.width, event.area.height)
		self.ctx.clip()
		self.draw_image(self.ctx,0,0, self._Winwo_bgImg)
		
	def draw_image(self,ctx,x,y, pix):
		"""Draws a picture from specified path with a certain width andheight"""

		ctx.save()
		ctx.translate(x, y)	
		pixbuf = gtk.gdk.pixbuf_new_from_file(pix)
		format = cairo.FORMAT_RGB24
		if pixbuf.get_has_alpha():
			format = cairo.FORMAT_ARGB32
	
		iw = pixbuf.get_width()
		ih = pixbuf.get_height()
		image = cairo.ImageSurface(format, iw, ih)
		image = ctx.set_source_pixbuf(pixbuf, 0, 0)
		
		ctx.paint()
		puxbuf = None
		image = None
		ctx.restore()
		ctx.clip()
		
	def setup(self):
		today = datetime.date.today()
		
		jCal = pyJCal()
		
		jy, jm, jd = jCal.gregorian_to_jalali(today.year, today.month, today.day)
		#print "%s/%s/%s\n" % (jy,jm,jd)
		#print jCal.MonthName(jm)
		jMonthName = jCal.MonthName(jm)
		jWeekDayName = jCal.WeekDayName(datetime.datetime.now().strftime('%A'))
		
		str_CYear_Month = '<span foreground="#888888">%s %d</span>' % (jMonthName, jy)
		str_CDay = '<span foreground="#888888" font_desc="Sans normal 35">%d</span>' % (jd)
		str_CDay_Week = '<span foreground="#888888"><b>%s</b></span>' % (jWeekDayName)
		
		str_bToday = '<span foreground="#888888"><b>%s</b></span>' % (today)
				
		#geregoorian 
		gLabel = gtk.Label()
		gLabel.set_markup(str_bToday)
		gLabel.set_tooltip_text(datetime.datetime.now().strftime('%B'))
		
		#current persian year and month
		ymLabel = gtk.Label()
		ymLabel.set_markup(str_CYear_Month)
		
		#current persian day
		dmLabel = gtk.Label()
		dmLabel.set_markup(str_CDay)
		
		#Current Week day name
		wmLabel = gtk.Label()
		wmLabel.set_markup(str_CDay_Week)
		
		
		lTabele = gtk.Table(6, 1, True)
		
		lTabele.attach(ymLabel, 0, 1, 0, 3, gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)
		lTabele.attach(dmLabel, 0, 1, 2, 4, gtk.FILL|gtk.EXPAND, gtk.FILL, 0, 0)
		lTabele.attach(wmLabel, 0, 1, 3, 5, gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 0)
		lTabele.attach(gLabel, 0, 1, 4, 6, gtk.FILL|gtk.EXPAND, gtk.FILL|gtk.EXPAND, 0, 5)
		
		self.window.add(lTabele)
		
	def show_window(self):
		self.window.show_all()
		while gtk.events_pending():
			gtk.main_iteration()
		self.window.present()
		self.window.grab_focus()
		#self.p = 1

if __name__ == "__main__":
	pC = pyPCalendar()
	pC.setup()
	pC.show_window()
	gtk.main()
