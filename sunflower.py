def setup_sunflower(size):
	goxy(0, 0)
	missing = True
	max_petal = 0
	maxx = 0
	maxy = 0
	grid = make_grid(size, size)
	while missing :
		missing = False
		for x in range(size) :
			for y in range(size) :
				buy_item(Items.Sunflower_Seed)
				if num_items(Items.Sunflower_Seed) < size * size :
					return
				if get_entity_type() != Entities.Sunflower :
					grow()
					if can_harvest() :
						harvest()
					if get_ground_type() != Grounds.Soil :
						till()
					plant(Entities.Sunflower)
					water()
					missing = True
				elif can_harvest() :
					if grid[y][x] != None :
						continue
					grid[y][x] = measure()
					if grid[y][x] > max_petal :
						max_petal = grid[y][x]
						maxx = x
						maxy = y
				else :
					missing = True
				move(North)
			move(East)
	return (grid, maxx, maxy)

def harvest_sunflower(n):
	grid, maxx, maxy= setup_sunflower(size)

	while num_items(Items.Power) < n :
		goxy(maxx, maxy)
		harvest()
		buy_item(Items.Sunflower_Seed)
		if num_items(Items.Sunflower_Seed) < size * size :
			return
		plant(Entities.Sunflower)
		grow()
		grid[maxy][maxx] = measure()
		for x in range(size) :
			for y in range(size) :
				if grid[y][x] > grid[maxy][maxx] :
					maxx = x
					maxy = y
