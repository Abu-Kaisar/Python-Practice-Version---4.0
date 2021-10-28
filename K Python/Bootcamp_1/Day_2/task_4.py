numb = int(input("Tell Your Age :"))

if numb < 5 :
    print("Too Young for Everything....")
elif numb == 5:
    print("Go to Kindergarten..")
    
elif numb >= 6 and numb <= 17:
    print("Go to Grade {}..".format(numb - 5))
    
elif numb > 17:
    print("Go to College..")
