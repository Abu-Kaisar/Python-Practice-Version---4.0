import random
import math
class Warrior:
    def __init__(self, name="warrior", health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max
    def attack(self):
        attk_amt = self.attk_max * (random.random() + .5)
        return attk_amt
    def block(self):
        block_amt = self.block_max * (random.random() + .5)
        return block_amt
class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
    def get_attack_result(self, warriorA, warriorB):
        warriorA_attk_to_b = warriorA.attack()
        warriorB_block_to_a = warriorB.block()
        dmg_to_warriorB = math.ceil(warriorA_attk_to_b - warriorB_block_to_a )
        warriorB.health = warriorB.health - dmg_to_warriorB
        print("{} attks {} deals {} damages...!!!".format(warriorA.name, warriorB.name, dmg_to_warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0 :
            print("{} has Died and {} is Victorious!!!!!!!".format(warriorB, warriorA))
            return "Game Over"
        else:
            return "Fight Again"      
def main():
    shanto = Warrior("Shanto", 50, 20, 10)
    bhuchu = Warrior("Bhuchu", 50, 20, 10)
    war = Battle()
    war.get_attack_result(shanto, bhuchu)
main()

def main():
     thor = Warrior("Thor", 50, 20, 10)
     loki = Warrior("Loki", 50, 20, 10)
     battle = Battle()
     battle.start_fight(thor, loki)
main()