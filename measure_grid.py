def measure_grid() :
	size = get_world_size()
	grid = make_grid(size, size)
	for x in range(size) :
		for y in range(size) :
			grid[y][x] = measure()
			move(North)
		move(East)
	return grid
