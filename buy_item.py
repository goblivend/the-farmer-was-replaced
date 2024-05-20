def buy_item(i):
    size = get_world_size()
	n = size * size
	if num_items(i) < n :
		if num_unlocked(Unlocks.Multi_Trade) > 0 :
			return trade(i, n)
		else :
			for e in range(n) :
				if not trade(i) :
					return False
	return True
