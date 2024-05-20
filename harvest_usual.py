def harvest_usual(n) :
	goxy(0, 0)
	for x in range(size) :
		for y in range(size) :
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
