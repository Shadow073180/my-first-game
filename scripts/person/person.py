from ..weapon import Weapon 


class Person():

    def __init__(self, name, level, attributes, enhancements, class_type, attack, current_position_x, current_position_y, final_position):
        attributes = [stamina, armor, intellect]
        self.attributes = attributes
        enhancements = [critical_strike, haste, versatility]
        self.enhancements = enhancements
        class_type = [Druid, Warrior, Mage, Warlock, Hunter, Healer]
        self.position_x = position_x
        self.position_y = position_y
        self.final_position = final_position
        
        
    def move_forward(self, position_x, steps, position_y):
        self.steps = steps
        self.final_position = [self.position_x += self.steps , self.position_y]
        
    def move_back(self, self.position_x, steps):
        self.final_position = [self.position_x -= steps , self.position_y]

    def move_left(self,self.position_y, steps):
        self.final_position = [self.position_x, self.position_y -= steps]

    def move_right(self, self.position_y, steps):
        self.final_position = [self.position_x, self.position_y += steps]


    def defend(self):

    def equip_main_hand(self, weapon):
        self.weapon = weapon
        self.attack += weapon.attack

