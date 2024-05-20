
def main() :
	while num_items(Items.Hay) < 20 :
		if can_harvest() :
			harvest()
	unlock(Unlocks.Speed)
	while num_items(Items.Hay) < 30 :
		if can_harvest() :
			harvest()
	unlock(Unlocks.Expand)
	while num_items(Items.Hay) < 50 :
		if can_harvest() :
			harvest()
			move(North)
	unlock(Unlocks.Plant)
	inc = 20
	n = 50
	while True :
		unlock_all()
		size = get_world_size()
		if (not enough(Items.Hay, n)) or (not enough(Items.Wood, n)) or (not enough(Items.Carrot, n) and num_unlocked(Unlocks.Carrots) > 0) :
			harvest_usual(n)
		elif  num_unlocked(Unlocks.Pumpkins) > 0 and not enough(Items.Pumpkin, n) :
			harvest_pumpkin()
		elif num_unlocked(Unlocks.Mazes) > 0 and not enough(Items.Gold, n) :
			treasure()
		elif num_unlocked(Unlocks.Sunflowers) > 0 and not enough(Items.Power, n / 3) and size > 5:
			harvest_sunflower(n)
		elif num_unlocked(Unlocks.Cactus) > 0 and not enough(Items.Cactus, n) and can_buy(Items.Cactus_Seed, size*size) and (num_unlocked(Unlocks.Dinosaurs) == 0 or num_items(Items.Cactus) < (2000 - num_items(Items.Bones) - num_items(Items.Egg)*2)* 60):
			harvest_cactus()
		elif num_unlocked(Unlocks.Dinosaurs) > 0 and not enough(Items.Bones, n) :
			harvest_bones()
		else :
			n += inc
			inc *= 8/5
			quick_print(n, inc)
			n = min(n, 5000)

main()
