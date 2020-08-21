from spell import Spell


class Spellbook():

    def __init__(self, slots_available = 10):
        self.slots_available = slots_available
        self.spells = []

    def add_spell(self, spell):
        for spell in self.spells:
            if spell.name == spell.name:
                return "Spell is already in spellbook."
            else:
                self.spells.append(spell)
                print(self.spells)
        