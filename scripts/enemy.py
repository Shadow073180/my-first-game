from scripts.player import Player
import random
import time as t




class Enemy():

    def __init__(self, name, hp, type, attack_damage, attack_time):
        self.name = name
        self.hp = hp
        self.type = type
        self.attack_damage = attack_damage
        self.attack_time = attack_time
       

    def attack(self, player):
        if self.hp <= .10 * self.hp:
            damage = random.randrange(10,self.attack_damage)
            print("Ultra ATTACK!")
        else:
            damage = random.randrange(0,self.attack_damage)
        print(f"{self.name} hits {player.name} for {damage} hp.")
        player.hp -= damage
        if self.attack_time > 1:
            wait = True
            while wait == True:
                for i in range(self.attack_time):
                    print(self.name + " has " + str(self.attack_time-i) + " seconds remaining \n")
                    t.sleep(1)
                    if i == 0:
                        wait = False
                    else:
                        player.attack(player.weapon,self)
        print(f"{player.name} has {player.hp} hp left.")

    def check_if_dead(self):
        return self.hp
        
        

        
        
            
    



    
        