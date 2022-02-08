dig_1, dig_2 = map(int, input("Type digits to calculate...  ").split())

add = dig_1 + dig_2
diff = dig_1 - dig_2
prod = dig_1 * dig_2
divi = dig_1 / dig_2
rem = dig_1 % dig_2


print("The Addition -- {} + {} = {}".format(dig_1, dig_2, add))
print("The Addition -- {} - {} = {}".format(dig_1, dig_2, diff))
print("The Addition -- {} * {} = {}".format(dig_1, dig_2, prod))
print("The Addition -- {} / {} = {}".format(dig_1, dig_2, divi))
print("The Addition -- {} % {} = {}".format(dig_1, dig_2, rem))
