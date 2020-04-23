# -*- coding: UTF-8 -*-
#A part of the EnhancedFind addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import config
import core
import cursorManager
from logHandler import log
import wx

# this addon mostly complements NVDA functionalities.
# however, because the way NVDA works, when you use
# addon translation infrastructure by calling addonHandler.initTranslation() you loose access to the
# NVDA translated strings
# It is all or nothing: if you call addonHandler.initTranslation() the _(str) function looks for translations only in the addon localization files.
# if you don't, then the _(str) function looks for translations in the NVDA localization files, but not in the addon localization files
# In this addon, we add new elements to specific dialogs. Of course the translations for these elements are not available in nvda localization files.
# In the other hand, we use lots of strings that are already translated in NVDA
# So now we need to access the nvda localization files to have already defined translations, but we also need to access addon translation files to translate custom dialogs
# What we did is we saved the nvda translator to the __ variable while _ variable now is used to translate addon strings

# search history list constants
SEARCH_HISTORY_MOST_RECENT_INDEX = 0
SEARCH_HISTORY_LEAST_RECENT_INDEX = 19

__ = _


class EnhancedFindDialog(wx.Dialog):
	"""A dialog used to specify text to find in a cursor manager.
	"""

	def __init__(self, parent, cursorManager, caseSensitivity, searchEntries):
		# Translators: Title of a dialog to find text.
		super(EnhancedFindDialog, self).__init__(parent, wx.ID_ANY, __("Find"))
		# Have a copy of the active cursor manager, as this is needed later for finding text.
		self.activeCursorManager = cursorManager
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		findSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Dialog text for NvDA's find command.
		textToFind = wx.StaticText(self, wx.ID_ANY, label=__("Type the text you wish to find"))
		findSizer.Add(textToFind)
		self.findTextField = wx.ComboBox(self, wx.ID_ANY, choices = searchEntries,style=wx.CB_DROPDOWN)

		# if there is a previous list of searched entries, make sure we present the last searched term  selected by default
		if searchEntries:
			self.findTextField.Select(SEARCH_HISTORY_MOST_RECENT_INDEX)
		findSizer.Add(self.findTextField)
		mainSizer.Add(findSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)
		# Translators: An option in find dialog to perform case-sensitive search.
		self.caseSensitiveCheckBox=wx.CheckBox(self,wx.ID_ANY,label=__("Case &sensitive"))
		self.caseSensitiveCheckBox.SetValue(caseSensitivity)
		mainSizer.Add(self.caseSensitiveCheckBox,border=10,flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK|wx.CANCEL), flag=wx.ALIGN_RIGHT)
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)

		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CentreOnScreen()
		self.findTextField.SetFocus()

	def updateSearchEntries(self, searchEntries, currentSearchTerm):
		if not currentSearchTerm:
			return
		if not searchEntries:
			searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)
			return
		# we can not accept entries that differ only on text case
		#because of a wxComboBox limitation on MS Windows
		# see https://wxpython.org/Phoenix/docs/html/wx.ComboBox.html
		#notice also that python 2 does not offer caseFold functionality
		# so lower is the best we can have for comparing strings
		for index, item in enumerate(searchEntries):
			if(item.lower() == currentSearchTerm.lower()):
				# if the user has selected a previous search term in the list or retyped an already listed term , we need to make sure the 
				# current search term becomes the first item of the list, so that it will appear selected by default when the dialog is
				# shown again. If the current search term differs from the current item only in case letters, we will choose to store the
				# new search as we can not store both.
				searchEntries.pop(index)
				searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)
				return
		# not yet listed. Save it.
		if len(searchEntries) > SEARCH_HISTORY_LEAST_RECENT_INDEX:
			self._truncateSearchHistory(searchEntries)
		searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)
		
	def onOk(self, evt):
		text = self.findTextField.GetValue()
		# update the list of searched entries so that it can be exibited in the next find dialog call
		self.updateSearchEntries(self.activeCursorManager._searchEntries, text)
		
		caseSensitive = self.caseSensitiveCheckBox.GetValue()
		# We must use core.callLater rather than wx.CallLater to ensure that the callback runs within NVDA's core pump.
		# If it didn't, and it directly or indirectly called wx.Yield, it could start executing NVDA's core pump from within the yield, causing recursion.
		core.callLater(100, self.activeCursorManager.doFindText, text, caseSensitive=caseSensitive)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

	def _truncateSearchHistory(self, entries):
		del entries[SEARCH_HISTORY_LEAST_RECENT_INDEX:]

