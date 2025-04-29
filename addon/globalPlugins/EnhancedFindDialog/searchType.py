# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from enum import Enum, unique
import addonHandler


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

	@staticmethod
	def getSearchTypes():
		return [i.value for i in SearchType]
