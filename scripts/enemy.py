import random
import time




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
        if player.hp < 0:
            player.hp = 0
            return
        print(f"{player.name} has {player.hp} hp left.")
        time.sleep(self.attack_time)


    
        