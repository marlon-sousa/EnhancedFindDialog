# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _


addon_info = AddonInfo(
    addon_name="EnhancedFindDialog",
    # Translators: Summary/title for this add-on.
    addon_summary=_("Enhanced find dialog for NVDA"),
    # Translators: Long description for this add-on in add-on store.
    addon_description=_("""This addon introduces improvements to the NVDA find dialog.
It is now possible to have your previous searches history available on a list during the NVDA session, which will enable you to quickly select and search for previous searched terms."""),
    # Translators: what's new text for this add-on version shown in add-on store.
    addon_changelog=_("""NVDA 2026.1 compatibility. Minimum supported NVDA version is now 2026.1."""),
    addon_version="1.9.0",
    addon_author="Marlon Brandão de Sousa <marlon.bsousa@gmail.com>, Thiago Seus <thiago.seus@yahoo.com.br>",
    addon_url="https://github.com/marlon-sousa/EnhancedFindDialog",
    addon_sourceURL="https://github.com/marlon-sousa/EnhancedFindDialog",
    addon_docFileName="readme.html",
    addon_minimumNVDAVersion="2026.1",
    addon_lastTestedNVDAVersion="2026.1.0",
    addon_updateChannel=None,
    addon_license="MIT License",
    addon_licenseURL="https://github.com/marlon-sousa/EnhancedFindDialog/blob/master/LICENSE",
)


pythonSources: list[str] = ["addon/globalPlugins/EnhancedFindDialog/*.py"]
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Paths are relative to the addon directory when building the bundle.
excludedFiles: list[str] = [
    "doc/*/contributing*.*",
    "doc/*/*.tpl.md",
]

baseLanguage: str = "en"
markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}
symbolDictionaries: SymbolDictionaries = {}
