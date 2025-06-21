# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from logHandler import log
import config
from . import cursorManagerHelper
from .configUtils import getDefaultConfig, initConfiguration, strToBool
from .searchHistory import SearchHistory

import globalPluginHandler
import globalVars

import os
import logging


ADDON_LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "my_addon_shutdown.log")
log.info("addon log file" + ADDON_LOG_FILE)

# Configure a separate logger for your addon's shutdown messages
shutdown_logger = logging.getLogger("my_addon_shutdown")
shutdown_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(ADDON_LOG_FILE, mode='a')  # Use 'w' to overwrite on each NVDA start
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
shutdown_logger.addHandler(file_handler)


def getActiveProfile(self):
	if globalVars.appArgs.secure:
		return
	return self.profiles[-1]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.injectProcessing()

	def terminate(self):
		if strToBool(getDefaultConfig("useSearchHistory")):
			searchHistory = SearchHistory.get()
			searchHistory.persist()
			shutdown_logger.info('Persisted config')
		shutdown_logger.info('turned off')

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
		# add methods to offsetsTextInfo class
		cursorManagerHelper.patchOffsetsTextInfo()
