# -*- coding: UTF-8 -*-
# A part of the EnhancedFind addon for NVDA
# Copyright (C) 2020 Marlon Sousa
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.


from .configUtils import getDefaultConfig, strToBool
import addonHandler
from logHandler import log
import pickle
import time
import os


class SearchHistory:
	_instance = None

	@classmethod
	def get(cls):
		if cls._instance is None:
			cls._instance = cls()
		return cls._instance

	def __init__(self):
		if strToBool(getDefaultConfig("useSearchHistory")):
			self._loadFromDisk()
			return
		self._terms = []

	def _loadFromDisk(self):
		# Load the pickle file from the addon directory
		addonPath = addonHandler.getCodeAddon().path
		filePath = os.path.join(addonPath, "search_history.pkl")
		if os.path.exists(filePath):
			with open(filePath, "rb") as f:
				data = pickle.load(f)
				if data.get("version") == "1.0":
					self._terms = data.get("terms", [])
				else:
					log.error(f"Unsupported search history version: {data.get('version')}")
					self._terms = []
		else:
			log.info("No search history file found, starting with an empty history.")
			self._terms = []

	def persist(self):
		data = {
			"version": "1.0",
			"timestamp": time.time(),
			"terms": self._terms,
		}
		# Save the pickle file in the addon directory
		addonPath = addonHandler.getCodeAddon().path
		filePath = os.path.join(addonPath, "search_history.pkl")
		with open(filePath, "wb") as f:
			pickle.dump(data, f)

	def getMostRecent(self):
		return self._terms[0] if self._terms else None

	def getItems(self, searchType=None):
		log.debug(dir(self))
		if searchType is None:
			return self._terms
		return list(filter(lambda t: t.searchType == searchType, self._terms))

	def getItemByText(self, text):
		return next((term for term in self._terms if term.text == text), None)

	def append(self, term):
		if not term.text:
			return
		if term in self._terms:
			self._terms.remove(term)
		self._terms.insert(0, term)
		if len(self._terms) > 20:
			self._terms.pop()


class SearchTerm:
	def __init__(self, text, searchType):
		self.text = text
		self.searchType = searchType

	def __eq__(self, other):
		# we can not accept entries that differ only on text case
		# because of a wxComboBox limitation on MS Windows
		# see https://wxpython.org/Phoenix/docs/html/wx.ComboBox.html
		return self.text.casefold() == other.text.casefold()
