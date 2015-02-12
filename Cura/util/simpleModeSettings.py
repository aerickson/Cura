from Cura.util import profile
from Cura.util.settings import lulzbot_mini_settings, \
		lulzbot_taz_settings, \
		lulzbot_taz5_settings, \
		default_settings

class SimpleModeSettings(object):
	# Set the Quickprint settings:
	#
	# Settings Format : Dictionary[machine_type] = machine_settings
	#					Dictionary[None] = other_machine_settings
	#
	# Machine settings Format : List of setting dictionaries
	# Setting dictionary Format: Dictionary[Option] = Value
	#							 Dictionary['Settings'] = Option settings
	# Option settings format : List of tuples ('profile setting', 'value')
	#										  ('profile setting', callable function)
	#
	# All the settings in the list of machine settings will be checked. For
	# each of those settings, the list of options will be verified and only the
	# settings in which all the options match will be applied.
	# The 'Settings' key in the dictionary will contain the settings to apply.
	# Those settings will be a a list a tuples of key:value in which the value
	# can be a callable function for greater control
	#
	# For example, a Dictionary with only 'Settings' will always be applied
	# while a setting with {'Brim':True} will only be applied if the printBrim
	# option is enabled, and settings with {'MaterialABS':True, 'TypeHigh':False}
	# will only be applied for Low and Normal quality prints in ABS

	settings = {"lulzbot_mini": lulzbot_mini_settings,
				"lulzbot_TAZ": lulzbot_taz_settings,
				"lulzbot_TAZ_4": lulzbot_taz_settings,
				"lulzbot_TAZ_5": lulzbot_taz5_settings,
				None: default_settings}


	@staticmethod
	def getSimpleSettings(simpleMode):
		simple_settings = []
		if SimpleModeSettings.settings.has_key(profile.getMachineSetting('machine_type')):
			machine_settings = SimpleModeSettings.settings[profile.getMachineSetting('machine_type')]
		else:
			machine_settings = SimpleModeSettings.settings[None]

		for setting_dict in machine_settings:
			matches = True
			settings = []
			for option in setting_dict.keys():
				if option == 'Settings':
					settings = setting_dict[option]
				else:
					if not hasattr(simpleMode, "print" + option) or \
					   getattr(simpleMode, "print" + option).GetValue() != setting_dict[option]:
						matches = False
						break
			if matches is False:
				continue
			for item in settings:
				if len(item) != 2:
					continue
				if hasattr(item[1], '__call__'):
					simple_settings += [(item[0], item[1]())]
				else:
					simple_settings += [item]

		return simple_settings
