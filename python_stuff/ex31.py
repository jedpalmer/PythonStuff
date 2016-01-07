print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There is a man playing bagpipes. What do you do?"
	print "1. Immediately cover your ears and yell at him to stop."
	print "2. Give him some money."
	
	pipes = raw_input("> ")
	
	if pipes == "1":
		print "Six men in kilts knock you down and kick you to death. Good job!!"
	elif pipes == "2":
		print "He steps aside, revealing another door that you then walk through."
		print "You see a small Jack Russel Terrier asleep in his dog bed. What do you do?"
		print "1. Attempt to pet him."
		print "2. Try to sneak around him to the next room."
		
		rex = raw_input("> ")
		
		if rex == "1":
			print "He rips your face off. Good job!"
		elif rex == "2":
			print "He wakes up and latches onto your ankle. You leave the dungeon to go to the hospital, but still die of infection a week later. Good job!"
		else:
			print "That's probably a better idea anyway."
	else:
		print "You decide it's not worth it, turn around, and go home."

		
elif door == "2":
	print "You are now outside in a vegetable garden. What do you do?"
	print "1. Pick some tomatoes."
	print "2. Walk through the garden to the gate on the far side."
	print "3. Burn it."
	
	garden = raw_input("> ")
	
	if garden == "1" or garden == "2":
		print "Hands emerge from the soil and drag you down, never to be heard from again. Good job!"
	elif garden == "3":
		print "You've saved the world! Good job!"
	else:
		print "Yeah, better not to mess with strange gardens."
		
else:
	print "You stumble around and fall on a knife and die. Good job!"
		