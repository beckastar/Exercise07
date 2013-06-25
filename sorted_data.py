from sys import argv
import string

script, file_input = argv
f = open(file_input)

line = f.readline()


restaurantDictionary = {}


for line in f:
	line = string.strip(line)
	line = line.split(":")
	restaurantDictionary[line[0]] = int(line [1])

for key, value in restaurantDictionary.items():
	print "%s is rated at %d" % (key, value)





#print "%s is rated at %d." % (restaurantDictionary[key], restaurantDictionary[value] ) 

# split content of each line on the :

# add 