from sys import argv

#read in arguments
script, filename = argv

#open file and store file handle as a variable
txt = open(filename)

#tell the user what we're doing, then print the
#entire contents of the file
print "Here's your file %r:" % filename
print txt.read()

#ask the user for the file name again using raw_input()
print "Type the filename again:"
file_again = raw_input("> ")

#store the input in another file handle variable
txt_again = open(file_again)

#print out the full file again
print txt_again.read()