from character import *

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.special_ability_a = "Holy Strike"
        self.special_ability_b = "Divine Shield"
        self.divine_shield = False

    def special(self, opponent):
        self.holy_strike(opponent)
    
    def special_b(self, opponent):
        self.divine_shield(self) 

    def holy_strike(self, opponent):
        '''A special attack that deals +25% damage and doesn't miss.'''
        damage = opponent.take_damage(self.attack_power, damage_bonus_percentage = 0.25) #Skip accuracy check
        print(f"{self.name} strikes true at {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        '''A shield that makes sure that the next attack deals no damage'''
        self.divine_shield = True
        print(f"{self.name} protects themself in holy light.")

    def take_damage(self, base_attack_power, variance=0.1):
        '''Overwritten to account for Divine Shield'''
        if self.divine_shield:
            print(f"{self.name}'s divine shield blocks all damage")
            self.divine_shield = False
            return 0
        super().take_damage(base_attack_power, variance)