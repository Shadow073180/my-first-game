from weapon import Weapon
import random
import time



class Player():

    def __init__(self, name, hp, class_type):
        self.name = name
        self.hp = hp
        self.class_type = class_type

    def attack(self, weapon, enemy):
        weapon = weapon.name
        enemy = enemy.name
        damage = random.random(range(0,weapon.attack))
        enemy.hp -= damage
        time.sleep(weapon.attack_time)
        


    
    


    