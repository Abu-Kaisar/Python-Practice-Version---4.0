import random

h_t = ["H", "T"]
final_list = []

for i in range(100):
    final_list += random.choice(h_t)
       
print("Number of Heads: ", final_list.count("H"))
print("Number of Tails: ", final_list.count("T"))