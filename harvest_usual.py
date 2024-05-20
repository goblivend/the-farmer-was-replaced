def harvest_usual(n) :
	water_lvl = 0
	goxy(0, 0)
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if can_harvest() :
				harvest()
			elif get_entity_type() != None :
				water_lvl = min(1, water_lvl + 0.1)
				water(water_lvl)
			if (not enough(Items.Hay, n)) or (not enough(Items.Wood, n)) :
				if (x+y) % 2 == 0 and num_items(Items.Hay) > num_items(Items.Wood) / 2:
					water(water_lvl)
					if num_unlocked(Unlocks.Trees) > 0 :
						plant(Entities.Tree)
					else :
						plant(Entities.Bush)
				elif get_ground_type() == Grounds.Soil:
					plant(Entities.Grass)
			elif num_unlocked(Unlocks.Carrots) > 0 :
				water(water_lvl)
				buy_item(Items.Carrot_Seed)
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Carrots)
			move(North)
		move(East)
 