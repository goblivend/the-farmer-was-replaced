def goxy(x, y):
	dirs = [North, East, South, West]
	n = get_pos_x() - x
	if n < 0 :
		dir = 1
		n = -n
	else :
		dir = 3

	if n > get_world_size() / 2 :
		n = get_world_size() - n
		dir = (dir + 2) % 4

	for i in range(n) :
		move(dirs[dir])


	n = get_pos_y() - y
	if n < 0 :
		dir = 0
		n = -n
	else :
		dir = 2

	if n > get_world_size() / 2 :
		n = get_world_size() - n
		dir = (dir + 2) % 4

	for i in range(n) :
		move(dirs[dir])
