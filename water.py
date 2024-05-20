def water(n = 1):
	while get_water() < n :
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