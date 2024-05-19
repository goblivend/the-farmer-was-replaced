def goxy(x, y):
	dirs = [North, East, South, West]
	n = get_pos_x() - x
	if n < 0 :
		dir = 1
		n = -n
	else :
		dir = 3

	if n > get_world_size() / 2 :
		n = get_world_size() - n
		dir = (dir + 2) % 4

	for i in range(n) :
		move(dirs[dir])


	n = get_pos_y() - y
	if n < 0 :
		dir = 0
		n = -n
	else :
		dir = 2

	if n > get_world_size() / 2 :
		n = get_world_size() - n
		dir = (dir + 2) % 4

	for i in range(n) :
		move(dirs[dir])
	#while get_pos_x() != x :
	#	move(West)

	#while get_pos_y() != y :
	#	move(South)


def clean():
	goxy(0, 0)
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			water()
			if can_harvest() :
				harvest()
			if get_ground_type() != Grounds.Soil :
				till()
			move(North)
		move(East)

def can_buy(i, n):
	costs = get_cost(i)
	cond = True
	for c in costs :
		if not enough(c[0], c[1]*n) :
			cond = False
			break
	return cond


def buy_item(i):
	n = get_world_size()
	n *= n
	if num_items(i) < n :
		if num_unlocked(Unlocks.Multi_Trade) > 0 :
			trade(i, n)
		else :
			for e in range(n) :
				trade(i)

def enough(item, n):
	return num_items(item) >= n


def water():
	while get_water() < 1 :
		use_item(Items.Water_Tank)
		if num_items(Items.Water_Tank) == 0 :
			break
	if num_items(Items.Wood) > 500 and num_items(Items.Water_Tank) < 10 and num_unlocked(Unlocks.Watering) > 0 :
		if can_buy(Items.Empty_Tank, 20) :
			if num_unlocked(Unlocks.Multi_Trade) > 0 :
				trade(Items.Empty_Tank, 20)
			else :
				for i in range(20) :
					trade(Items.Empty_Tank)
	while num_unlocked(Unlocks.Sunflowers) >= 5 and get_active_power() < 30 :
		if num_items(Items.Power) > 1 :
			use_item(Items.Power)
		else :
			break
	#print(get_active_power())

def buy_barrels():
	while num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) <= 3000 :
		trade(Items.Empty_Tank)

def harvest_all() :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if can_harvest() :
				harvest()

def harvest_usual(n) :
	goxy(0, 0)
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if can_harvest() :
				harvest()
			if (not enough(Items.Hay, n)) or (not enough(Items.Wood, n)) :
				if (x+y) % 2 == 0 and num_items(Items.Hay) > num_items(Items.Wood) / 4:
					water()
					if num_unlocked(Unlocks.Trees) > 0 :
						plant(Entities.Tree)
					else :
						plant(Entities.Bush)
				elif get_ground_type() == Grounds.Soil:
					plant(Entities.Grass)
			elif num_unlocked(Unlocks.Carrots) > 0 :
				buy_item(Items.Carrot_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Carrots)
			move(North)
		move(East)

def setup_sunflower(size):
	#size = 3#get_world_size()
	goxy(0, 0)
	missing = True
	max_petal = 0
	maxx = 0
	maxy = 0
	grid = []
	for i in range(size) :
		grid.append([])
		for i2 in range(size) :
			grid[-1].append(None)
	while missing :
		missing = False
		for x in range(size) :
			for y in range(size) :
				buy_item(Items.Sunflower_Seed)
				if num_items(Items.Sunflower_Seed) < get_world_size() * get_world_size() :
					return
				if get_entity_type() != Entities.Sunflower :
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
						maxx = x#get_pos_x()
						maxy = y#get_pos_y()
				else :
					missing = True
				move(North)
			move(East)
	return [grid, maxx, maxy]


def harvest_sunflower(n):
	print(n)
	#n = 1000
	size = get_world_size()

	res = setup_sunflower(size)
	grid = res[0]
	maxx = res[1]
	maxy = res[2]

	while num_items(Items.Power) < n :
		goxy(maxx, maxy)
		#water()
		#print(grid)
		harvest()
		buy_item(Items.Sunflower_Seed)
		if num_items(Items.Sunflower_Seed) < get_world_size() * get_world_size() :
			return
		plant(Entities.Sunflower)
		while not can_harvest() :
			water()
			if can_buy(Items.Fertilizer, 64) :
				buy_item(Items.Fertilizer)
				use_item(Items.Fertilizer)
			else :
				do_a_flip()
		grid[maxy][maxx] = measure()
		for x in range(size) :
			for y in range(size) :
				if grid[y][x] > grid[maxy][maxx] :
					maxx = x
					maxy = y

def setup_pumpkin():
	goxy(0, 0)
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if get_entity_type() != Entities.Pumpkin :
				if can_harvest() :
					harvest()
				buy_item(Items.Pumpkin_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
			move(North)
		move(East)

def harvest_pumpkin():
	setup_pumpkin()
	missings = []
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if get_entity_type() != Entities.Pumpkin :
				missings.append([x, y])
				water()
				buy_item(Items.Pumpkin_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
			move(North)
		move(East)

	while len(missings) != 0 :
		new = []
		for xy in missings :
			goxy(xy[0], xy[1])
			if get_entity_type() != Entities.Pumpkin or not can_harvest() :
				new.append(xy)
			if get_entity_type() != Entities.Pumpkin :
				if can_harvest() :
					harvest()
				water()
				buy_item(Items.Pumpkin_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
		missings = new

	harvest()
	goxy(0, 0)

def can_move(i):
	directions = [East, North, West, South]
	x = get_pos_x()
	y = get_pos_y()
	move(directions[i])
	return x != get_pos_x() or y != get_pos_y()

def treasure() :
	while get_entity_type() != None and not can_harvest():
		continue
	harvest()
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		plant(Entities.Bush)
		while not can_harvest() :
			water()
			buy_item(Items.Fertilizer)
			use_item(Items.Fertilizer)
		while get_entity_type() == Entities.Bush :
			buy_item(Items.Fertilizer)
			use_item(Items.Fertilizer)
	i = 0
	while get_entity_type() != Entities.Treasure :
		if can_move((i-1) % 4) :
			i = (i-1) % 4
			continue

		if can_move(i) :
			continue

		if can_move((i+1) % 4) :
			i = (i+1) % 4
			continue

		if can_move((i+2) % 4) :
			i = (i+2) % 4
			continue
	harvest()

def can_unlock(u):
	costs = get_cost(u)
	cond = True
	for c in costs :
		if not enough(c[0], c[1]) :
			cond = False
			break
	return cond

def needs_too_much(u):
	if u == Unlocks.Reset :
		return False
	costs = get_cost(u)
	for c in costs :
		if c[0] != Items.Wood and c[1] >= 80000 :
			return True
	return False

def handle_expand():
	goxy(0, get_world_size() - 1)
	for i in range(get_world_size()) :
		till()
		move(East)
	move(West)
	move(South)
	for i in range(get_world_size()-1) :
		till()
		move(South)
	move(East)

def unlock_all():
	upgrade_unlocks = [
		Unlocks.Grass,
		Unlocks.Speed,
		Unlocks.Expand,
		Unlocks.Carrots,
		Unlocks.Pumpkins,
		Unlocks.Trees,
		Unlocks.Sunflowers,
		Unlocks.Mazes
	]
	single_unlocks = [
		Unlocks.Loops,
		Unlocks.Plant,
		Unlocks.Senses,
		Unlocks.Watering,
		Unlocks.Fertilizer,
		Unlocks.Multi_Trade,
		#Unlocks.Polyculture,
		Unlocks.Reset
	]
	for u in single_unlocks :
		if num_unlocked(u) == 0:
			if can_unlock(u) :
				unlock(u)
	for u in upgrade_unlocks :
		if u == Unlocks.Mazes and num_items(Items.Gold) > 10000 :
			continue
		if needs_too_much(u) :
			continue
		if can_unlock(u) :
			unlock(u)
			if u == Unlocks.Expand and num_unlocked(Unlocks.Expand) > 2 :
				handle_expand()
			elif u == Unlocks.Reset :
				reset()

def min(a, b):
	if a < b :
		return a
	return b

def main() :
	while num_unlocked(Unlocks.Expand) < 1 or num_unlocked(Unlocks.Plant) < 1 :
		while num_items(Items.Hay) < 50 :
			if can_harvest() :
				harvest()
		unlock_all()
	inc = 20
	n = 50
	while True :
		unlock_all()
		if (not enough(Items.Hay, n)) or (not enough(Items.Wood, n)) or (not enough(Items.Carrot, n) and num_unlocked(Unlocks.Carrots) > 0) :
			harvest_usual(n)
		elif not enough(Items.Pumpkin, n) and num_unlocked(Unlocks.Pumpkins) > 0:
			harvest_pumpkin()
		elif not enough(Items.Gold, min(20000, n)) and num_unlocked(Unlocks.Mazes) > 0 :
			did_treasure = True
			treasure()
		elif not enough(Items.Power, n / 3) and num_unlocked(Unlocks.Sunflowers) > 0 and get_world_size() > 5:
			harvest_sunflower(n)
		else :
			n += inc
			inc *= 8/5

		if num_unlocked(Unlocks.Reset) == 1 :
			reset()
			break
