def can_buy(i, n):
	costs = get_cost(i)
	cond = True 
	for c in costs :
		if not enough(c, costs[c]*n) :
			cond = False
			break
	return cond