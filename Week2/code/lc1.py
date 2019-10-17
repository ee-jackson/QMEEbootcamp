birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

birds_latin = [i[0] for i in birds]
print(birds_latin)

birds_name = [i[1] for i in birds]
print(birds_name)

birds_mass = [i[2] for i in birds]
print(birds_mass)


# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

birds_latin=set()
for i in birds:
	birds_latin.add(i[0])
print(birds_latin)

birds_name=set()
for i in birds:
	birds_name.add(i[1])
print(birds_name)

birds_mass=set()
for i in birds:
	birds_mass.add(i[2])
print(birds_mass)
