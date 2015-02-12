taz4_start_gcode = """;This Gcode has been generated specifically for the LulzBot TAZ 4
;Sliced at: {day} {date} {time}
;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
;Filament Diameter: {filament_diameter}
;Print time: {print_time}
;M190 S{print_bed_temperature} ;Uncomment to add your own bed temperature line
;M109 S{print_temperature} ;Uncomment to add your own temperature line
G21        ;metric values
G90        ;absolute positioning
M82        ;set extruder to absolute mode
M107       ;start with the fan off
G28 X0 Y0  ;move X/Y to min endstops
G28 Z0     ;move Z to min endstops
G1 Z15.0 F{travel_speed} ;move the platform down 15mm
G92 E0                  ;zero the extruded length
G1 F200 E0              ;extrude 3mm of feed stock
G92 E0                  ;zero the extruded length again
G1 F{travel_speed}
M203 X192 Y208 Z3 ;speed limits
"""

taz4_end_gcode = """M400
M104 S0                                        ; Hotend off
M140 S0                                        ;heated bed heater off (if you have it)
M107                                             ; fans off
G91                                                ;relative positioning
G1 E-1 F300                                  ;retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F3000    ;move Z up a bit and retract filament even more
M84                                                 ;steppers off
G90                                                 ;absolute positioning
;{profile_string}
"""


taz4_settings = [('filament_diameter', '2.85'),
				 ('nozzle_size', '0.35'),
				 ('wall_thickness', '1.05'),
				 ('solid_layer_thickness', '0.84'),
				 ('retraction_amount', '1.5'),
				 ('layer0_width_factor', '125'),
				 ('print_temperature', '0'),
				 ('print_bed_temperature', '0'),
				 ('bottom_layer_speed', '30'),
				 ('travel_speed', '175'),
				 ('cool_min_layer_time', '15'),
				 ('retraction_speed', '25'),
				 ('start.gcode', taz4_start_gcode),
				 ('end.gcode', taz4_end_gcode)]

support_settings = [('support', _("Everywhere")),
					('support_type', 'Lines'),
					('support_angle', '45'),
					('support_fill_rate', '30'),
					('support_xy_distance', '0.7'),
					('support_z_distance', '0.05')]

brim_settings = [('platform_adhesion', 'Brim')]

hips_low_settings = [('layer_height', '0.28'),
					 ('print_speed', '120'),
					 ('retraction_hop', '0.1'),
					 ('inset0_speed', '80'),
					 ('insetx_speed', '100'),
					 ('fan_full_height', '1'),
					 ('fan_speed', '25'),
					 ('fan_speed_max', '30')]
hips_normal_settings = [('layer_height', '0.21'),
						('print_speed', '100'),
						('inset0_speed', '60'),
						('insetx_speed', '80'),
						('skirt_minimal_length', '250'),
						('fan_full_height', '0.35'),
						('fan_speed', '50'),
						('fan_speed_max', '50')]
hips_high_settings = [('layer_height', '0.14'),
					  ('print_speed', '60'),
					  ('inset0_speed', '40'),
					  ('insetx_speed', '50'),
					  ('fan_full_height', '0.56'),
					  ('fan_speed', '50'),
					  ('fan_speed_max', '60'),
					  ('cool_min_feedrate', '8')]

abs_low_settings = [('layer_height', '0.28'),
					('print_speed', '120'),
					('retraction_hop', '0.1'),
					('inset0_speed', '80'),
					('insetx_speed', '100'),
					('fan_full_height', '5'),
					('fan_speed', '25'),
					('fan_speed_max', '30')]
abs_normal_settings = [('layer_height', '0.21'),
					   ('print_speed', '100'),
					   ('inset0_speed', '60'),
					   ('insetx_speed', '80'),
					   ('fan_speed', '25'),
					   ('fan_speed_max', '25'),
					   ('fill_overlap', '5')]
abs_high_settings = [('layer_height', '0.14'),
					 ('print_speed', '60'),
					 ('retraction_hop', '0.1'),
					 ('inset0_speed', '40'),
					 ('insetx_speed', '50'),
					 ('fan_full_height', '5'),
					 ('fan_speed', '40'),
					 ('fan_speed_max', '75')]


pla_low_settings = [('layer_height', '0.28'),
					('print_speed', '120'),
					('retraction_hop', '0.1'),
					('inset0_speed', '80'),
					('insetx_speed', '100'),
					('skirt_minimal_length', '250'),
					('fan_full_height', '1'),
					('fan_speed', '75'),
					('cool_min_feedrate', '15'),
					('fill_overlap', '0')]
pla_normal_settings = [('layer_height', '0.21'),
					   ('print_speed', '100'),
					   ('retraction_hop', '0.1'),
					   ('inset0_speed', '60'),
					   ('insetx_speed', '80'),
					   ('skirt_minimal_length', '250'),
					   ('fan_full_height', '1'),
					   ('fan_speed', '75'),
					   ('cool_min_feedrate', '15')]
pla_high_settings = [('layer_height', '0.14'),
					 ('print_speed', '60'),
					 ('inset0_speed', '40'),
					 ('insetx_speed', '50'),
					 ('skirt_minimal_length', '0'),
					 ('fan_full_height', '0.28'),
					 ('fill_overlap', '10')]

# LulzBot TAZ 4 slice settings for use with the simple slice selection.
lulzbot_taz_settings = [{'Settings': taz4_settings},
						 {'Brim': True,
						  'Settings': brim_settings},
						 {'Support': True,
						  'Settings': support_settings},

						 {'MaterialHIPS': True, 'TypeLow': True,
						  'Settings': hips_low_settings},
						 {'MaterialHIPS': True, 'TypeNormal': True,
						  'Settings': hips_normal_settings},
						 {'MaterialHIPS': True, 'TypeHigh': True,
						  'Settings': hips_high_settings},

						 {'MaterialABS': True, 'TypeLow': True,
						  'Settings': abs_low_settings},
						 {'MaterialABS': True, 'TypeNormal': True,
						  'Settings': abs_normal_settings},
						 {'MaterialABS': True, 'TypeHigh': True,
						  'Settings': abs_high_settings},

						 {'MaterialPLA': True, 'TypeLow': True,
						  'Settings': pla_low_settings},
						 {'MaterialPLA': True, 'TypeNormal': True,
						  'Settings': pla_normal_settings},
						 {'MaterialPLA': True, 'TypeHigh': True,
						  'Settings': pla_high_settings}]
