
world_physics = {
	'sprite_energy_per_pixel' : 1,
	'background_energy_per_pixel' : 0.02,
	'world_width' : 1300,
	'world_height' : 700,
	'mutation_rate' : .1
}

plant_one = {
	'type' : 'plant',
	'initial_seeds_per_pixel' : 0.001,
	'seed_size' : 1,
	'seed_rate_per_pixel_per_second' : 0.001,
	'seed_distance' : 200,
	'birth_energy_consumption' : 0.3,
	'birth_chance' : 0.5,
	'growth_rate_per_second' : 1,
	'energy_avail_per_pixel' : 1,
	'red' : 100,
	'green' : 100,
	'blue' : 100
}

initial = [plant_one]