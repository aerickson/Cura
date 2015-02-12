from Cura.util import profile

def nozzle_size_mult(mult):
    return float(profile.getProfileSetting('nozzle_size')) * mult

default_settings = [{'Settings': [('filament_diameter', '2.85')]},
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
					'Settings': [('wall_thickness', lambda: nozzle_size_mult(1.5))]},
				   {'TypeLow': False, 'TypeJoris': False,
					'Settings': [('wall_thickness', lambda: nozzle_size_mult(2.0))]},
				   {'TypeHigh': True,
					'Settings': [('layer_height', '0.06'),
								 ('fill_density', '20'),
								 ('bottom_layer_speed', '15')]},
				   {'TypeNormal': True,
					'Settings': [('layer_height', '0.10'),
								 ('fill_density', '20')]},
				   {'TypeLow': True,
					'Settings': [('wall_thickness', lambda: nozzle_size_mult(2.5)),
								 ('layer_height', '0.20'),
								 ('fill_density', '10'),
								 ('print_speed', '60'),
								 ('cool_min_layer_time', '3'),
								 ('bottom_layer_speed', '30')]}]
