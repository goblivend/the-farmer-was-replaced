def measure_grid() :
	grid = make_grid(get_world_size(), get_world_size())
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			grid[y][x] = measure()
			move(North)
		move(East)
	return grid