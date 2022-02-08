cust_dict = {}
cust_list = []
c = 0
while True:
    code = input("Enter Customer :")
    if code[0].lower() == 'y':
        f_name, l_name = input("Enter Customer Name: ").split()
        cust_list.append(f_name)
        cust_list.append(l_name)
        strr = cust_list[0] + " " +cust_list[1]
        cust_list.clear()
        c += 1
        cust_dict[c] = strr
        
    elif code[0].lower() == 'n':
        break

for i in cust_dict.values():
    print(i)




