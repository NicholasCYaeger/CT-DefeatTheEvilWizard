from character import *

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=10)  # Lower attack power
        self.pressure = 0
        self.crit_chance = 0.1

    def start_turn(self):
        self.pressure += 5
        print(f"{self.name} applies pressure: {self.pressure + self.attack_power}")
        super().start_turn()

    def attack(self, opponent, variance = 0.1, accuracy = 0.9, damage_bonus_percentage = 0):
        '''Overwritten to account for the Evil Wizard's critical hits'''
        if opponent.evasion:
            print(f"{opponent.name} evades {self.name}'s attack")
            opponent.evasion = False
            return
        if random.random() >= accuracy:
            print(f"{self.name} swings at {opponent.name} but misses")
            return
        crit_bonus = 0
        if random.random() < self.crit_chance:
            crit_bonus = 1
        damage = opponent.take_damage(self.attack_power + self.pressure, variance, damage_bonus_percentage + crit_bonus)
        if crit_bonus == 0:
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {opponent.name} critically for {damage} damage!")

    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
