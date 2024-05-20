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

	directions = [East, North, West, South]
	while get_entity_type() != Entities.Treasure :
		if move(directions[(i-1) % 4]) :
			i = (i-1) % 4
			continue

		if move(directions[i]) :
			continue

		if move(directions[(i+1) % 4]) :
			i = (i+1) % 4
			continue

		if move(directions[(i+2) % 4]) :
			i = (i+2) % 4
			continue
	harvest()
