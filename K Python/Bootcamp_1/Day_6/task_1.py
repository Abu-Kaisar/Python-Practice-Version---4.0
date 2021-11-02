import random

one_to_one_thousand = []

# 100 number randomly by between 1 to 1000
for i in range(100):
    one_to_one_thousand.append(random.randint(1,1000))

#FILTERING THOSE NUMBERS MULTIPYER OF 9
nine_multiple_list = list(filter((lambda x: x % 9 == 0), one_to_one_thousand))
print(nine_multiple_list)
