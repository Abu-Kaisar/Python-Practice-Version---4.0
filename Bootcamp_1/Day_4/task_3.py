# Fighting Simulation
# Class And Object

import math
import random


class Warrior():
    def __init__(self, name="Warrior", health_max=0, attack_max=0, block_max=0, heal_max=0, endu_max=0):
        self.name = name
        self.health_max = health_max
        self.attack_max = attack_max
        self.block_max = block_max
        self.heal_max = heal_max
        self.endu_max = endu_max
        
    def attack(self):
        attack_amount = self.attack_max * (random.random() + 0.125)
        return attack_amount
    def block(self):
        block_amount = self.block_max * (random.random() + 0.125)
        return block_amount
    def heal(self):
        heal_amount = self.heal_max * (random.random() + 0.5)
        return heal_amount
    

class Battle_Pass():
    def start_fight(self, warrior_1, warrior_2):
        while True:
            if self.get_death_match(warrior_1, warrior_2) == "Match Finished":
                break
            if self.get_death_match(warrior_2, warrior_1) == "Match Finished":
                break
        
    def get_death_match(self, warrior_A, warrior_B):
        warrior_A_attack_to_b = warrior_A.attack()
        warrior_B_block_to_a = warrior_B.block()
        warrior_B.endu_max += 1
        warrior_B_heal_to_attack_of_a = 0
        if warrior_B.endu_max % 3 == 0:
            warrior_B_heal_to_attack_of_a = math.ceil(warrior_B.heal())
        dmg_to_warrior_b = math.ceil(warrior_A_attack_to_b - warrior_B_block_to_a )
        warrior_B.health_max = warrior_B.health_max - dmg_to_warrior_b + warrior_B_heal_to_attack_of_a
            
        print("{} attacks {} deals {} damages...!!!".format(warrior_A.name, warrior_B.name, dmg_to_warrior_b))
        print("{} is down to {} health".format(warrior_B.name, warrior_B.health_max))
        print("{} heals {} HP.........".format(warrior_B.name, warrior_B_heal_to_attack_of_a))
            
        if warrior_B.health_max <= 0 :
            print("{} has Died and {} is Victorious!!!!!!!".format(warrior_B.name, warrior_A.name))
            return "Match Finished"
        else:
            return "Fight Again"
            
            
def main():
    shanto = Warrior("Shanto", 100, 30, 20, 10, 0)
    bhuchu = Warrior("Bhuchu", 100, 30, 20, 10, 0)
    war = Battle_Pass()
    war.start_fight(shanto, bhuchu)
        

main()
    