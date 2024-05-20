def setup_dino() :
	size = get_world_size()
	goxy(0, 0)
	for x in range(size) :
		for y in range(size) :
			if get_entity_type() != Entities.Dinosaur :
				grow()
				if can_harvest() :
					harvest()
				buy_item(Items.Egg)
				if num_items(Items.Egg) == 0 :
					return
				use_item(Items.Egg)	
			move(North)
		move(East)
def swap_all() :
	size = get_world_size()
	for x in range(size) :
		for y in range(size) :
			swap(East)
			move(North)
		move(East)

def harvest_bones() :
	setup_dino()
	harvest_all()
