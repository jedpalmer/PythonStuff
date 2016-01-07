from sys import argv

script, cats, dogs = argv

cats = int(cats)
dogs = int(dogs)
people = int(raw_input("How many people are there? "))
print "There are %s cats." % cats
print "There are %s dogs." % dogs
print "There are %s people." % people
print "Oops, now there are only %d cats." % (cats - dogs + people)
