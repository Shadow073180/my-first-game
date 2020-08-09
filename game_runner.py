from scripts.bag import Bag
from scripts.enemy import Enemy
from scripts.player import Player
from scripts.weapon import Weapon
from scripts.spellbook import Spellbook
from scripts.spell import Spell
import time

player = Player("David", 150, "Mage")
weapon = Weapon("Flame Staff of the Phoenix","staff", 100, 1, "common", "2-handed", 100, 5)
enemy = Enemy("Rockthar", 200, "Orc", 25, 1)
david_spellbook = Spellbook(10)
inferno = Spell(50, 1.5, "Inferno", 1, 10)


fighting = True

while fighting == True:
    enemy.attack(player)
    player.attack(weapon, enemy)
    if player.hp <= 0:
        fighting = False
        print(f"{enemy.name} has killed {player.name}, GAME OVER!!!")
        
    elif enemy.hp <= 0:
        fighting = False
        print(f"{player.name} is victorious. {enemy.name} has been destroyed!!")
        




