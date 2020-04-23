# -*- coding: UTF-8 -*-
#A part of the EnhancedFind addon for NVDA
#Copyright (C) 2020 Marlon Sousa
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from . import cursorManagerHelper
from . import guiHelper
import globalPluginHandler
from logHandler import log


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		log.debug("constructor called fo enhanced find")
		self.injectProcessing()
	
	# the method below is responsible for modifying NVDA behavior.
	# we need that certain parts of NVDA behave differently than the original to insert our functionality
	# for example, when calling the find dialog we need to show the enhanced version provided by this addon
	# the CursorManager mixin also needs to have functionality added
	def injectProcessing(self):
		# add methods to SpeechDict class
		cursorManagerHelper.patchCursorManager()

