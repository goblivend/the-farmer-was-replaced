def measure_grid() :
	grid = make_grid(size, size)
	for x in range(size) :
		for y in range(size) :
			grid[y][x] = measure()
			move(North)
		move(East)
	return grid