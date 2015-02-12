
taz5_start_gcode = """;Sliced at: {day} {date} {time} for use with the LulzBot TAZ 5
;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
G21                     ;metric values
G90                     ;absolute positioning
M82                     ;set extruder to absolute mode
M107                    ;start with the fan off
G28 X0 Y0               ;move X/Y to min endstops
G28 Z0                  ;move Z to min endstops
G1 Z15.0 F{travel_speed};move the platform down 15mm
G92 E0                  ; zero the extruded length
G1 F200 E0              ; extrude 3mm of feed stock
G92 E0                  ; zero the extruded length again
G1 F{travel_speed}      ; set travel speed
M203 X192 Y208 Z3       ; speed limits
M117 Printing...        ; send message to LCD"""

taz5_end_gcode = """M400                           ; wait for buffer to clear
M104 S0                        ; hotend off
M140 S0                        ; heated bed heater off (if you have it)
M107                           ; fans off
G91                            ; relative positioning
G1 E-1 F300                    ; retract the filament a bit before lifting the nozzle, to release some of the pressure
G1 Z+0.5 E-5 X-20 Y-20 F3000   ; move Z up a bit and retract filament even more
G90                            ; absolute positioning
G1 X0 Y250                     ; move to cooling position
M84                            ; steppers off
G90                            ; absolute positioning
M117 TAZ Ready.
;{profile_string}"""




taz5_settings = [('nozzle_size', '0.35'),
				 ('wall_thickness', '1.05'),
				 ('retraction_speed', '10'),
				 ('retraction_hop', '0.1'),
				 ('layer0_width_factor', '125'),
				 ('travel_speed', '175'),
				 ('bottom_layer_speed', '15'),
				 ('skirt_minimal_length', '250'),
				 ('fan_full_height', '0.5'),
				 ('brim_line_count', '10'),
				 ('print_temperature', '0'),
				 ('print_bed_temperature', '0'),
				 ('retraction_minimal_extrusion', '0.005'),
				 ('start.gcode', taz5_start_gcode),
				 ('end.gcode', taz5_end_gcode)]

support_settings = [('support', _("Everywhere")),
					('support_type', 'Lines'),
					('support_angle', '45'),
					('support_fill_rate', '30'),
					('support_xy_distance', '0.7'),
					('support_z_distance', '0.05')]

brim_settings = [('platform_adhesion', 'Brim')]

abs_hips_settings = [('retraction_amount', '1'),
					 ('fan_speed', '40')]

hips_pla_settings = [('raft_airgap', '0.5')]

hips_settings = [('fan_speed_max', '50'),
				 ('cool_min_layer_time', '20')]
hips_low_settings = [('layer_height', '0.28'),
					 ('solid_layer_thickness', '0.84'),
					 ('infill_speed', '70'),
					 ('inset0_speed', '40'),
					 ('insetx_speed', '45')]
hips_normal_settings = [('layer_height', '0.22'),
						('solid_layer_thickness', '0.88'),
						('infill_speed', '50'),
						('inset0_speed', '30'),
						('insetx_speed', '35')]
hips_high_settings = [('layer_height', '0.14'),
					  ('solid_layer_thickness', '0.7'),
					  ('infill_speed', '30'),
					  ('inset0_speed', '20'),
					  ('insetx_speed', '25')]

abs_settings = [('fan_speed_max', '60'),
				('raft_airgap', '0.35')]
abs_low_settings = [('layer_height', '0.28'),
					('solid_layer_thickness', '0.84'),
					('infill_speed', '60'),
					('inset0_speed', '50'),
					('insetx_speed', '55'),
					('cool_min_layer_time', '15')]
abs_normal_settings = [('layer_height', '0.22'),
					   ('solid_layer_thickness', '0.88'),
					   ('infill_speed', '55'),
					   ('inset0_speed', '45'),
					   ('insetx_speed', '50'),
					   ('cool_min_layer_time', '15')]
abs_high_settings = [('layer_height', '0.16'),
					 ('solid_layer_thickness', '0.74'),
					 ('infill_speed', '40'),
					 ('inset0_speed', '30'),
					 ('insetx_speed', '35'),
					 ('cool_min_layer_time', '20')]

pla_settings = [('retraction_amount', '1.5'),
				('fan_speed', '75'),
				('fan_speed_max', '100')]
pla_low_settings = [('layer_height', '0.28'),
					('solid_layer_thickness', '0.84'),
					('infill_speed', '80'),
					('inset0_speed', '60'),
					('insetx_speed', '70'),
					('cool_min_layer_time', '15'),
					('cool_min_feedrate', '15')]
pla_normal_settings = [('layer_height', '0.21'),
					   ('solid_layer_thickness', '0.84'),
					   ('infill_speed', '60'),
					   ('inset0_speed', '50'),
					   ('insetx_speed', '55'),
					   ('cool_min_layer_time', '15'),
					   ('cool_min_feedrate', '10')]
pla_high_settings = [('layer_height', '0.14'),
					 ('solid_layer_thickness', '0.7'),
					 ('infill_speed', '50'),
					 ('inset0_speed', '40'),
					 ('insetx_speed', '45'),
					 ('cool_min_layer_time', '20'),
					 ('cool_min_feedrate', '5')]

# LulzBot TAZ 5 slice settings for use with the simple slice selection.
lulzbot_taz5_settings = [{'Settings': taz5_settings},
						 {'Brim': True,
						  'Settings': brim_settings},
						 {'Support': True,
						  'Settings': support_settings},

						 {'MaterialPLA': False,
						  'Settings': abs_hips_settings},
						 {'MaterialABS': False,
						  'Settings': hips_pla_settings},

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
