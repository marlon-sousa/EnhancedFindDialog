# -*- coding: UTF-8 -*-
#A part of the EnhancedFind addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import config
import controlTypes
from cursorManager import CursorManager
import gui
from . import guiHelper
import speech
import textInfos
from tones import beep
import ui
import os
import wx

# search history list constants
SEARCH_HISTORY_MOST_RECENT_INDEX = 0
SEARCH_HISTORY_LEAST_RECENT_INDEX = 19


def patchCursorManager():
	#  History of search terms.
	# Sorted in most to least recently searched order.
	# First, most recently searched item index: SEARCH_HISTORY_MOST_RECENT_INDEX
	# Last, least recently searched item index: SEARCH_HISTORY_LEAST_RECENT_INDEX
	# Items that differ only by case will only have one entry. 
	CursorManager._searchEntries = []
	CursorManager._searchWrap = False
	# scripts that will call the enhancedFindDialog
	CursorManager.script_find = script_enhancedFind
	CursorManager.script_findNext = script_enhancedFindNext
	CursorManager.script_findPrevious = script_EnhancedFindPrevious
	# our enhanced dfind text method
	CursorManager.doFindText = doFindText


def script_enhancedFind(self,gesture):
	# #8566: We need this to be a modal dialog, but it mustn't block this script.
	def run():
		# get the active profile and send that to the find dialog
		# this is needed because whenever the find dialog is opened the default probile is loaded. We, however, want to retrieve state from the active profile when the find dialog was loaded
		profile = config.conf.getActiveProfile()

		gui.mainFrame.prePopup()
		d = guiHelper.EnhancedFindDialog(gui.mainFrame, self, profile, self._searchEntries)
		d.ShowModal()
		gui.mainFrame.postPopup()
	wx.CallAfter(run)

def script_enhancedFindNext(self,gesture):
	if not self._searchEntries:
		self.script_find(gesture)
		return
	self.doFindText(self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX], caseSensitive = self._lastCaseSensitivity, searchWrap = self._searchWrap)


def script_EnhancedFindPrevious(self,gesture):
	if not self._searchEntries:
		self.script_find(gesture)
		return
	self.doFindText(self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX], reverse=True, caseSensitive = self._lastCaseSensitivity, searchWrap = self._searchWrap)

def doFindText(self,text,reverse=False,caseSensitive=False, searchWrap = False):
	if not text:
		return
	
	info=self.makeTextInfo(textInfos.POSITION_CARET)
	res = performSearch(text, info, reverse, caseSensitive, searchWrap)
	if res:
		self.selection=info
		speech.cancelSpeech()
		info.move(textInfos.UNIT_LINE,1, endPoint="start")
		info.expand(textInfos.UNIT_LINE)
		speech.speakTextInfo(info,reason=controlTypes.REASON_CARET)
	else:
		wx.CallAfter(gui.messageBox,_('text "%s" not found')%text,_("Find Error"),wx.OK|wx.ICON_ERROR)
	CursorManager._lastFindText=text
	CursorManager._lastCaseSensitivity=caseSensitive
	CursorManager._searchWrap = searchWrap

def performSearch(text, info, reverse, caseSensitive, wrapSearch):
	res=info.find(text, reverse = reverse, caseSensitive = caseSensitive)
	# if either not interested in search wrapping or we have found a result then we are done here
	if not wrapSearch or res:
		return res
	found = False
	while info.find(text,reverse= not reverse, caseSensitive=caseSensitive):
		found = True
	if found:
		beep(440, 30)
	return found
	