# -*- coding: utf-8 -*-
import xbmc
import os
import xbmcaddon
import shutil
from zipfile import ZipFile
import xbmcgui
import urllib2
import time

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon("script.kangool.update")

if addon.getSetting('url') == "TVSKIN Orange":
    url="http://beam2.tk/tvorange"
    dialog.notification("K. Updater","TV+ Skin Orange Wird Geladen",sound=False)
else:
    if addon.getSetting('url') == "TVSKIN Violett":
        url="http://beam2.tk/tvviolett"
        dialog.notification("K. Updater","TV+ Skin Violett Wird Geladen",sound=False)

if addon.getSetting('url') == "TVSKIN Blue":
        url="http://beam2.tk/tvblue"
        dialog.notification("K. Updater","TV+ Skin Blau Wird Geladen",sound=False)
else:
    if addon.getSetting('url') == "Build K.":
        url="http://beam2.tk/buildkan"
        dialog.notification("K. Updater","Kangool's Build Wird Geladen",sound=False)
        
if addon.getSetting('url') == "Build C.":
        url="http://beam2.tk/ckodi"
        dialog.notification("K. Updater","cHarOns's Build Wird Geladen",sound=False)


out=os.path.join(xbmc.translatePath("special://home/upd.zip"))
page=urllib2.urlopen(url)
open(out,"wb").write(page.read())
time.sleep(5)
dialog.notification("K. Updater","Daten wurde heruntergeladen...Verarbeite Daten und Einstellungen",sound=False)
with ZipFile(xbmc.translatePath("special://home/upd.zip"), 'r') as zf:
    zf.extractall(xbmc.translatePath("special://home/"))
time.sleep(5)
if os.path.exists(out):
    os.remove(out)
time.sleep(2)

if dialog.ok("K. Updater","Kodi beenden um Update zu übernehmen!"):
    os._exit(1)
