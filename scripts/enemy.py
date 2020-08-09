import random




class Enemy():

    def __init__(self, name, hp, type, attack_damage):
        self.name = name
        self.hp = hp
        self.type = type
        self.attack_damage = attack_damage

    def attack(self, weapon, player):
        weapon = weapon.name
        player = player.name
        damage = random.random(range(0,self.attack_damage))
        player.hp -= damage

    
        