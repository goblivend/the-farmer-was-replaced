def handle_expand():
	size = get_world_size()
	goxy(0, size - 1)
	for i in range(size) :
		till()
		move(East)
	move(West)
	move(South)
	for i in range(size-1) :
		till()
		move(South)
	move(East)

def needs_too_much(u):
	if u == Unlocks.Reset :
		return False
	costs = get_cost(u)
	if costs == None :
		return True
	for c in costs :
		if c != Items.Wood and costs[c] >= 80000 :
			return True
	return False

def unlock_all():
	upgrade_unlocks = [
		Unlocks.Grass,
		Unlocks.Speed,
		Unlocks.Expand,
		Unlocks.Carrots,
		Unlocks.Pumpkins,
		Unlocks.Trees,
		Unlocks.Sunflowers,
		Unlocks.Cactus,
		Unlocks.Dinosaurs,
		Unlocks.Mazes
	]
	single_unlocks = [
		Unlocks.Plant,
		Unlocks.Fertilizer,
		#Unlocks.Polyculture,
		Unlocks.Leaderboard
	]
	for u in single_unlocks :
		if num_unlocked(u) == 0:
			if unlock(u) and u == Unlocks.Leaderboard :
				timed_reset()
	for u in upgrade_unlocks :
		if u == Unlocks.Mazes and num_items(Items.Gold) > 10000 :
			continue
		if needs_too_much(u) :
			continue
		if unlock(u) :
			if u == Unlocks.Expand :
				size = num_unlocked(u)+1
				if num_unlocked(Unlocks.Expand) > 2 :
					handle_expand()
