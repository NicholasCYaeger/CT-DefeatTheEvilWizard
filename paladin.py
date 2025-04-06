from character import *

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.special_ability_a = "Holy Strike"
        self.special_ability_b = "Divine Shield"
        self.divine_shield = 0

    def special(self, opponent):
        self.holy_strike(opponent)
    
    def special_b(self, opponent):
        self.divine_shield(self) 

    def holy_strike(self, opponent):
        pass

    def divine_shield(self):
        self.divine_shield = 1
        print(f"{self.name} protects themself in holy light.")

    def take_damage(self, base_attack_power, variance=0.1):
        base_damage = base_attack_power * random.uniform(1 - variance, 1 + variance)
        protection = round(base_damage * self.divine_shield)
        if protection > 0:
            print(f"{self.name}'s divine shield blocks {protection} damage")
        damage = round(base_damage - protection)
        self.divine_shield /= 2
        self.health -= damage
        return damage

    # Add your Holy Strike here

    # Add your Divine Shield here
