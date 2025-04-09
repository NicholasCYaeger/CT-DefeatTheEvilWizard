from character import *
import random

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
        self.exhaustion = 0
        self.parrying = False
        self.special_ability_a = "Power Attack"
        self.special_ability_b = "Parrying Attack"

    def attack(self, opponent, variance=0.1, accuracy=0.9, damage_bonus_percentage = 0):    #overwrite attack(s,o,v,a,d)
        '''Overwrite attack to use exhaustion.'''
        prior_exhaustion = self.exhaustion
        if random.random() >= accuracy:
            print(f"{self.name} swings at {opponent.name} but misses")
            return
        self.reduce_exhaustion()
        super().attack(opponent, variance, 1, damage_bonus_percentage-prior_exhaustion)     #I have checked for accuracy once already

    def heal(self):                                                                         #overwrite heal(s)
        '''Overwrite heal to reduce exhaustion twice when used'''
        self.reduce_exhaustion()
        self.reduce_exhaustion()
        super().heal()

    def special(self, opponent):
        self.power_attack(opponent)

    def special_b(self, opponent):
        self.parrying_attack(opponent)

    def power_attack(self, opponent):                                                       
        '''A special attack that deals double damage, but grants exhaustion to the warrior.'''
        damage = opponent.take_damage(                                                      
            self.attack_power * 2 * (1 - self.exhaustion), 0.1
        )
        self.exhaustion = min(self.exhaustion + 0.25, 0.75)
        print(f"{self.name} pushes themself, attacking {opponent.name} for {damage} damage! (Exhaustion @ {self.exhaustion})")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def parrying_attack(self, opponent):                                                    
        '''A special attack that deals reduced damage, but halves the damage taken next time the Warrior is attacked'''
        self.parrying = True                                                                
        print(f"{self.name} swings their weapon defensively.")
        self.attack(opponent, damage_bonus_percentage = -0.25)

    def reduce_exhaustion(self):                                                            
        '''Reduce exhaustion by half. If exhaustion is < 0.1, reduce it to 0 instead'''
        if self.exhaustion > 0:                                                             
            self.exhaustion /= 2
            if self.exhaustion < 0.1:
                self.exhaustion = 0
            print(f"Exhaustion reduced to {self.exhaustion}.")

    def take_damage(self, base_attack_power, variance=0.1, damage_bonus_percentage=0):
        '''Overwrite taking damage to use parry'''
        if self.parrying:
            damage_bonus_percentage -= 0.5
            self.parrying = False
            print(f"{self.name} is parrying.")
        return super().take_damage(base_attack_power, variance, damage_bonus_percentage)
