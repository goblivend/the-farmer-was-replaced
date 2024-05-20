def setup_dino() :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
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

def harvest_bones() :
	setup_dino()
	harvest_all()
