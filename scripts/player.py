from scripts.weapon import Weapon
import random
import time as t



class Player():

    def __init__(self, name, hp, class_type):
        self.name = name
        self.hp = hp
        self.class_type = class_type
        

    def attack(self, weapon, enemy):
        damage = random.randrange(0,weapon.attack)
        print(f"{self.name} hit {enemy.name} for {damage} hp.")
        enemy.hp -= damage
        wait = True
        while wait == True:
            for i in range(weapon.attack_time):
                print(self.name + " has " + str(weapon.attack_time-i) + " seconds remaining \n")
                t.sleep(1)
                if i == 0:
                    wait = False
                else:
                    enemy.attack(self)
        if enemy.hp < 0:
            enemy.hp = 0
            return
        print(f"{enemy.name} has {enemy.hp} hp left.")
        
            
            
        


    
    


    