my_string = "Lola Tin Bola. Kal Cholas!"

print(my_string)
print("Length =", len(my_string))
print("any letter in index =", my_string[5])
print("last letter in index =", my_string[-1])
print("slice in n:m =", my_string[5: 12])
print("n to last index =", my_string[5:])
print("first to m index =", my_string[:12])
print("Every Other Letter =", my_string[0:-1:2])
print("Reverse String =", my_string[::-1])

print("{} is in unicode {}".format(my_string[5], ord(my_string[5])))
print("65 to Unicode code = {}".format(chr(65)))
