from scripts.weapon import Weapon
from scripts.counter import Counter
import random
import time



class Player():

    def __init__(self, name, hp, class_type):
        self.name = name
        self.hp = hp
        self.class_type = class_type

    def attack(self, weapon, enemy):
        damage = random.randrange(0,weapon.attack)
        print(f"{self.name} hit {enemy.name} for {damage} hp.")
        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0
            return
        print(f"{enemy.name} has {enemy.hp} hp left.")
        
            
            
        


    
    


    