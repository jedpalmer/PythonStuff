#Game for fun

import random #allows random choice from list, e.g. random.choice(list)
from traps_list import *


def is_a_trap():
	"""Returns a random true/false value to decide if there is a trap"""
	return bool(random.getrandbits(1))
	
def spring_trap():
	if not is_a_trap():
		return None
	else
		print "A trap is sprung!"
	
	#Here we decide which trap from the list of traps is sprung in this room
	trap = random.choice(traps)
	
#user has to get through 4 rooms to survive