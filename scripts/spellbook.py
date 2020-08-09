from scripts.spell import Spell


class Spellbook():

    def __init__(self, slots_available = 10):
        self.slots_available = slots_available
        self.spells = []

    def add_spell_to_spellbook(self, spell):
        self.slots_available -= 1
        spell = spell.name
        self.spells.append(spell.name)

        