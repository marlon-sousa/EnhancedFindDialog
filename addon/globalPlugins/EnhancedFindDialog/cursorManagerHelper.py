# -*- coding: UTF-8 -*-
#A part of the EnhancedFind addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import config
from cursorManager import CursorManager
import gui
from . import guiHelper
from logHandler import log
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
	# scripts that will call the enhancedFindDialog
	CursorManager.script_find = script_enhancedFind
	CursorManager.script_findNext = script_enhancedFindNext
	CursorManager.script_findPrevious = script_EnhancedFindPrevious


def script_enhancedFind(self,gesture):
	# #8566: We need this to be a modal dialog, but it mustn't block this script.
	def run():
		gui.mainFrame.prePopup()
		d = guiHelper.EnhancedFindDialog(gui.mainFrame, self, self._lastCaseSensitivity, self._searchEntries)
		d.ShowModal()
		gui.mainFrame.postPopup()
	log.debug("calling")
	wx.CallAfter(run)

def script_enhancedFindNext(self,gesture):
	if not self._searchEntries:
		self.script_find(gesture)
		return
	self.doFindText(self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX], caseSensitive = self._lastCaseSensitivity)


def script_EnhancedFindPrevious(self,gesture):
	if not self._searchEntries:
		self.script_find(gesture)
		return
	self.doFindText(self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX], reverse=True, caseSensitive = self._lastCaseSensitivity)