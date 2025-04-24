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
import textInfos.offsets
import textUtils
from . import guiHelper
from .searchHistory import SearchHistory
from .searchType import SearchType
import inspect
from logHandler import log
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
	CursorManager.supportsRegexpSearch = supportsRegexpSearch
	CursorManager.getSearchEntries = getSearchEntries


def patchOffsetsTextInfo():
	setattr(textInfos.offsets.OffsetsTextInfo, "findRegexp", findRegexp)


def script_enhancedFind(self, gesture, reverse=False):
	# #8566: We need this to be a modal dialog, but it mustn't block this script.
	def run():
		# get the active profile and send that to the find dialog
		# this is needed because whenever the find dialog is opened the default profile is loaded.
		# We, however, want to retrieve state from the active profile when the find dialog was loaded
		profile = config.conf.getActiveProfile()

		gui.mainFrame.prePopup()
		d = guiHelper.EnhancedFindDialog(gui.mainFrame, self, profile, reverse)
		d.ShowModal()
		gui.mainFrame.postPopup()
	wx.CallAfter(run)


def script_enhancedFindNext(self, gesture):
	mostRecentSearchTerm = getMostRecentSearchTerm()
	if mostRecentSearchTerm is None or (mostRecentSearchTerm.searchType == SearchType.REGULAR_EXPRESSION.name and not self.supportsRegexpSearch()):
		self.script_find(gesture)
		return
	doFindText(
		self,
		mostRecentSearchTerm,
		caseSensitive=self._lastCaseSensitivity,
		searchWrap=self._searchWrap,
		willSayAllResume=willSayAllResume(gesture),
	)


def script_EnhancedFindPrevious(self, gesture):
	mostRecentSearchTerm = getMostRecentSearchTerm()
	if mostRecentSearchTerm is None or (mostRecentSearchTerm.searchType == SearchType.REGULAR_EXPRESSION.name and not self.supportsRegexpSearch()):
		self.script_find(gesture, reverse=True)
		return
	doFindText(
		self,
		mostRecentSearchTerm,
		reverse=True,
		caseSensitive=self._lastCaseSensitivity,
		searchWrap=self._searchWrap,
		willSayAllResume=willSayAllResume(gesture)
	)


def supportsRegexpSearch(self):
	info = self.makeTextInfo(textInfos.POSITION_CARET)
	return isinstance(info, textInfos.offsets.OffsetsTextInfo)


def getSearchEntries(self):
	searchHistory = SearchHistory.get()
	if self.supportsRegexpSearch():
		return searchHistory.getItems()
	return searchHistory.getItems(searchType="normal")


def getMostRecentSearchTerm():
	searchHistory = SearchHistory.get()
	return searchHistory.getMostRecent()


def doFindText(cursorManagerInstance, searchTerm,
               reverse=False, caseSensitive=False, searchWrap=False, willSayAllResume=False):  # noqa: E101
	log.debug("doFindText, reverse=%s, caseSensitive=%s, searchWrap=%s", reverse, caseSensitive, searchWrap)
	if not searchTerm:
		return

	info = cursorManagerInstance.makeTextInfo(textInfos.POSITION_CARET)
	res = performSearch(cursorManagerInstance, searchTerm, info, reverse, caseSensitive, searchWrap)
	if res:
		cursorManagerInstance.selection = info
		speech.cancelSpeech()

		if searchTerm.searchType == SearchType.REGULAR_EXPRESSION.name:
			info.move(textInfos.UNIT_LINE, 1, endPoint="end")
		else:
			info.move(textInfos.UNIT_LINE, 1, endPoint="start")
			info.expand(textInfos.UNIT_LINE)

		if not willSayAllResume:
			speech.speakTextInfo(info, reason=controlTypes.OutputReason.CARET)
	else:
		wx.CallAfter(gui.messageBox, __('text "%s" not found') % searchTerm.text,
		             FIND_ERROR_DIALOG_TITLE, wx.OK | wx.ICON_ERROR)  # Noqa E101
	CursorManager._lastFindText = searchTerm.text
	CursorManager._lastCaseSensitivity = caseSensitive
	CursorManager._searchWrap = searchWrap


def performSearch(cursorManager, searchTerm, info, reverse, caseSensitive, wrapSearch):
	res = find(cursorManager, searchTerm, info, reverse=reverse, caseSensitive=caseSensitive)
	# if either not interested in search wrapping or we have found a result then we are done here
	if not wrapSearch or res:
		return res
	found = False
	while find(cursorManager, searchTerm, info, reverse=(not reverse), caseSensitive=caseSensitive):
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

	if searchTerm.searchType == SearchType.REGULAR_EXPRESSION.name:
		found = re.search(searchTerm.text, inText, re.UNICODE)
	else:
		found = re.search(re.escape(searchTerm.text), inText, (0 if caseSensitive else re.IGNORECASE) | re.UNICODE)

	if found:
		beep(440, 30)
	return found


def find(cursorManager, searchTerm, info, reverse, caseSensitive):
		if searchTerm.searchType == SearchType.REGULAR_EXPRESSION.name:
			if not cursorManager.supportsRegexpSearch():
				wx.CallAfter(
					# Translators: Message shown when an invalid regular expression is entered.
					_("current textInfo backend does not support regular expression searches"),
					FIND_ERROR_DIALOG_TITLE, wx.OK | wx.ICON_ERROR
				)
				return None
			res = info.findRegexp(searchTerm.text, reverse=reverse)
		else:
			res = info.find(searchTerm.text, reverse=reverse, caseSensitive=caseSensitive)
		return res


def findRegexp(self, text, reverse=False):
	if reverse:
		inText = self._getTextRange(0, self._startOffset)
		matches = list(re.finditer(text, inText, re.UNICODE))
		if not matches:
			return False
		m = matches[-1]
	else:
		inText = self._getTextRange(self._startOffset + 1, self._getStoryLength())
		m = re.search(text, inText, re.UNICODE)
	if not m:
		return False

	converter = textUtils.getOffsetConverter(self.encoding)(inText)

	if reverse:
		offset = converter.strToEncodedOffsets(m.start())
	else:
		offset = self._startOffset + 1 + converter.strToEncodedOffsets(m.start())

	self._startOffset = self._endOffset = offset
	return True


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
