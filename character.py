import math
import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.special_ability_a = "Default A"
        self.special_ability_b = "Default B"
        self.heal_base = 0.5
        self.heal_count = 0
        self.heal_max = 6

    def attack(self, opponent, variance = 0.1):
        damage = opponent.take_damage(self.attack_power)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def heal(self, variance=0.1):
        base_heal_value = round(
            (
                (self.max_health * self.heal_base)
                * (1 - min(1, self.heal_count / self.heal_max))
            )
            * random.uniform(1 - variance, 1 + variance)
        )
        unhealed_damage = self.max_health - self.health
        heal_value = min(base_heal_value, unhealed_damage)
        self.heal_count += 1
        self.health += heal_value
        print(
            f"{self.name} recovers {heal_value} health! ({self.health}/{self.max_health})"
        )

    def special(self, opponent):
        print("Basic Character doesn't have a special A")

    def special_b(self, opponent):
        print("Basic Character doesn't have a special B")

    def take_damage(self, base_attack_power, variance = 0.1):
        damage = round(base_attack_power * random.uniform(1 - variance, 1 + variance))
        self.health -= damage
        return damage
