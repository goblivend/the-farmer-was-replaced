def clean():
	size = get_world_size()
	goxy(0, 0)
	for x in range(size) :
		for y in range(size) :
			water()
			if can_harvest() :
				harvest()
			if get_ground_type() != Grounds.Soil :
				till()
			move(North)
		move(East)
