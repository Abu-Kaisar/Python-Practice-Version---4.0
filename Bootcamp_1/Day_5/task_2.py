#File with Exception

fle = open("mydata2.txt", "w")
fle.write('''Oh damn
Oh yeah
Oh yeah
Oh yeah

It's been a long road but we're finally here (Ayyy)
And the view from the top so beautifully clear
We can see for forever not a cloud in the sky (Ayyy)
Picture perfect weather every day of our lives (Every day of our lives)

Just imagine if everything you wanted came true
Well it happened to me so it can happen to you
We're on a journey of truth and belief is the key (Aw)
So open up your heart and let ya light free''')
fle.close()

try:
    name_of_file = input("Please type the name of the file: ")
    fle = open(name_of_file + ".txt", "r")

except FileNotFoundError:
    print("{} not found in the directory....!!".format(name_of_file + ".txt"))

else:
    print(fle.read())
    
finally:
    fle.close()
    print("I will execute the command...")
    
    