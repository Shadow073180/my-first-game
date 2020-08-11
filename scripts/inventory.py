from scripts import *



class Inventory():

    def __init__(self, head = None, shoulders = None, back = None, waist = None, bracers = None, hands = None, legs = None, feet = None, ring1 = None, ring2 = None, trinket1 = None, trinket2 = None, main_hand = None, off_hand = None):
        self.head = head
        self.shoulders = shoulders
        self.back = back
        self.waist = waist
        self.bracers = bracers 
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.ring1 = ring1
        self.ring2 = ring2
        self.trinket1 = trinket1
        self.trinket2 = trinket2
        self.main_hand  = main_hand
        self.off_hand = off_hand
        self.inventory = {}

    def add_item_to_inventory(self):
        pass

        
        