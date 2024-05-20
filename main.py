size = get_world_size()
def main() :
	while num_unlocked(Unlocks.Expand) < 1 or num_unlocked(Unlocks.Plant) < 1 :
		while num_items(Items.Hay) < 50 :
			if can_harvest() :
				harvest()
		unlock_all()
	inc = 20
	n = 50
	while True :
		unlock_all()
		if (not enough(Items.Hay, n)) or (not enough(Items.Wood, n)) or (not enough(Items.Carrot, n) and num_unlocked(Unlocks.Carrots) > 0) :
			harvest_usual(n)
		elif  num_unlocked(Unlocks.Pumpkins) > 0 and not enough(Items.Pumpkin, n) :
			harvest_pumpkin()
		elif num_unlocked(Unlocks.Mazes) > 0 and not enough(Items.Gold, n) :
			treasure()
		elif num_unlocked(Unlocks.Sunflowers) > 0 and not enough(Items.Power, n / 3) and size > 5:
			harvest_sunflower(n)
		#elif num_unlocked(Unlocks.Cactus) > 0 and not enough(Items.Cactus, n) and can_buy(Items.Cactus_Seed, size*size*2) :
		#	harvest_cactus()
		else :
			n += inc
			inc *= 8/5
			quick_print(n, inc)

		if num_unlocked(Unlocks.Reset) == 1 :
			reset()
			break
main()
