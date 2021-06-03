# Read the data file
filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')

with open(filename, 'r') as datafile: # context manager that automatically closes when finished
   data = datafile.read()

print(type(data))