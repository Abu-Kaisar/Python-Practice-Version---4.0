import random


multipyer_of_nine = [x for x in [random.randint(1,1001) for i in range(50)] if x % 9 == 0]

print(multipyer_of_nine)
