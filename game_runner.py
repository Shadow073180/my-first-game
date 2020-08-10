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




def run_game(enemy, player, weapon):
    dead = False
    while dead == False:
        enemy.attack(player)
        enemy_current_hp = enemy.check_if_dead()
        if enemy_current_hp <= 0:
            dead == True
            print(f"{player.name} has killed {enemy.name}. Great Job.....GAME OVER!!")
            return
        
    
        player.attack(weapon, enemy)
        player_current_hp = player.check_if_dead()
        if player_current_hp <= 0:
            dead = True
            print(f"{enemy.name} has killed {player.name}. Better luck next time.....GAME OVER!!")
            return


run_game(enemy, player, weapon)



