import sys 
import os

filename=sys.argv[1]

if not os.path.exists(filename):
	with open(filename, "w") as file:
		file.write("New file is created\n")
else:
	print("Error: the {} has already exists!".format(filename))
	sys.exit(1)