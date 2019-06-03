
#3rd party libraries
import pygame

#import system libraries
import random
import sys
import psutil
import time

#local imports
import physics as phys





def main():

	pygame.init()
	
	my_font = pygame.font.SysFont("Courier", 12)
	frame_count = 0
	frame_rate = 0
	clock = pygame.time.Clock()



	#logo = pygame.image.load("logo32x32.png")
	#pygame.display.set_icon(logo)
	pygame.display.set_caption("Evolve")

	world_width = phys.world_physics['world_width']
	world_height = phys.world_physics['world_height']
	world_area = world_height*world_width
	mutation_rate = phys.world_physics['mutation_rate']
	energy_limit = world_area * phys.world_physics['background_energy_per_pixel']

	screen = pygame.display.set_mode((world_width,world_height))

	#iterate over initial entities and populate world

	world_object = []
	for entity in phys.initial:
		
		total_seeds = entity['initial_seeds_per_pixel'] * world_area
		for seed in range(int(total_seeds)):
			to_append = {'ent_def' : entity, 'entities' : []}
			x_loc = random.randint(1,world_width + 1)
			y_loc = random.randint(1,world_height + 1)
			size = entity['seed_size']
			to_append['entities'] += [[ x_loc, y_loc, entity['seed_size'], entity['seed_size']]]
			#pygame.draw.rect(screen, (100,100,100), (x_loc, y_loc, entity['seed_size'], entity['seed_size']))
			world_object += [to_append]
	running = True

	while running:

		screen.fill((0,0,0))

		#if frame_count % 200 == 0:
			#t1 = time.clock()
			#frame_rate = 200 / (t1-t0)
			#t0 = t1

		

		running_energy = 0
		total_ents = 0


		for entity in world_object:
			#print 'length of entities' + str(len(entity["entities"]))
			for entities in entity["entities"]:

				
				total_ents += 1
				red = entity['ent_def']['red'] % 255
				blue = entity['ent_def']['blue'] % 255
				green = entity['ent_def']['green'] % 255
				pygame.draw.rect(screen, (red,green,blue), (entities[0], entities[1], entities[2], entities[3]))
				
				

				entity_energy_consumption = entities[2] * entities[3]
				running_energy += entity_energy_consumption
				

				##SEED
				#seed_rate = 0.01
				seed_rate = entity['ent_def']['seed_rate_per_pixel_per_second']
				ent_size = entities[2] * entities[3]
				seeds = int(seed_rate * ent_size)
				ent_x_loc = entities[0]
				ent_y_loc = entities[1]

				
				if seeds >= 1:
					mutated_ent_def = {}
					#ad to seed def 
					for attribute, value in entity['ent_def'].iteritems():
						try:
							if random.randint(0,1) == 0:
								mutated_ent_def.update({attribute : value * (1+ mutation_rate)})
							else:
								mutated_ent_def.update({attribute : value * (1- mutation_rate)})
						except:
							mutated_ent_def.update({attribute : value })
						

					to_append = {'ent_def' : mutated_ent_def, 'entities' : []}
					for seed in range(seeds):
						seed_distance = int(entity['ent_def']['seed_distance'])
						x_loc = random.randint(-seed_distance, seed_distance) + ent_x_loc
						y_loc =  random.randint(-seed_distance, seed_distance) + ent_y_loc
						if x_loc < 0:
							x_loc *= -1
						if y_loc < 0:
							y_loc *= -1
						if x_loc > world_width:
							x_loc = x_loc - (x_loc -world_width)
						if y_loc > world_height:
							y_loc = y_loc - (y_loc -world_height)
						size = entity['ent_def']['seed_size']
						to_append['entities'] += [[ x_loc, y_loc, entity['ent_def']['seed_size'], entity['ent_def']['seed_size']]]
					world_object += [to_append]
					
					entities[2] = entities[2] - (size * 2)
					entities[3] = entities[3] - (size * 2)

				entities[2] += entity['ent_def']['growth_rate_per_second']
				entities[3] += entity['ent_def']['growth_rate_per_second']


		print 'Total Ents: ', total_ents
		print 'Total Energy: ', running_energy
		#print 'energy_limit: ', energy_limit
		#print psutil.virtual_memory()
		#print pygame
		
		ent_limit = 1000
		if total_ents > ent_limit:
			overage = total_ents - ent_limit
			remove_count_one = overage
			
			print remove_count_one
			
			for remove in range(remove_count_one):

				which_ent_group = random.randint(0,len(world_object)) - 1
				which_ent = random.randint(0,len(world_object[which_ent_group]["entities"])) - 1
				if which_ent_group > 0:			
					world_object[which_ent_group]["entities"].pop(which_ent)
				if len(world_object[which_ent_group]["entities"]) == 0:
					world_object.pop(which_ent_group)
		

		if running_energy > energy_limit:
			overage = running_energy - energy_limit
			average_ent_energy = running_energy / total_ents
			remove_count = int(overage/average_ent_energy)
			print remove_count
			
			
			
		
			for remove in range(remove_count):
			
				which_ent_group = random.randint(0,len(world_object)) - 1
				
				which_ent = random.randint(0,len(world_object[which_ent_group]["entities"])) - 1
				
				if which_ent_group > 0:			
					world_object[which_ent_group]["entities"].pop(which_ent)
				
			
				if len(world_object[which_ent_group]["entities"]) == 0:
					world_object.pop(which_ent_group)
		
		#comp_limit = sys.getsizeof(world_object)
		#the_text = my_font.render("limit = {0} rate = {1:.2f} fps".format(comp_limit, frame_rate), True, (250,250,250))
        # Copy the text surface to the main surface
		pygame.draw.rect(screen, (0,0,0), (0, 0, world_width, 40))
		#screen.blit(the_text, (10, 5))
		#frame_count +=1
		clock.tick(20)
		pygame.display.flip()
		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				running = False

if __name__=="__main__":
    # call the main function
    main()