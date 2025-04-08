from character import *

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
        self.special_ability_a = "Burning Spell"
        self.special_ability_b = "Sleep Spell"

    def special(self, opponent):
        self.burning_spell(opponent)

    def special_b(self, opponent):
        self.sleep_spell(opponent)

    def sleep_spell(self, opponent):
        if random.random() < 0.5:
            opponent.awake = False
            print(f"{opponent.name} passed out asleep.")
        else:
            print(f"{opponent.name} pushes themself to stay awake through the spell.")

    # Add your cast spell method here
