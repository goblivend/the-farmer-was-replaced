
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
		if (not enough(Items.Hay, min(8000, n))) or (not enough(Items.Wood, min(8000, n))) or (not enough(Items.Carrot, min(8000, n)) and num_unlocked(Unlocks.Carrots) > 0) :
			harvest_usual(min(8000, n))
		elif num_unlocked(Unlocks.Pumpkins) > 0 and not enough(Items.Pumpkin, min(16000, n)) :
			harvest_pumpkin()
		elif num_unlocked(Unlocks.Mazes) > 1 and not enough(Items.Gold, min(16000, n)) :
			treasure()
		elif num_unlocked(Unlocks.Sunflowers) > 0 and not enough(Items.Power, min(15000, n / 3)) and get_world_size() > 5:
			harvest_sunflower(min(15000, n / 3))
		elif num_unlocked(Unlocks.Cactus) > 1 and not enough(Items.Cactus, min(10000, n)) and can_buy(Items.Cactus_Seed, get_world_size()*get_world_size()) and (num_unlocked(Unlocks.Dinosaurs) == 0 or num_items(Items.Cactus) < (2000 - num_items(Items.Bones) - num_items(Items.Egg)*2)* 60): 
			harvest_cactus()
		elif num_unlocked(Unlocks.Dinosaurs) > 0 and not enough(Items.Bones, n) :
			harvest_bones()
		else :
			n += inc
			inc *= 1.5
main()
