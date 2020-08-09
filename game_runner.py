from scripts.bag import Bag
from scripts.enemy import Enemy
from scripts.player import Player
from scripts.weapon import Weapon
from scripts.spellbook import Spellbook
from scripts.spell import Spell

player = Player("David", 150, "Mage")
weapon = Weapon("staff", 30, 1, "common", "2-handed", 100, 2)
enemy = Enemy("Rockthar", 350, "Orc", 50)
david_spellbook = Spellbook(10)
inferno = Spell(50, 1.5, "Inferno", 1)


fighting = True

while fighting == True
    player.attack(weapon, enemy)
    if david.hp == 0:
        fighting = False
        print(f"{enemy.name} has killed {player.name}, GAME OVER!!!")
    elif enemy.hp == 0:
        fighting == False
        print(f"{player.name} is victorious. {enemy.name} has been destroyed!!")





