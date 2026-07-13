# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
import config
import core

from . import cursorManagerHelper
from .searchHistory import SearchHistory, SearchTerm
from .searchType import SearchType
from gui import contextHelp, guiHelper
from gui.message import MessageDialog
import wx

from logHandler import log
import re


# this addon mostly complements NVDA functionalities.
# however, because the way NVDA works, when you use
# addon translation infrastructure by calling addonHandler.initTranslation() you loose access to the
# NVDA translated strings
# It is all or nothing: if you call addonHandler.initTranslation() the _(str) function looks for translations
# only in the addon localization files.
# if you don't, then the _(str) function looks for translations in the NVDA
# localization files, but not in the addon localization files
# In this addon, we add new elements to specific dialogs. Of course
# the translations for these elements are not available in nvda localization files.
# In the other hand, we use lots of strings that are already translated in NVDA
# So now we need to access the nvda localization files to have already defined translations, but we
# also need to access addon translation files to translate custom dialogs
# What we did is we saved the nvda translator to the __ variable
# while _ variable now is used to translate addon strings

__ = _
addonHandler.initTranslation()

# search history list constants
SEARCH_HISTORY_MOST_RECENT_INDEX = 0
SEARCH_HISTORY_LEAST_RECENT_INDEX = 19


# case sensitivity, search wrapping and search type are persisted per profile.
# The dialog sets shouldSuspendConfigProfileTriggers (see the class below), so while it is
# shown the configuration profile that was active in the document stays active. That lets us
# read and write config.conf directly: values target the correct profile, and NVDA marks
# that profile dirty and persists it as usual.

module = "EnhancedFindDialog"


class EnhancedFindDialog(contextHelp.ContextHelpMixin, wx.Dialog):
	"""A dialog used to specify text to find in a cursor manager.
	"""

	helpId = "SearchingForText"

	# Keep the configuration profile that was active in the document active while this
	# dialog is shown, so per-profile settings are read from and saved to that profile.
	# Requires NVDA 2026.1, which suspends profile triggers for any shown top-level window
	# that sets this attribute.
	shouldSuspendConfigProfileTriggers = True

	def __init__(self, parent, cursorManager, reverseSearch):
		# Translators: Title of a dialog to find text.
		super().__init__(parent, title=__("Find"))
		self.searchHistory = SearchHistory.get()
		self.reverseSearch = reverseSearch
		# Have a copy of the active cursor manager, as this is needed later for finding text.
		self.activeCursorManager = cursorManager
		self.caseSensitivity = config.conf[module]["searchCaseSensitivity"]
		self.searchWrap = config.conf[module]["searchWrap"]
		self.searchType = SearchType.getByName(config.conf[module]["searchType"]).name
		self.buildGui()
		self.updateUi()
		self.bindEvents()

	def buildGui(self):
		log.debug("called buildGui")
		supportsRegexp = self.activeCursorManager.supportsRegexpSearch()
		searchEntries = self.searchHistory.getItems(None if supportsRegexp else SearchType.NORMAL.name)
		# if the search type is not supported, remove it from the list of search entries
		searchTerms = [entry.text for entry in searchEntries]
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Dialog text for NvDA's find command.
		textToFind = wx.StaticText(self, wx.ID_ANY, label=__("Type the text you wish to find"))
		hSizer.Add(textToFind, flag=wx.ALIGN_CENTER_VERTICAL)
		hSizer.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)
		self.findTextField = wx.ComboBox(self, wx.ID_ANY, choices=searchTerms, style=wx.CB_DROPDOWN)
		hSizer.Add(self.findTextField)
		sHelper.addItem(hSizer)
		# if there is a previous list of searched entries, make sure we
		# present the last searched term  selected by default
		if searchEntries:
			self.findTextField.Select(SEARCH_HISTORY_MOST_RECENT_INDEX)
		searchTypeHelper = guiHelper.BoxSizerHelper(
			self, orientation=wx.HORIZONTAL)
		self._searchTypeCtrl = searchTypeHelper.addItem(wx.RadioBox(
			self,
			# Translators: A radio box to select the search type.
			label=_("Search type:"), choices=SearchType.getSearchTypes(),
			majorDimension=1, style=wx.RA_SPECIFY_ROWS))
		sHelper.addItem(searchTypeHelper)
		# Translators: An option in find dialog to perform case-sensitive search.
		self.caseSensitiveCheckBox = wx.CheckBox(self, wx.ID_ANY, label=__("Case &sensitive"))
		sHelper.addItem(self.caseSensitiveCheckBox)

		# Translators: An option in find dialog to perform search wrapping
		self.searchWrapCheckBox = wx.CheckBox(self, wx.ID_ANY, label=_("Search &wrap"))
		sHelper.addItem(self.searchWrapCheckBox)

		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))

		mainSizer.Add(sHelper.sizer, border=guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CentreOnScreen()
		self.findTextField.SetFocus()

	def updateUi(self):
		log.debug("called update ui")
		self.caseSensitiveCheckBox.SetValue(self.caseSensitivity)
		self.searchWrapCheckBox.SetValue(self.searchWrap)
		if not self.activeCursorManager.supportsRegexpSearch():
			self.searchType = SearchType.NORMAL.name
			self._searchTypeCtrl.Enable(False)
		self._searchTypeCtrl.SetSelection(SearchType.getIndexByName(self.searchType))
		if (self.searchType == SearchType.NORMAL.name):
			self.caseSensitiveCheckBox.Enable(True)
		else:
			self.caseSensitiveCheckBox.Enable(False)

	def bindEvents(self):
		log.debug("called bind events")
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		self._searchTypeCtrl.Bind(wx.EVT_RADIOBOX, self.OnSearchTypeChanged)

	def OnSearchTypeChanged(self, evt):
		log.debug("called OnSearchTypeChanged")
		self.searchType = SearchType.getByIndex(self._searchTypeCtrl.GetSelection()).name
		self.updateUi()

	def updateSearchHistory(self, currentSearchText):
		if not currentSearchText:
			return None
		searchTerm = SearchTerm(currentSearchText, self.searchType)
		self.searchHistory.append(searchTerm)
		return searchTerm

	def onOk(self, evt):
		log.debug("called onOk")
		text = self.findTextField.GetValue()
		if self.searchType == SearchType.REGULAR_EXPRESSION.name:
			try:
				re.compile(text)
			except re.error:
				wx.CallAfter(
					MessageDialog.alert,
					# Translators: Message shown when an invalid regular expression is entered.
					_("The entered text is not a valid regular expression."),
					cursorManagerHelper.FIND_ERROR_DIALOG_TITLE
				)  # Noqa E101
				return

		self.caseSensitive = self.caseSensitiveCheckBox.GetValue()

		self.searchWrap = self.searchWrapCheckBox.GetValue()

		self.searchType = SearchType.getByIndex(self._searchTypeCtrl.GetSelection()).name

		# update the list of searched entries so that it can be exibited in the next find dialog call
		searchTerm = self.updateSearchHistory(text)

		self.updateProfile()

		# We must use core.callLater rather than wx.CallLater to
		# ensure that the callback runs within NVDA's core pump.
		# If it didn't, and it directly or indirectly called wx.Yield, it
		# could start executing NVDA's core pump from within the yield, causing recursion.
		core.callLater(
			100, cursorManagerHelper.doFindText, self.activeCursorManager, searchTerm,
			caseSensitive=self.caseSensitive, searchWrap=self.searchWrap,
			reverse=self.reverseSearch)  # Noqa: E101
		self.Destroy()

	def onCancel(self, evt):
		log.debug("called onCancel")
		self.Destroy()

	def updateProfile(self):
		log.debug("called updateProfile")
		config.conf[module]["searchType"] = self.searchType
		config.conf[module]["searchCaseSensitivity"] = self.caseSensitiveCheckBox.GetValue()
		config.conf[module]["searchWrap"] = self.searchWrapCheckBox.GetValue()

	def _truncateSearchHistory(self, entries):
		del entries[SEARCH_HISTORY_LEAST_RECENT_INDEX:]
