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
        damage = random.randrange(0,self.attack_damage)
        print(f"{self.name} hits {player.name} for {damage} hp.")
        player.hp -= damage
        wait = True
        while wait == True:
            for i in range(self.attack_time):
                print(self.name + " has " + str(self.attack_time-i) + " seconds remaining \n")
                t.sleep(1)
                if i == 0:
                    wait = False
                else:
                    player.attack(player.weapon,self)
        if player.hp < 0:
            player.hp = 0
            return
        print(f"{player.name} has {player.hp} hp left.")
        
            
            



    
        