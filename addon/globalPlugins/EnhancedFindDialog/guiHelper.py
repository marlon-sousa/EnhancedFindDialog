# -*- coding: UTF-8 -*-
#A part of the EnhancedFind addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import addonHandler
import config
import core
import cursorManager
from gui import contextHelp
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
	if not module in profile or not key in profile[module]:
		return getDefaultConfig(key)
	return profile[module][key]


def setConfig(profile, key, value):
	if not module in profile:
		profile[module] = {}
	profile[module][key] = value


class EnhancedFindDialog(
	contextHelp.ContextHelpMixin,
	wx.Dialog
):
	"""A dialog used to specify text to find in a cursor manager.
	"""

	helpId = "SearchingForText"

	def __init__(self, parent, cursorManager, profile, searchEntries):
		# Translators: Title of a dialog to find text.
		super().__init__(parent, title=__("Find"))
		# if checkboxes change during this dialog we need to save the profile with the new values
		self._mustSaveProfile = False
		# Have a copy of the active cursor manager, as this is needed later for finding text.
		self.activeCursorManager = cursorManager
		# have a copy of the profile active when this dialog was called
		# this is needed because whenever the find dialog is opened the default probile is loaded. We, however, want to retrieve state from the active profile when the find dialog was loaded
		self.profile = profile
		caseSensitivity = strToBool(getConfig(profile, "searchCaseSensitivity"))
		searchWrap = strToBool(getConfig(profile, "searchWrap"))

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
		self.caseSensitiveCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		mainSizer.Add(self.caseSensitiveCheckBox,border=10,flag=wx.BOTTOM)
		# Translators: An option in find dialog to perform search wrapping
		self.searchWrapCheckBox=wx.CheckBox(self,wx.ID_ANY,label=_("Search &wrap"))
		self.searchWrapCheckBox.SetValue(searchWrap)
		self.searchWrapCheckBox.Bind(wx.EVT_CHECKBOX, self.onStatChange)
		mainSizer.Add(self.searchWrapCheckBox,border=10,flag=wx.BOTTOM)

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
		setConfig(self.profile, "searchCaseSensitivity", caseSensitive)

		searchWrap = self.searchWrapCheckBox.GetValue()
		setConfig(self.profile, "searchWrap", searchWrap)

		if self._mustSaveProfile:
			scheduleProfileSave(self.profile)

		# We must use core.callLater rather than wx.CallLater to ensure that the callback runs within NVDA's core pump.
		# If it didn't, and it directly or indirectly called wx.Yield, it could start executing NVDA's core pump from within the yield, causing recursion.
		core.callLater(100, self.activeCursorManager.doFindText, text, caseSensitive=caseSensitive, searchWrap = searchWrap)
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

	def onStatChange(self, evt):
		self._mustSaveProfile = True

	def _truncateSearchHistory(self, entries):
		del entries[SEARCH_HISTORY_LEAST_RECENT_INDEX:]

