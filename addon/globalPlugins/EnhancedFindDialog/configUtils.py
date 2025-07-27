import config


module = "EnhancedFindDialog"


def initConfiguration():
	confspec = {
		"searchCaseSensitivity": "boolean( default=False)",
		"searchWrap": "boolean( default=False)",
		"searchType": "string( default='NORMAL')",
		"useSearchHistory": "boolean( default=False)",
	}
	config.conf.spec[module] = confspec


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
	defaultProfile = config.conf.profiles[0]
	try:
		value = defaultProfile[module][key]
	except KeyError:
		# Not set in base profile, get default from spec
		spec = config.conf.spec[module][key]
		value = config.conf.validator.get_default_value(spec)
	return value


def getConfig(profile, key):
	# if this is not set on current profile, use the default config values.
	if module not in profile or key not in profile[module]:
		return getDefaultConfig(key)
	return profile[module][key]


def setConfig(profile, key, value):
	if module not in profile:
		profile[module] = {}
	profile[module][key] = value


def setDefaultConfig(key, value):
	defaultProfile = config.conf.profiles[0]
	if module not in defaultProfile:
		defaultProfile[module] = {}
	defaultProfile[module][key] = value
