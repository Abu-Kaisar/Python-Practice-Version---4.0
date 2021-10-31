# Class And Object

class Dog():
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("{} Eat it Now! Delicious Meat".format(self.name))
        
    def bark(self):
        print("{} Barks!!! Bouk Bouk".format(self.name))
        
        

def main():
    Pipo = Dog("Pipo", 55, 26)
    print("Dog Height {}...\nDog Wight {}".format(Pipo.height, Pipo.weight))
    Pipo.eat()
    Pipo.bark()

main()