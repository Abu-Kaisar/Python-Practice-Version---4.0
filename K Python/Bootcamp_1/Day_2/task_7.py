tree_row = int(input('How long the tree will be? = '))
load = 2 * tree_row - 1
for i in range(1, tree_row+1):
    tilda = (load - (2 *i -1)) / 2
    print("{}{}{}".format(" "*int(tilda), "#"*(2*i-1), " "*int(tilda)))
print("{}{}{}".format(" "*int((load - 1) / 2), "#", " "*int((load - 1) / 2)))


