def can_buy(i, n):
	costs = get_cost(i) 
	for c in costs :
		if not enough(c, costs[c]*n) :
			return False
	return True