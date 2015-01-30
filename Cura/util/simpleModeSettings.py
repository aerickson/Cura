from Cura.util import profile

class SimpleModeSettings(object):
	mini_abs_start_gcode = """;This Gcode has been generated specifically for the LulzBot Mini
;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
;Filament Diameter: {filament_diameter}
;Nozzle Size: {nozzle_size}
G21                          ; metric values
G90                          ; absolute positioning
M82                          ; set extruder to absolute mode
M107                         ; start with the fan off
G92 E0                       ; set extruder position to 0
M140 S110                    ; get bed heating up
G28                          ; home all
M109 S150                    ; set to cleaning temp and wait
G1 Z150 E-30 F75             ; suck up XXmm of filament
M109 S170                    ; heat up rest of way
G1 X45 Y174 F11520           ; move behind scraper
G1 Z0  F1200                 ; CRITICAL: set Z to height of top of scraper
G1 X45 Y174 Z-.5 F4000       ; wiping ; plunge into wipe pad
G1 X55 Y172 Z-.5 F4000       ; wiping
G1 X45 Y174 Z0 F4000         ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X45 Y174 F4000            ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X45 Y174 F4000            ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X80 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X80 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X90 Y172 F4000            ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X115 Y172 Z-0.5 F1000     ; wipe slower and bury noz in cleanish area
G1 Z10                       ; raise z
G28 X0 Y0                    ; home x and y
M109 S170                    ; set to probing temp
M204 S300                    ; set accel for probing
G29                          ; Probe
M204 S2000                   ; set accel back to normal
G1 X5 Y15 Z10 F5000          ; get out the way
M400                         ; clear buffer
G4 S1                        ; pause
M109 S{print_temperature}    ; set extruder temp and wait
G4 S25                       ; wait for bed to temp up
G1 Z2 E0 F75                 ; extrude filament back into nozzle
M140 S{print_bed_temperature}; get bed temping up during first layer
"""

	mini_abs_end_gcode = """
M400
M104 S0                         ; Hotend off
M140 S0                         ; heated bed heater off (if you have it)
M107                            ; fans off
G92 E0                          ; set extruder to 0
G1 E-3 F300                     ; retract a bit to relieve pressure
G1 X5 Y5 Z156 F10000            ; move to cooling positioning
M190 R60                        ; wait for bed to cool
M140 S0                         ; Turn off bed temp
G1 X145 Y175 Z156 F1000         ; move to cooling positioning
M84                             ; steppers off
G90                             ; absolute positioning
;{profile_string}
"""

	mini_pla_start_gcode = """;This Gcode has been generated specifically for the LulzBot Mini
;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
;Filament Diameter: {filament_diameter}
;Nozzle Size: {nozzle_size}
G21                          ; metric values
G90                          ; absolute positioning
M82                          ; set extruder to absolute mode
M107                         ; start with the fan off
G92 E0                       ; set extruder position to 0
M140 S{print_bed_temperature}; get bed heating up
G28                          ; home all
M109 S140                    ; set to cleaning temp and wait
G1 Z150 E-30 F75             ; suck up XXmm of filament
M109 S140                    ; heat up rest of way
G1 X45 Y174 F11520           ; move behind scraper
G1 Z0  F1200                 ; CRITICAL: set Z to height of top of scraper
G1 X45 Y174 Z-.5 F4000       ; wiping ; plunge into wipe pad
G1 X55 Y172 Z-.5 F4000       ; wiping
G1 X45 Y174 Z0 F4000         ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X45 Y174 F4000            ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X45 Y174 F4000            ; wiping
G1 X55 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X80 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X80 Y172 F4000            ; wiping
G1 X60 Y174 F4000            ; wiping
G1 X90 Y172 F4000            ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X80 Y174 F4000            ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X100 Y172 F4000           ; wiping
G1 X110 Y174 F4000           ; wiping
G1 X115 Y172 Z-0.5 F1000     ; wipe slower and bury noz in cleanish area
G1 Z10                       ; raise z
G28 X0 Y0                    ; home x and y
M109 S140                    ; set to probing temp
M204 S300                    ; Set probing acceleration
G29                          ; Probe
M204 S2000                   ; Restore standard acceleration
G1 X5 Y15 Z10 F5000          ; get out the way
G4 S1                        ; pause
M400                         ; clear buffer
M109 S{print_temperature}    ; set extruder temp and wait
G4 S15                       ; wait for bed to temp up
G1 Z2 E0 F75                 ; extrude filament back into nozzle
M140 S{print_bed_temperature}; get bed temping up during first layer
"""

	mini_pla_end_gcode = """
M400
M104 S0                                      ; hotend off
M140 S0                                      ; heated bed heater off (if you have it)
M107                                         ; fans off
G92 E5                                       ; set extruder to 5mm for retract on print end
G1 X5 Y5 Z156 E0 F10000                      ; move to cooling positioning
M190 R50                                     ; wait for bed to cool
M104 S0                                      ;
G1 X145 Y175 Z156 F1000                      ; move to cooling positioning
M84                                          ; steppers off
G90                                          ; absolute positioning
;{profile_string}
"""


	mini_settings = [('filament_diameter', '2.85'),
					 ('nozzle_size', '0.5'),
					 ('wall_thickness', '1'),
					 ('fill_density', '20'),
					 ('retraction_speed', '10'),
					 ('retraction_hop', '0.1'),
					 ('bottom_thickness', '0.425'),
					 ('layer0_width_factor', '125'),
					 ('travel_speed', '175'),
					 ('skirt_minimal_length', '250'),
					 ('brim_line_count', '10'),
					 ('raft_airgap', '0.5'),
					 ('bottom_layer_speed', '15'),
					 ('fan_full_height', '0.5'),
					 ('retraction_minimal_extrusion', '0.005')]

	support_settings = [('support', _("Everywhere")),
						('support_type', 'Lines'),
						('support_angle', '45'),
						('support_fill_rate', '30'),
						('support_xy_distance', '0.7'),
						('support_z_distance', '0.05')]

	brim_settings = [('platform_adhesion', 'Brim')]

	abs_hips_settings = [('print_temperature', '240'),
						 ('print_bed_temperature', '110'),
						 ('solid_layer_thickness', '0.8'),
						 ('retraction_amount', '1'),
						 ('fan_speed', '40'),
						 ('start.gcode', mini_abs_start_gcode),
						 ('end.gcode', mini_abs_end_gcode)]

	hips_settings = [('fan_speed_max', '50')]
	hips_low_settings = [('layer_height', '0.38'),
						 ('print_speed', '50'),
						 ('infill_speed', '70'),
						 ('inset0_speed', '40'),
						 ('insetx_speed', '45'),
						 ('cool_min_layer_time', '15'),
						 ('cool_min_feedrate', '10')]

	hips_normal_settings = [('layer_height', '0.25'),
							('print_speed', '50'),
							('infill_speed', '60'),
							('inset0_speed', '30'),
							('insetx_speed', '35'),
							('cool_min_layer_time', '15'),
							('cool_min_feedrate', '10')]

	hips_high_settings = [('layer_height', '0.18'),
						  ('print_speed', '30'),
						  ('infill_speed', '30'),
						  ('inset0_speed', '20'),
						  ('insetx_speed', '25'),
						  ('cool_min_layer_time', '20'),
						  ('cool_min_feedrate', '5')]

	abs_settings = [('fan_speed_max', '60')]
	abs_low_settings = [('layer_height', '0.38'),
						('print_speed', '85'),
						('infill_speed', '60'),
						('inset0_speed', '50'),
						('insetx_speed', '55'),
						('cool_min_feedrate', '10')]

	abs_normal_settings = [('layer_height', '0.25'),
						   ('print_speed', '50'),
						   ('infill_speed', '55'),
						   ('inset0_speed', '45'),
						   ('insetx_speed', '50'),
						   ('cool_min_feedrate', '10')]

	abs_high_settings = [('layer_height', '0.18'),
						 ('print_speed', '50'),
						 ('infill_speed', '40'),
						 ('inset0_speed', '30'),
						 ('insetx_speed', '35'),
						 ('cool_min_feedrate', '5')]

	pla_settings = [('print_temperature', '205'),
					('print_bed_temperature', '60'),
					('solid_layer_thickness', '1'),
					('print_speed', '50'),
					('retraction_amount', '1.5'),
					('bottom_layer_speed', '15'),
					('cool_min_layer_time', '20'),
					('fan_speed', '75'),
					('fan_speed_max', '100'),
					('start.gcode', mini_pla_start_gcode),
					('end.gcode', mini_pla_end_gcode)]

	pla_low_settings = [('layer_height', '0.38'),
						 ('cool_min_feedrate', '10'),
						 ('infill_speed', '40'),
						 ('inset0_speed', '30'),
						 ('insetx_speed', '35')]
	pla_normal_settings = [('layer_height', '0.25'),
						   ('cool_min_feedrate', '10'),
						   ('infill_speed', '40'),
						   ('inset0_speed', '30'),
						   ('insetx_speed', '35')]
	pla_high_settings = [('layer_height', '0.14'),
						 ('cool_min_feedrate', '5'),
						 ('infill_speed', '30'),
						 ('inset0_speed', '25'),
						 ('insetx_speed', '27')]

	# LulzBot Mini slice settings for use with the simple slice selection.
	lulzbot_mini_settings = [{'Settings': mini_settings},
							 {'Brim': True,
							  'Settings': brim_settings},
							 {'Support': True,
							  'Settings': support_settings},
							 {'MaterialPLA': False,
							  'Settings': abs_hips_settings},
							 {'MaterialHIPS': True,
							  'Settings': hips_settings},
							 {'MaterialHIPS': True, 'TypeLow': True,
							  'Settings': hips_low_settings},
							 {'MaterialHIPS': True, 'TypeNormal': True,
							  'Settings': hips_normal_settings},
							 {'MaterialHIPS': True, 'TypeHigh': True,
							  'Settings': hips_high_settings},
							 {'MaterialABS': True,
							  'Settings': abs_settings},
							 {'MaterialABS': True, 'TypeLow': True,
							  'Settings': abs_low_settings},
							 {'MaterialABS': True, 'TypeNormal': True,
							  'Settings': abs_normal_settings},
							 {'MaterialABS': True, 'TypeHigh': True,
							  'Settings': abs_high_settings},
							 {'MaterialPLA': True,
							  'Settings': pla_settings},
							 {'MaterialPLA': True, 'TypeLow': True,
							  'Settings': pla_low_settings},
							 {'MaterialPLA': True, 'TypeNormal': True,
							  'Settings': pla_normal_settings},
							 {'MaterialPLA': True, 'TypeHigh': True,
							  'Settings': pla_high_settings}]

	# LulzBot TAZ slice settings for use with the simple slice selection.
	lulzbot_taz_settings = []

	@staticmethod
	def nozzle_size_mult(mult):
		return float(profile.getProfileSetting('nozzle_size')) * mult
	others_settings = [{'Settings': [('filament_diameter', '2.85')]},
					   {'Brim': True,
						'Settings': [('platform_adhesion', 'Brim'),
									 ('brim_line_count', '10')]},
					   {'Support': True,
						'Settings': [('support', _("Exterior Only"))]},
					   {'MaterialABS': True,
						'Settings': [('print_bed_temperature', '100'),
									 ('platform_adhesion', 'Brim'),
									 ('filament_flow', '107'),
									 ('print_temperature', '245')]},
					   {'TypeJoris': True,
						'Settings': [('wall_thickness', lambda: SimpleModeSettings.nozzle_size_mult(1.5))]},
					   {'TypeLow': False, 'TypeJoris': False,
						'Settings': [('wall_thickness', lambda: SimpleModeSettings.nozzle_size_mult(2.0))]},
					   {'TypeHigh': True,
						'Settings': [('layer_height', '0.06'),
									 ('fill_density', '20'),
									 ('bottom_layer_speed', '15')]},
					   {'TypeNormal': True,
						'Settings': [('layer_height', '0.10'),
									 ('fill_density', '20')]},
					   {'TypeLow': True,
						'Settings': [('wall_thickness', lambda: SimpleModeSettings.nozzle_size_mult(2.5)),
									 ('layer_height', '0.20'),
									 ('fill_density', '10'),
									 ('print_speed', '60'),
									 ('cool_min_layer_time', '3'),
									 ('bottom_layer_speed', '30')]}]

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
				None: others_settings}


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
			print "Testing setting dict : " + str(setting_dict)
			for option in setting_dict.keys():
				if option == 'Settings':
					settings = setting_dict[option]
				else:
					if not hasattr(simpleMode, "print" + option) or \
					   getattr(simpleMode, "print" + option).GetValue() != setting_dict[option]:
						print "Option %s is wrong, ignoring this setting dict" % (option)
						matches = False
						break
			if matches is False:
				continue
			for item in settings:
				if len(item) != 2:
					continue
				print "Adding " + item[0]
				if hasattr(item[1], '__call__'):
					print "It's callable!"
					simple_settings += [(item[0], item[1]())]
				else:
					simple_settings += [item]

		print "Simple settings are : " + str(simple_settings)
		return simple_settings
