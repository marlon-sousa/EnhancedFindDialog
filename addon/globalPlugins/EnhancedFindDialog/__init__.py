# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import config
from . import cursorManagerHelper

import globalPluginHandler
import globalVars


module = "EnhancedFindDialog"


def initConfiguration():
	confspec = {
		"searchCaseSensitivity": "boolean( default=False)",
		"searchWrap": "boolean( default=False)",
		"searchType": "string( default='NORMAL')",
	}
	config.conf.spec[module] = confspec


def getActiveProfile(self):
	if globalVars.appArgs.secure:
		return
	return self.profiles[-1]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.injectProcessing()

	# the method below is responsible for modifying NVDA behavior.
	# we need that certain parts of NVDA behave differently than the original to insert our functionality
	# for example, when calling the find dialog we need to show the enhanced version provided by this addon
	# the CursorManager mixin also needs to have functionality added
	def injectProcessing(self):
		# Don't inject on secure screens as the addon can write to configuration
		if globalVars.appArgs.secure:
			return

		# add utility method to ConfigManager class to allow us to get the active profile in a higher level
		if not hasattr(config.ConfigManager, "getActiveProfile"):
			config.ConfigManager.getActiveProfile = getActiveProfile

		initConfiguration()

		# add methods to CursorManager class
		cursorManagerHelper.patchCursorManager()
