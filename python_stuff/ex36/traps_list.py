#list of functions that define the traps

def get_response(options):
	"""loops until user enters a valid response from a list of options"""
	valid_response = False
	
	for index, item in enumerate(options, start=1):
		print index, item
	
	while valid_response == False:
		pick = int(raw_input("> "))
		if pick <= len(options):
			valid_response = True
			return pick
		else:
			print "What was that?"
			
			
#below here are all the trap functions. If the player lives, the return a value of True. If they die, return a value of False
def wentworth():
	print "Chris Wentworth approaches you and asks:"
	print '"Hey, could you help me cut down a tree?"'
	print "What do you tell him?"
	
	choices = ['fuck off', 'sure thing', 'Can I use the chainsaw?']
	
	input = get_response(choices)
	
	if input == 1:
		print "Chris storms off in a huff. You are safe."
		return True
	elif input == 2:
		print "You go off with Chris to help with the tree."
		print "The tree falls in the 'safe' area and crushes you. You are dead."
		return False
	elif input == 3:
		print "Chris goes into a rage and cuts you in half. You are dead."
		return False
	else:
		#shouldn't have gotten to this case, use it for error checking
		print "You shouldn't have gotten here."
		return False
		
			
def mud():
	print "Thick sticky mud starts oozing up from the floor."
	print "It's already up to your ankles."
	print "What do you do?"
	
	choices = ['panic', 'roll around like a pig', 'call for help', 'put on my wellies']
	
	input = get_response(choices)
	
	if input == 1:
		print "The mud continues to rise until it swallows you up."
		print "You are dead."
		return False
	elif input == 2:
		print "The mud continues to rise until it swallows you up,"
		print "but at least you had fun while you died."
		return False
	elif input == 3:
		return wentworth()
	elif input == 4:
		print "You traipse through the mud to safety."
		return True
	else:
		#user shouldn't get to this case, error check
		print "You shouldn't be here."
		return False
		

def trapdoor():
	print "A trapdoor opens beneath you. You are falling and cannot see the bottom."
	print "What do you do?"
	
	choices = ['use my shirt like a parachute', 'wait', 'flap my arms']
	
	input = get_response(choices)
	
	if input == 1:
		print "As you float gently down, you maneuver safely into a door in the side of the shaft."
		print "You are safe."
		return True
	elif input == 2:
		print "You starve to death waiting to hit the bottom."
		return False
	elif input == 3:
		print "Surprisingly, you are able to hover!"
		print "You fly back up to the top of the shaft and land safely"
		return True
	else:
		#user shouldn't end up here
		print "You shouldn't be here."
		return False
		
		
def walls():
	print "The walls of this room are slowly closing in on you."
	print "You will soon be crushed to death."
	print "What do you do?"
	
	choices = ['turn sideways and hope they stop', 'tell C3PO to turn off all the garbage smashers on the detention level', 'brace the walls with this convenient stick', 'flick off the light switch near the door']
	
	input = get_response(choices)
	
	if input == 1:
		print "The walls don't stop and you are crushed."
		return False
	elif input == 2:
		print "A snaky thing springs from the floor and eats you."
		return False
	elif input == 3:
		print "The stick holds the walls just long enough for you to kick the door down at the opposite end of the room"
		print "You are safe."
		return True
	elif input == 4:
		print "The walls stop. You walk calmly to the other end of the room and go through the door."
		print "You are safe."
		return True
	else:
		print "Invalid input"
		return False


def snare():
	print "Suddenly a noose tightens around your feet,"
	print "and you find yourself hanging upside down, ankles tied together."
	print "What do you do?"
	
	choices = ['Smear some of my lunch on the rope and hope the rats chew through it', 'Call for help', 'Use the Force', 'Gnaw through my ankles']
	
	input = get_response(choices)
	
	if input == 1:
		print "There are no rats here, and now you have no food."
		print "You slowly starve to death hanging there."
		return False
	elif input == 2:
		print "A hungry bear hears your call and eats you."
		return False
	elif input == 3:
		print "The rope unties itself and you fall to the floor,"
		print "bruised, but safe."
		return True
	elif input == 4:
		print "You get through one ankle but then pass out from the pain."
		print "You are never heard from again."
		return False
	else:
		print "Invalid input"
		return False
	
	
def darts():
	print "A dart shoots out from the wall and hits you in the leg"
	print "You start feeling woozy."
	print "There are 3 labeled bottles on a table in front of you."
	print "Which one do you drink?"
	
	choices = ['bleach', 'antidote', 'hair dye']
	
	input = get_response(choices)
	
	if input == 1:
		print "The bleach reacts with the poison."
		print "You let out a huge belch and feel much better"
		print "You are safe."
		return True
	if input == 2:
		print "It turns out to be the wrong antidote."
		print "Your legs turns green and falls off."
		print "You are dead."
		return False
	if input == 3:
		print "You are an idiot, but your hair is now nice and shiny and pink."
		print "You still die from the poison."
		return False
		