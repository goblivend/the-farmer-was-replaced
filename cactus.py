def setup_cactus() :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			grow()
			if get_entity_type() != Entities.Cactus :
				harvest()
			buy_item(Items.Cactus_Seed)
			if num_items(Items.Cactus_Seed) == 0 :
				quick_print("Poor")
				return False
			if get_ground_type() != Grounds.Soil :
					till()
			water(0.3)
			plant(Entities.Cactus)
			move(North)
		move(East)
	return True

def nearest(not_sorted, xy) :
	for e in not_sorted :
		return e

def new_harvest(grid, not_sorted) :
	x = 0
	y = 0
	while len(not_sorted) > 0 :
		(x, y) = nearest(not_sorted, (x, y))
		not_sorted.remove((x, y))
		goxy(x, y)
		if y > 0 and grid[y][x] < grid[y-1][x] :
			swap(South)
			not_sorted.add((x, y-1))
			grid[y][x], grid[y-1][x] = grid[y-1][x], grid[y][x]

		if x > 0 and grid[y][x] < grid[y][x-1] :
			swap(West)
			not_sorted.add((x, y))
			not_sorted.add((x-1, y))
			grid[y][x], grid[y][x-1] = grid[y][x-1], grid[y][x]

def harvest_cactus() :
	goxy(0, 0)
	if not setup_cactus() :
		return
	grid = measure_grid()
	not_sorted = {(0, 0)}
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			not_sorted.add((x, y))
	
	new_harvest(grid, not_sorted)
	harvest()

harvest_cactus()
