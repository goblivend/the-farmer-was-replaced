def harvest_all() :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if can_harvest() :
				harvest()
			move(North)
		move(East)
