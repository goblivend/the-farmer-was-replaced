def buy_item(i):
	n = get_world_size() * get_world_size()
	c = num_items(i)
	if c < n :
		if num_unlocked(Unlocks.Multi_Trade) > 0 :
			return trade(i, n)
		else :
			for e in range(n-c) :
				if not trade(i) :
					return False
	return True
