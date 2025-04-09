from character import *

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)  # Boost health and attack power
        self.special_ability_a = "Quick Shot"
        self.special_ability_b = "Evade"

    def special(self, opponent):
        self.quick_shot(opponent)

    def special_b(self, opponent):
        self.evade()

    def quick_shot(self, opponent):
        '''Make two attacks at the foe'''
        print(f"{self.name} fires 2 arrows.")
        for i in range(2):
            super().attack(opponent)

    def evade(self):
        '''Triggers evasion to dodge the next attack'''
        print(f"{self.name} moves quickly to dodge.")
        self.evasion = True