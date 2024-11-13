# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
import buildVersion
import config
import controlTypes
from cursorManager import CursorManager
import gui
from . import guiHelper
import inspect
import re
import speech
from scriptHandler import willSayAllResume, script
import textInfos
from tones import beep
import wx

# this addon mostly complements NVDA functionalities.
# however, because the way NVDA works, when you use
# addon translation infrastructure by calling addonHandler.initTranslation() you loose access to the
# NVDA translated strings
# It is all or nothing: if you call addonHandler.initTranslation() the _(str) function looks for translations
# only in the addon localization files.
# if you don't, then the _(str) function looks for translations in the NVDA localization files,
# but not in the addon localization files
# In this addon, we add new elements to specific dialogs.
# Of course the translations for these elements are not available in nvda localization files.
# In the other hand, we use lots of strings that are already translated in NVDA
# So now we need to access the nvda localization files to have already defined translations, but
# we also need to access addon translation files to translate custom dialogs
# What we did is we saved the nvda translator to the __ variable
# while _ variable now is used to translate addon strings

__ = _
addonHandler.initTranslation()

# search history list constants
SEARCH_HISTORY_MOST_RECENT_INDEX = 0
SEARCH_HISTORY_LEAST_RECENT_INDEX = 19


# Workaround to support the new find error dialog title introduced in NVDA 2024.1
if buildVersion.version_year > 2023:
	# Translators: message dialog title displayed to the user when
	# searching text and no text is found.
	FIND_ERROR_DIALOG_TITLE = __("0 matches")
else:
	FIND_ERROR_DIALOG_TITLE = __("Find Error")


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


def script_enhancedFind(self, gesture, reverse=False):
	# #8566: We need this to be a modal dialog, but it mustn't block this script.
	def run():
		# get the active profile and send that to the find dialog
		# this is needed because whenever the find dialog is opened the default profile is loaded.
		# We, however, want to retrieve state from the active profile when the find dialog was loaded
		profile = config.conf.getActiveProfile()

		gui.mainFrame.prePopup()
		d = guiHelper.EnhancedFindDialog(gui.mainFrame, self, profile, self._searchEntries, reverse)
		d.ShowModal()
		gui.mainFrame.postPopup()
	wx.CallAfter(run)


def script_enhancedFindNext(self, gesture):
	if not self._searchEntries:
		self.script_find(gesture)
		return
	doFindText(
		self,
		self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX],
		caseSensitive=self._lastCaseSensitivity,
		searchWrap=self._searchWrap,
		willSayAllResume=willSayAllResume(gesture),
	)


def script_EnhancedFindPrevious(self, gesture):
	if not self._searchEntries:
		self.script_find(gesture, reverse=True)
		return
	doFindText(
		self,
		self._searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX],
		reverse=True,
		caseSensitive=self._lastCaseSensitivity,
		searchWrap=self._searchWrap,
		willSayAllResume=willSayAllResume(gesture)
	)


def doFindText(cursorManagerInstance, text,
               reverse=False, caseSensitive=False, searchWrap=False, willSayAllResume=False):  # noqa: E101
	if not text:
		return

	info = cursorManagerInstance.makeTextInfo(textInfos.POSITION_CARET)
	res = performSearch(cursorManagerInstance, text, info, reverse, caseSensitive, searchWrap)
	if res:
		cursorManagerInstance.selection = info
		speech.cancelSpeech()
		info.move(textInfos.UNIT_LINE, 1, endPoint="start")
		info.expand(textInfos.UNIT_LINE)
		if not willSayAllResume:
			speech.speakTextInfo(info, reason=controlTypes.OutputReason.CARET)
	else:
		wx.CallAfter(gui.messageBox, __('text "%s" not found') % text,
		             FIND_ERROR_DIALOG_TITLE, wx.OK | wx.ICON_ERROR)  # Noqa E101
	CursorManager._lastFindText = text
	CursorManager._lastCaseSensitivity = caseSensitive
	CursorManager._searchWrap = searchWrap


def performSearch(cursorManager, text, info, reverse, caseSensitive, wrapSearch):
	res = info.find(text, reverse=reverse, caseSensitive=caseSensitive)
	# if either not interested in search wrapping or we have found a result then we are done here
	if not wrapSearch or res:
		return res
	found = False
	while info.find(text, reverse=(not reverse), caseSensitive=caseSensitive):
		found = True
	if found:
		beep(440, 30)
		return found

	# We currently have no content either above or below the current selection matching the searched text
	# we now have to check if the selection itself matches the searched text, meaning
	# that there is only one instance of the searched text in the whole content.
	# If it does, because we are in screen wrapping mode, we have to beep and returm the current selection
	# otherwise, we can safely return that the searched text is not matched
	# currently, the findTextInfo function either advances or returns one position before
	# proceeding with the search, which is something we are not interested in
	info = cursorManager.makeTextInfo(textInfos.POSITION_CARET).copy()
	info.expand(textInfos.UNIT_STORY)
	inText = info._get_text()
	found = re.search(re.escape(text), inText, (0 if caseSensitive else re.IGNORECASE) | re.UNICODE)
	if found:
		beep(440, 30)
	return found


# Patch say all functionality.
# Fix the patched script losing the reference to the decorated say all,
# documentation and other necessary attributes for the gesture
def _copyScriptAttributes(oldScript, newScript):
	for parameterName in inspect.signature(script).parameters.keys():
		attributeName = "__doc__" if parameterName == "description" else parameterName
		if hasattr(oldScript, attributeName):
			setattr(newScript, attributeName, getattr(oldScript, attributeName))


_copyScriptAttributes(CursorManager.script_find, script_enhancedFind)
_copyScriptAttributes(CursorManager.script_findNext, script_enhancedFindNext)
_copyScriptAttributes(CursorManager.script_findPrevious, script_EnhancedFindPrevious)
