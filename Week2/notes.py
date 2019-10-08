#!/usr/bin/env python
# Author: Eleanor Jackson. eleanor.elizabeth.j@gmail.com
# Script: test
# Desc: 
# Arguments: 
# Date: 7th Oct 2019

#shows current namespace
%who

a=1

#tells you what the variables are
%whos

# gives you info about the variable
type(a)
a? # gives even more info

# a float is anything that can have decimal points, not an integer
# there are also strings and booleans

# if you do calcluations with object of integer divisions then the decimal will be lost e.g.
3//2
3/2

x= "My string"
x + " now has more stuff"
y= 2
x+ str(y)

# in python no difference between class and type

#############################################
##########Python data stuctures #############
#############################################

# data types#################################
# List:most versatile, can contain compound data, "mutable", enclosed in brackets, [ ]
# Tuple : like a list, but "immutable" — like a read only list, enclosed in parentheses, ( )
# Dictionary : a kind of "hash table" of key-value pairs enclosed by curly braces, { } — key can be number or string, values can be any python object
# numpy arrays : Fast, compact, convenient for numerical computing — more on this later


##Lists 
# they are  mutable
MyList = [3,2.44,"green", True]
MyList[1] # this brings up the second item in the list beaucse python indexing starts at 0 !
MyList[0]

MyList[2]="blue" # chnages the 3rd item to blue
MyList.append("a new item")
MyList

%whos
#or
type(MyList)

del MyList[2]


#TIP in ipython you can suffix an . to a particular object (e.g., MyList.), and then hit tab to see the methods that can be applied to that object.


###Tuples 
#are like a list, but "immutable", that is, a particular pair or sequence 
# of strings or numbers cannot be modified after it is created. So a tuple is like a read-only list.

FoodWeb=[('a','b'),('a','c'),('b','c'),('c','c')]
FoodWeb
FoodWeb[0]
FoodWeb[0][0]
FoodWeb[0][0] = "bbb" #error can't change this
FoodWeb[0] = ("bbb","ccc") # but you can change a whole pairing
FoodWeb[0]

# why would you use a tuple and not a list? beacuse you want to maintain something, and they are faster- fixed memory space and write-protects your data
# you cant remoce or add things but you can find elements, use in to check if somehting is in there
# you can append to tuples

a = (1, 2, []) 
a
a[2].append(1000)
a[2].append((100,10))
a

#you can also concatenate slice and dice them
a = (1, 2, 3)
b = a + (4, 5, 6)
b
c = b[1:]
c
b = b[1:]
b
a = ("1", 2, True)
a

##sets
# You can convert a list to an immutable "set" — an unordered collection with no duplicate elements. 
# Once you create a set you can perform set operations on it:

a = [5,6,7,7,7,8,9,9] #create a set
b = set(a)
b
c=set([3,4,5,6])
b&c #intersection, lists the elements that are in both?
b|c #union, all the elements of both- no duplicates
a-b # difference
a<=b #a as a subset of b
a>=b #b as a subset of a

##Dictionaries
#A dictionary is a set of values (any python object) indexed by keys (string or number). So they are a bit like R lists.

GenomeSize = {'Homo sapiens': 3200.0, 'Escherichia coli': 4.6, 'Arabidopsis thaliana': 157.0}
GenomeSize

GenomeSize['Arabidopsis thaliana']

GenomeSize['Saccharomyces cerevisiae'] = 12.1 # add something to the dictionary
GenomeSize['Escherichia coli'] = 4.6 # change a value in the dictionary


#So, in summary:
#
#If your elements/data are unordered and indexed by numbers use a list
#If you're defining a constant set of values (or ordered sequences) and all you're ever going to do with them is iterate through them, use a tuple.
#If you want to perform set operations on data, use a set
#If they are unordered and indexed by keys (e.g., names), use a dictionary
#But why not use dictionaries for everything? – because it can slow down your code!

# Copying mutable objects
a = [1, 2, 3]
b = a
# can be tricky- here have just created a new 'tag' for a called b
a.append(4)
b # you can see this beacuse any changes you make to a, are also made to b

a = [1, 2, 3]
b = a[:]  # This is a "shallow" copy
a.append(4) #[1, 2, 3, 4]   
b #[1, 2, 3] 

a = [[1, 2], [3, 4]]
b = a[:]
b

a[0][1] = 22 # Note how I accessed this 2D list
b# a shallow copy doesnt copy beyond the first level of the list- the nested values are still linked to a

# need to do a DEEPCOPY
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[0][1] = 22
b

# a deep copy will clone child objects which are fully independent but this is slower than creating a shallow copy

##STRINGS
# python is good at strings

s = " this is a string "
len(s) # length of s -> 18

s.replace(" ","-")
s.find("s") #how many s are there (there are 3 but it says 4 , indexing starts at 0)

t= s.split() # split the string using spaces and make a list
t
t=s.split (" is ") # split the string using is

t = s.strip() # remove trailing spaces
t
s.upper()
s.upper().strip() # can perform sequential operations
'WORD'.lower() # can perfrom operations directy on a literal string 

?s.upper() # for help

#witing python script
#program is self standing contaoned a script wont run in a vacume


