# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from enum import Enum, unique
import addonHandler
import config
import core

from . import cursorManagerHelper
from gui import contextHelp, guiHelper
import wx

from logHandler import log


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

module = "EnhancedFindDialog"


def strToBool(value):
	if not isinstance(value, str):
		return value
	return value == "True"


# we need to mark profiles we updated for save, otherwise they will not be persisted
def scheduleProfileSave(profile):
	# default pprofile is always saved
	if not profile.name:
		return
	config.conf._dirtyProfiles.add(profile.name)


# get config from default profile
def getDefaultConfig(key):
	return config.conf[module][key]


def getConfig(profile, key):
	# if this is not set on current profile, use the default config values.
	if module not in profile or key not in profile[module]:
		return getDefaultConfig(key)
	return profile[module][key]


def setConfig(profile, key, value):
	if module not in profile:
		profile[module] = {}
	profile[module][key] = value


class InvalidTypeName(Exception):
	pass


@unique
class SearchType(Enum):
	# Translators: normal
	NORMAL = _("normal")
	# Translators: regular expression
	REGULAR_EXPRESSION = _("regular expression")

	@staticmethod
	def getByIndex(index):
		return list(SearchType)[index]

	@staticmethod
	def getIndexByName(name):
		log.debug(f"searching for {name}")
		for index, type in enumerate(SearchType):
			if type.name == name:
				return index
		raise InvalidTypeName(f"No variant with name '{name}' found in SearchType Enum")

	@staticmethod
	def getByName(name):
		for type in SearchType:
			if type.name == name:
				return type
		raise InvalidTypeName(f"No variant with name '{name}' found in SearchType Enum")


def getSearchTypes():
	return [i.value for i in SearchType]


class EnhancedFindDialog(contextHelp.ContextHelpMixin,
                         wx.Dialog):  # Noqa: E101
	"""A dialog used to specify text to find in a cursor manager.
	"""

	helpId = "SearchingForText"

	def __init__(self, parent, cursorManager, profile, searchEntries, reverseSearch):
		# Translators: Title of a dialog to find text.
		super().__init__(parent, title=__("Find"))
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
		self.searchType = SearchType.getByName(getConfig(profile, "searchType")).name
		self.buildGui(searchEntries)
		self.updateUi()
		self.bindEvents()

	def buildGui(self, searchEntries):
		log.debug("called buildGui")
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sHelper = guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Dialog text for NvDA's find command.
		textToFind = wx.StaticText(self, wx.ID_ANY, label=__("Type the text you wish to find"))
		hSizer.Add(textToFind, flag=wx.ALIGN_CENTER_VERTICAL)
		hSizer.AddSpacer(guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)
		self.findTextField = wx.ComboBox(self, wx.ID_ANY, choices=searchEntries, style=wx.CB_DROPDOWN)
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
			label=_("Search type:"), choices=getSearchTypes(),
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
		self._searchTypeCtrl.SetSelection(SearchType.getIndexByName(self.searchType))
		if(self.searchType == SearchType.NORMAL.name):
			self.caseSensitiveCheckBox.Enable(True)
		else:
			self.caseSensitiveCheckBox.Enable(False)

	def bindEvents(self):
		log.debug("called bind events")
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		self.caseSensitiveCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		self.searchWrapCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		self._searchTypeCtrl.Bind(wx.EVT_RADIOBOX, self.OnSearchTypeChanged)
		self._searchTypeCtrl.Bind(wx.EVT_CHECKBOX, self.onStatChange)

	def OnSearchTypeChanged(self, evt):
		log.debug("called OnSearchTypeChanged")
		self.searchType = SearchType.getByIndex(self._searchTypeCtrl.GetSelection()).name
		self.updateUi()
		self.onStatChange(evt)

	def updateSearchEntries(self, searchEntries, currentSearchTerm):
		if not currentSearchTerm:
			return
		if not searchEntries:
			searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)
			return
		# we can not accept entries that differ only on text case
		# because of a wxComboBox limitation on MS Windows
		# see https://wxpython.org/Phoenix/docs/html/wx.ComboBox.html
		# notice also that python 2 does not offer caseFold functionality
		# so lower is the best we can have for comparing strings
		for index, item in enumerate(searchEntries):
			if(item.lower() == currentSearchTerm.lower()):
				# if the user has selected a previous search term in the list or retyped
				# an already listed term ,we need to make sure the
				# current search term becomes the first item of the list, so that it
				# will appear
				# selected by default when the dialog is
				# shown again. If the current search term
				# differs from the current item only in case letters, we will choose to store the
				# new search as we can not store both.
				searchEntries.pop(index)
				searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)
				return
		# not yet listed. Save it.
		if len(searchEntries) > SEARCH_HISTORY_LEAST_RECENT_INDEX:
			self._truncateSearchHistory(searchEntries)
		searchEntries.insert(SEARCH_HISTORY_MOST_RECENT_INDEX, currentSearchTerm)

	def onOk(self, evt):
		log.debug("called onOk")
		text = self.findTextField.GetValue()
		# update the list of searched entries so that it can be exibited in the next find dialog call
		self.updateSearchEntries(self.activeCursorManager._searchEntries, text)

		self.caseSensitive = self.caseSensitiveCheckBox.GetValue()

		self.searchWrap = self.searchWrapCheckBox.GetValue()

		self.searchType = SearchType.getByIndex(self._searchTypeCtrl.GetSelection()).name

		self.updateProfile()

		# We must use core.callLater rather than wx.CallLater to
		# ensure that the callback runs within NVDA's core pump.
		# If it didn't, and it directly or indirectly called wx.Yield, it
		# could start executing NVDA's core pump from within the yield, causing recursion.
		core.callLater(
			100, cursorManagerHelper.doFindText, self.activeCursorManager, text,
			caseSensitive=self.caseSensitive, searchWrap=self.searchWrap,
			reverse=self.reverseSearch)  # Noqa: E101
		self.Destroy()

	def onCancel(self, evt):
		log.debug("called onCancel")
		self.Destroy()

	def updateProfile(self):
		log.debug("called updateProfile")
		setConfig(self.profile, "searchType", self.searchType)
		setConfig(self.profile, "searchCaseSensitivity", self.caseSensitiveCheckBox.GetValue())
		setConfig(self.profile, "searchWrap", self.searchWrapCheckBox.GetValue())

		if self._mustSaveProfile:
			scheduleProfileSave(self.profile)

	def onStatChange(self, evt):
		log.debug("called onStatChange")
		self._mustSaveProfile = True

	def _truncateSearchHistory(self, entries):
		del entries[SEARCH_HISTORY_LEAST_RECENT_INDEX:]
