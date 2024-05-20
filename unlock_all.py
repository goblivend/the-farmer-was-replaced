def handle_expand():
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
		Unlocks.Loops,
		Unlocks.Plant,
		Unlocks.Senses,
		Unlocks.Watering,
		Unlocks.Fertilizer,
		Unlocks.Multi_Trade,
		#Unlocks.Polyculture,
		Unlocks.Leaderboard
	]
	for u in single_unlocks :
		if num_unlocked(u) == 0:
			if unlock(u) :
				
				if u == Unlocks.Reset :
					reset()
	for u in upgrade_unlocks :
		if u == Unlocks.Mazes and num_items(Items.Gold) > 10000 :
			continue
		if needs_too_much(u) :
			continue
		if unlock(u) :
			if u == Unlocks.Expand and num_unlocked(Unlocks.Expand) > 2 :
				handle_expand()
