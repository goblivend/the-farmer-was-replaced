def setup_pumpkin():
	goxy(0, 0)
	for x in range(size) :
		for y in range(size) :
			if get_entity_type() != Entities.Pumpkin :
				grow()
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
	for x in range(size) :
		for y in range(size) :
			if get_entity_type() != Entities.Pumpkin :
				missings.append((x, y))
				water()
				buy_item(Items.Pumpkin_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
			elif not can_harvest() :
				missings.append((x, y))
			move(North)
		move(East)
	while len(missings) != 0 :
		new = []
		for xy in missings :
			x, y = xy
			goxy(x, y)
			if not can_harvest() :
				grow()
			if get_entity_type() != Entities.Pumpkin :
				new.append(xy)
			if get_entity_type() != Entities.Pumpkin :
				grow()
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