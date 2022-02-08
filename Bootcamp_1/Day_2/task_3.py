dig_1 , sign, dig_2 = input("Enter Calclulation :").split()

dig_1 = int(dig_1)
dig_2 = int(dig_2)

if sign == '+':
    print("{} {} {} = {}".format(dig_1, sign, dig_2, dig_1 + dig_2))
    
elif sign == '-':
    print("{} {} {} = {}".format(dig_1, sign, dig_2, dig_1 - dig_2))
    
elif sign == '*':
    print("{} {} {} = {}".format(dig_1, sign, dig_2, dig_1 * dig_2))
    
elif sign == '/':
    print("{} {} {} = {}".format(dig_1, sign, dig_2, dig_1 / dig_2))

