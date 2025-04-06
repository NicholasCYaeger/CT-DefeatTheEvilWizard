from character import *

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)  # Boost health and attack power
        self.special_ability_a = "Quick Shot"
        self.special_ability_b = "Evade"
        self.evasion = False

    def special(self, opponent):
        self.quick_shot(opponent)

    def special_b(self, opponent):
        self.evade()

    def quick_shot(self, opponent):
        print(f"{self.name} fires 2 arrows.")
        for i in range(2):
            damage = opponent.take_damage(self.attack_power, 0.1)
            print(f"{self.name} shoots {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
                return

    # Add your QuickShot ability here

    def evasive_maneuvers(self):
        print(f"{self.name} moves quickly to dodge.")
        self.evasion = True
    # Add your Evade ability here

    def take_damage(self, base_attack_power, variance = 0.1):
        if(self.evasion):
            print(f"{self.name} evaded the attack")
            return 0
        else:
            damage = round(base_attack_power * random.uniform(1 - variance, 1 + variance))
            self.health -= damage
            return damage
