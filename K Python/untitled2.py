light_pkg = []
with open('E:/Kaisar/Python_ReVOLTED_V_4.0/K Python/TensorFlow.txt', "r") as tfd:
    for x in tfd:
        light_pkg.append(x.split()[0])


final = []
for i in light_pkg:
    if i not in final:
        final.append(i)

#print(", ".join(final))
in_pkg = []
with open('E:/Kaisar/Python_ReVOLTED_V_4.0/K Python/kol.txt', "r") as sss:
    for x in sss:
        in_pkg.append(x.split()[0])

print("-----------------------------")
for i in final:
    if i not in in_pkg:
        print(i)
    
    
