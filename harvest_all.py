def harvest_all() :
	size = get_world_size()
	for x in range(size) :
		for y in range(size) :
			if can_harvest() :
				harvest()
			move(North)
		move(East)
