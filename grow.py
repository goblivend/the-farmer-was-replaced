def grow() :
	while not can_harvest() and get_entity_type() != None :
		water()
		if can_buy(Items.Fertilizer, 64) :
			buy_item(Items.Fertilizer)
			use_item(Items.Fertilizer)
