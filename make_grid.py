def make_grid(w, h) :
	grid = []
	for i in range(w) :
		grid.append([])
		for i2 in range(h) :
			grid[-1].append(None)
	return grid
