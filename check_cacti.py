def check_cacti() :
	goxy(0, 0)
	grid = measure_grid()
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if y > 0 and grid[y-1][x] > grid[y][x] :
				quick_print("Wrong Cactus :", (x, y-1, grid[y-1][x]), (x, y, grid[y][x]))
			if x > 0 and grid[y][x-1] > grid[y][x] :
				quick_print("Wrong Cactus :", (x-1, y, grid[y][x-1]), (x, y, grid[y][x]))
