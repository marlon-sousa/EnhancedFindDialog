# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import addonHandler
import core
import gui

from . import cursorManagerHelper
from .configUtils import getConfig, getDefaultConfig, scheduleProfileSave, setConfig, setDefaultConfig, strToBool  # Noqa: E501
from .searchHistory import SearchHistory, SearchTerm
from .searchType import SearchType
from gui import contextHelp, guiHelper
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


# case sensitivity and search wrapping checkboxes state will be persisted per profile
# so we need to be able to get and set values from config


class EnhancedFindDialog(
	contextHelp.ContextHelpMixin,
	wx.Dialog,  # Noqa: E101
):
	"""A dialog used to specify text to find in a cursor manager.
	"""

	helpId = "SearchingForText"

	def __init__(self, parent, cursorManager, profile, reverseSearch):
		# Translators: Title of a dialog to find text.
		super().__init__(parent, title=__("Find"))
		self.searchHistory = SearchHistory.get()
		self.reverseSearch = reverseSearch
		# if checkboxes change during this dialog we need to save the profile with the new values
		self._mustSaveProfile = False
		# Have a copy of the active cursor manager, as this is needed later for finding text.
		self.activeCursorManager = cursorManager
		# have a copy of the profile active when this dialog was called
		# this is needed because whenever the find dialog is opened the default profile is loaded. We, however, want
		# to retrieve state from the active profile when the find dialog was loaded
		self.profile = profile
		self.caseSensitivity = strToBool(getConfig(profile, "searchCaseSensitivity"))
		self.searchWrap = strToBool(getConfig(profile, "searchWrap"))
		self.useSearchHistory = strToBool(getDefaultConfig("useSearchHistory"))
		self.searchType = SearchType.getByName(getConfig(profile, "searchType")).name
		self.buildGui()
		self.updateUi()
		self.bindEvents()

	def buildGui(self):
		log.debug("called buildGui")
		supportsRegexp = self.activeCursorManager.supportsRegexpSearch()
		self.searchEntries = self.searchHistory.getItems(None if supportsRegexp else SearchType.NORMAL.name)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Dialog text for NvDA's find command.
		textToFind = wx.StaticText(self, wx.ID_ANY, label=__("Type the text you wish to find"))
		hSizer.Add(textToFind, flag=wx.ALIGN_CENTER_VERTICAL)
		hSizer.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)
		self.findTextField = wx.ComboBox(self, wx.ID_ANY, style=wx.CB_DROPDOWN)
		if self.searchEntries:
			self.updateFindTextEntries()
		hSizer.Add(self.findTextField)
		sHelper.addItem(hSizer)
		searchTypeHelper = guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
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

		searchHistoryHelper = guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)

		self.useSearchHistoryCheckBox = wx.CheckBox(
			self, wx.ID_ANY,
			# Translators: An option in find dialog to save search history persistently
			label=_("Use search history"))
		self.removeSearchHistoryButton = wx.Button(
			self, wx.ID_ANY,
			# Translators: A button to remove search history.
			label=_("Remove search history"))
		searchHistoryHelper.addItem(self.useSearchHistoryCheckBox)
		searchHistoryHelper.addItem(self.removeSearchHistoryButton)
		sHelper.addItem(searchHistoryHelper)

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
		self.useSearchHistoryCheckBox.SetValue(self.useSearchHistory)
		if not self.activeCursorManager.supportsRegexpSearch():
			self.searchType = SearchType.NORMAL.name
			self._searchTypeCtrl.Enable(False)
		self._searchTypeCtrl.SetSelection(SearchType.getIndexByName(self.searchType))
		if self.searchType == SearchType.NORMAL.name:
			self.caseSensitiveCheckBox.Enable(True)
		else:
			self.caseSensitiveCheckBox.Enable(False)

	def updateFindTextEntries(self):
		log.debug("called updateFindTextEntries")
		searchTerms = [entry.text for entry in self.searchEntries]
		mostRecentSearchTerm = self.searchEntries[SEARCH_HISTORY_MOST_RECENT_INDEX]
		self.searchType = mostRecentSearchTerm.searchType
		self.findTextField.SetItems(searchTerms)
		self.findTextField.Select(SEARCH_HISTORY_MOST_RECENT_INDEX)

	def bindEvents(self):
		log.debug("called bind events")
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		self.caseSensitiveCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		self.searchWrapCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		self._searchTypeCtrl.Bind(wx.EVT_RADIOBOX, self.OnSearchTypeChanged)
		self.findTextField.Bind(wx.EVT_COMBOBOX, self.onSearchTermChanged)
		self.useSearchHistoryCheckBox.Bind(wx.EVT_CHECKBOX, self.onUseSearchHistory)
		self.removeSearchHistoryButton.Bind(wx.EVT_BUTTON, self.onRemoveSearchHistory)

	def OnSearchTypeChanged(self, evt):
		log.debug("called OnSearchTypeChanged")
		self.searchType = SearchType.getByIndex(self._searchTypeCtrl.GetSelection()).name
		self.updateUi()
		self.onStatChange(evt)

	def onSearchTermChanged(self, evt):
		log.debug("called onSearchTermChanged")
		selectedSearchTermindex = self.findTextField.GetSelection()
		mostRecentSearchTerm = self.searchEntries[selectedSearchTermindex]
		self.searchType = mostRecentSearchTerm.searchType
		self.updateUi()
		self.onStatChange(evt)

	def onUseSearchHistory(self, evt):
		log.debug("called onUseSearchHistory")
		if self.useSearchHistoryCheckBox.GetValue():
			log.debug("Use search history checked")
			dlg = wx.MessageDialog(
				None,
				# Translators: Message shown when enabling persistent search history.
				_("Do you want to use your search history?"),
				# Translators: Title for the save search history confirmation dialog.
				_("Confirm Use Search History"),
				wx.OK | wx.CANCEL | wx.ICON_QUESTION
			)
			dlg.SetOKCancelLabels(
				# Translators: Label for the confirm usage button
				_("Confirm usage"),
				# Translators: Label for the deny usage button
				_("Deny usage"))
			result = dlg.ShowModal()
			dlg.Destroy()
			self.useSearchHistory = (result == wx.ID_OK)
			if self.useSearchHistory:
				log.debug("Use search history confirmed")
				# merge with history from disk
				self.searchHistory.mergeWithHistoryFromDisk()
				# truncate the search history to the last 20 entries
				self._truncateSearchHistory(self.searchHistory._terms)
				supportsRegexp = self.activeCursorManager.supportsRegexpSearch()
				self.searchEntries = self.searchHistory.getItems(None if supportsRegexp else SearchType.NORMAL.name)
				if(self.searchEntries):
					self.updateFindTextEntries()
		else:
			self.useSearchHistory = False
		self.useSearchHistoryCheckBox.SetValue(self.useSearchHistory)
		self.useSearchHistoryCheckBox.SetFocus()
		self.onStatChange(evt)

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
					gui.messageBox,
					#  Translators: Message shown when an invalid regular expression is entered.
					_("The entered text is not a valid regular expression."),
					cursorManagerHelper.FIND_ERROR_DIALOG_TITLE, wx.OK | wx.ICON_ERROR
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

	def onRemoveSearchHistory(self, evt):
		if self._confirmSearchHistoryDeletion():
			log.debug("called onRemoveSearchHistory")
			self.searchHistory.removePersistentHistory()
			self.searchHistory.clean()
			self.searchEntries = []
			self.findTextField.SetItems([])
			self.findTextField.SetValue("")
			self.findTextField.SetFocus()
			self.useSearchHistory = False
			self.useSearchHistoryCheckBox.SetValue(self.useSearchHistory)
			self.onStatChange(evt)

	def updateProfile(self):
		log.debug("called updateProfile")
		setConfig(self.profile, "searchType", self.searchType)
		setConfig(self.profile, "searchCaseSensitivity", self.caseSensitiveCheckBox.GetValue())
		setConfig(self.profile, "searchWrap", self.searchWrapCheckBox.GetValue())

		if self._mustSaveProfile:
			scheduleProfileSave(self.profile)

	def onStatChange(self, evt):
		log.debug(f"called onStatChange {self.useSearchHistory}")
		self._mustSaveProfile = True
		setDefaultConfig("useSearchHistory", self.useSearchHistory)

	def _confirmSearchHistoryDeletion(self):
		log.debug("called confirmSearchHistoryDeletion")
		dlg = wx.MessageDialog(
			None,
			# Translators: Message shown when removing search history.
			_("Do you want to remove your search history?"),
			# Translators: Title for the remove search history confirmation dialog.
			_("Confirm Remove Search History"),
			wx.OK | wx.CANCEL | wx.ICON_QUESTION
		)
		dlg.SetOKCancelLabels(
			# Translators: Label for the confirm removal button
			_("Confirm removal"),
			# Translators: Label for the deny removal button
			_("Deny removal"))
		result = dlg.ShowModal()
		dlg.Destroy()
		return result == wx.ID_OK

	def _truncateSearchHistory(self, entries):
		del entries[SEARCH_HISTORY_LEAST_RECENT_INDEX:]
