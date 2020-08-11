from scripts.bag import Bag
from scripts.enemy import Enemy
from scripts.player import Player
from scripts.weapon import Weapon
from scripts.spellbook import Spellbook
from scripts.spell import Spell
import time

player = Player("David", 150, "Mage")
weapon = Weapon("Flame Staff of the Phoenix","staff", 100, 1, "common", "2-handed", 100, 3)
enemy = Enemy("Rockthar", 200, "Orc", 25, 1)
david_spellbook = Spellbook(10)
inferno = Spell(50, 1.5, "Inferno", 1, 10)


run = True
while run == True:
    if player.hp <= 0:
        run = False
        print(f"{player.name} has been killed by {enemy.name}. Game Over!!")
    else:
        player.attack(weapon, enemy)
    if enemy.hp <= 0:
        run = False
        print(f"{player.name} has killed {enemy.name} Awesome job! Game Over!!")
    else:
        enemy.attack(player)




