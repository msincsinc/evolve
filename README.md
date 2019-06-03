

###Description

Expirementation with simple genetics, evolution, equillibrium concepts in pygame

### Getting Started

Set start values in physics.py 

System wide attributes
```
world_physics.sprite_energy_per_pixel //energy consumed per sprite pixel
world_physics.background_energy_per_pixel //energy available in system
world_physics.world_width //UI width
world_physics.world_height //UI Height
world_physics.mutation_rate // rate at which entity attributes mutate
```

Element attributes
```
plant_one.type // element type - to be furthur defined
plant_one.initial_seeds_per_pixel // seeds produced per pixel 
plant_one.seed_size // seed size in pixels
plant_one.seed_rate_per_pixel_per_second // plant production rate per pixel per second 
plant_one.seed_distance // range of seed from parent
plant_one.seed_energy_consumption // energy consumtion per seed
plant_one.seed_chance // seed change
plant_one.growth_rate_per_second // element growth rate
plant_one.red // red pigment
plant_one.green // green pigment
plent_one.blue // blue pigment
```
running program
```
python main.py
```
### Prerequisites

Python 2.7x

Pygame

### Installing

create virtualenv (optional)

pip install pygame

copy evolve files to directory


This project is licensed under the MIT License
