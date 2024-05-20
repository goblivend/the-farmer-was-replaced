def harvest_all() :
	for x in range(size) :
		for y in range(size) :
			if can_harvest() :
				harvest()
