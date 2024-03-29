############################
# FILE INPUT
############################
# Open a file for reading
f=open("sandbox/test.txt","r")
#use implicit for loop:
#if the object is a file, python will cylcle over lines
for line in f:
	print(line)

#close the fiels
f.close()

#Same example, skip blank lines
f=open("sandbox/test.txt","r")
for line in f:
	if len(line.strip()) > 0:
		print(line)

f.close()

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') ## Add a new line at the end

f.close()

#############################
# STORING OBJECTS
#############################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open('sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print(another_dictionary)

###
#Handling csv's

# Read a file containing:
# 'Species','Infraorder','Family','Distribution','Body mass male (Kg)'
f = open('../data/testcsv.csv','r')

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print(row)
    print("The species is", row[0])

f.close()

# write a file containing only species name and Body mass
f = open('../data/testcsv.csv','r')
g = open('../data/bodymass.csv','w')

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print(row)
    csvwrite.writerow([row[0], row[4]])

f.close()
g.close()

