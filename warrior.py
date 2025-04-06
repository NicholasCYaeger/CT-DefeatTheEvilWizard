from character import *
import random

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.exhaustion = 0
        self.special_ability_a = "Power Attack"

    def attack(self, opponent, variance=0.1):
        damage = opponent.take_damage(self.attack_power * (1 - self.exhaustion), variance)
        self.exhaustion /= 2
        if self.exhaustion < 0.1:
            self.exhaustion = 0
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        self.reduce_exhaustion()
        super().heal(self)

    def special(self, opponent):
        self.power_attack(opponent)

    def power_attack(self, opponent):
        damage = opponent.take_damage(
            self.attack_power * 2 * (1 - self.exhaustion), 0.1
        )
        self.exhaustion = 0.5
        print(f"{self.name} pushes themself, attacking {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    # Add your power attack method here
    
    def reduce_exhaustion(self):
        self.exhaustion /= 2
        if self.exhaustion < 0.1:
            self.exhaustion = 0
