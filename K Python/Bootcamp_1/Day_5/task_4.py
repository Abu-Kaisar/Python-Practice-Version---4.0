import random

h_t = ["H", "T"]
final_list = []

for i in range(100):
    ap_key = random.choice(h_t)
    final_list.append(ap_key)
    
h = 0
t = 0

for i in final_list:
    if i == "H":
        h += 1
    elif i == "T":
        t += 1
        
print("Number of Heads: ", h)
print("Number of Tails: ", t)