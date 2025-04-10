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
        self.heal_base = 0.75
        self.heal_count = 0
        self.heal_max = 6
        self.awake = True
        self.burning = 0
        self.evasion = False

    def start_turn(self):
        '''Check things that happen at the start of turn (fire damage)'''
        print(f"{self.name} starts their turn.")
        if self.burning > 0:
            fire_damage = self.take_damage(self.burning, 0, 0)
            print(f"{self.name}'s burning clothing deals {fire_damage} damage.")
            if self.health <= 0:
                print(f"{self.name} has been defeated by fire!")
            self.burning = math.floor(self.burning / 2)
            if self.burning == 0:
                print(f"The fire on {self.name}'s clothing is put out.")

    def attack(self, opponent, variance = 0.1, accuracy = 0.9, damage_bonus_percentage = 0):
        '''Make a simple attack. Varies by variance up or down. Has chance of hitting by accuracy (/1). 
           The damage increases by the damage_bonus_percentage (*[1+dbp]). 
           Also allows for evade (Archer Ability) to make the next attack miss (no check)'''
        if opponent.evasion:
            print(f"{opponent.name} evades {self.name}'s attack")
            opponent.evasion = False
            return
        if random.random() >= accuracy:
            print(f"{self.name} swings at {opponent.name} but misses")
            return
        damage = opponent.take_damage(self.attack_power, damage_bonus_percentage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        '''Display current player's Health and Attack Power'''
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )

    def heal(self):
        '''Recover health. Starts at 75% of max health, but reduces by 1/6 each use. Don't heal over damage taken'''
        base_heal_value = round(
            (
                (self.max_health * self.heal_base)
                * (1 - min(1, self.heal_count / self.heal_max))
            )
        )
        unhealed_damage = self.max_health - self.health
        heal_value = min(base_heal_value, unhealed_damage)
        self.heal_count += 1
        self.health += heal_value
        print(
            f"{self.name} recovers {heal_value} health! ({self.health}/{self.max_health})"
        )

    def special(self, opponent):
        '''First special ability'''
        print("Basic Character doesn't have a special A")

    def special_b(self, opponent):
        """Second special ability"""
        print("Basic Character doesn't have a special B")

    def take_damage(self, base_attack_power, variance = 0.1, damage_bonus_percentage = 0):
        '''Take damage (times 1 plus or minus up to variance either way), wake up, and return damage value'''
        damage = round(base_attack_power * random.uniform(1 - variance, 1 + variance) * (damage_bonus_percentage + 1))
        if damage > 0 and not self.awake:
            self.awake = True
        self.health -= damage
        return damage
