# Control flow tools
# OK, let's get deeper into python code. A computer script or program's control flow is the order in which the code executes. Upto now, you have written scripts with simple control flows, with the code executing statements from the top to bottom. But very often, you want more flexible flows of commands and statements, for example, where you can switch between alternative commands depending on some condition. This is possible using control flow tools. Let's learn python's control flow tools hands-on.

# Conditionals
# Try these function by function, pasting the block in the ipython command line (hopefully you have set your code editor to send a selection to the command line by now (see the Unix Chapter)).

#gives x
def foo_1(x):
	return x

foo_1(3)


# gives the bigger number
def foo_2(x, y):
    if x > y:
        return x
    return y

foo(2,3)


#puts the variables in order
def foo_3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]


def foo_4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

# a recursive function that calculates the factorial of x
def foo_5(x): 
    if x == 1:
        return 1
    return x * foo_5(x - 1)

def foo_6(x): # Calculate the factorial of x in a different way
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

# Loops
# Write the following, and save them to loops.py:

#FOR loops
for i in range(5):
	print(i)

my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
	print(k)

total = 0
summands = [0, 1 ,11, 111, 1111]
for s in summands:
	total  = total + s
	print(total)

#WHILE loops
z = 0
while z<100:
	z = z + 1
	print(z)

b = True
while b:
	print("GERONIMO! infinate loop! ctrl+c to stop!")
#actually ctrl not command

#############################
#Loops and conditionals
############################

for j in range(12):
    if j % 3 == 0:
        print(j, 'hello')

for j in range(15):
     if j % 5 == 3:
        print(j, 'hello')
     elif j % 4 == 3:
        print(j, 'hello')

z = 0
while z != 15:
    print('hello')
    z = z + 3

z = 12
while z < 100:
    if z == 31:
        for k in range(7):
            print('hello')
    elif z == 18:
        print('hello')
    z = z + 1

#     Comprehensions
# Python offers a way to combine loops, functions and logical tests / conditionals in a single line of code to transform any iterable object (list, set, or dictionary, over which you can iterate) into another object, after performing some operations on the elements in the original object. That is, they are a compact way to create a new list, dictionary or object from an existing one. As you might expect, there are three types of comprehensions, each corresponding to what the target object is (list, set, dictionary).

x = [i for i in range(10)]
print(x)

#this is the same as the following loop

x = []
for i in range(10):
	x.append(i)
print(x)

# another example:

x = [i.lower() for i in ["LIST","COMPREHENSIONS", 'ARE', 'COOL']]
print(x)

#which is ths same as this loop

x= ["LIST", 'COMPREHESNSIONS','ARE','COOL']
for i in range(len(x)): #explicit loop
	x[i] = x[i].lower()
print(x)

#or this loop

x = ["LIST","COMPREHENSIONS","ARE","COOL"]
x_new = []
for i in x: # implicit loop
    x_new.append(i.lower())
print(x_new)

# a nested loop
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened_matrix =[]
for row in matrix:
	for n in row:
		flattened_matrix.append(n)
print(flattened_matrix)

#a list comprehension to do the same
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened_matrix = [n for row in matrix for n in row]
print(flattened_matrix)

# Set and Dictionary comprehensions work in an analogous way. For example, create a set of all the first letters in a sequence of words using a loop:

words = (["These", "are", "some", "words"])
first_letters = set()
for w in words:
    first_letters.add(w[0])
print(first_letters)


