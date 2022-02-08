import re

#block one

if re.search("coconut", "The coconut-milk is produce from coconut"):
    print("Coconut Found")

#block two

all_coconut = re.findall("coconut", "The coconut-milk is produce from coconut")
for i in all_coconut:
    print(i)
    
#block three
    
the_line = "The coconut-milk is produce from coconut."

for i in re.finditer("coconut.", the_line):
    loc_tup = i.span()
    print(loc_tup)
    print(the_line[loc_tup[0]:loc_tup[1]])

#block three

animal_line = "Cat rat bat Sat fat Tat mat kat"
all_animal = re.findall("[crbsftmk]at", animal_line)
some_animal_1 = re.findall("[b-sB-S]at",animal_line)
some_animal_2 = re.findall("[^CSm]at",animal_line)

for i in all_animal:
    print(i, end="  ")
print()
for i in some_animal_1:
    print(i, end="  ")
print()
for i in some_animal_2:
    print(i, end="  ")
print()


#block four

snake_food = "cat bat rat mat fat hat"
print(snake_food)
regex = re.compile("[bcr]at")
snake_food = regex.sub("Snake", snake_food)
print(snake_food)

#block five
rand_str = "He is one of our \\stuff in the kitchen"
print(r"Find \\stuff: ", re.search(r"\\stuff", rand_str))
