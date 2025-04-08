from character import *
from warrior import *
from mage import *
from paladin import *
from archer import *
from evil_wizard import *

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        total_actions = 0
        print("\n--- Your Turn ---")
        print("1. Attack")
        print(f"2. {player.special_ability_a}")
        print(f"3. {player.special_ability_b}")
        print("4. Heal")
        print("5. View Stats")

        try:
            choice = int(input("Choose an action: "))

            if choice == 1:
                player.attack(wizard)
            elif choice == 2:
                player.special(wizard)
            elif choice == 3:
                player.special_b(wizard)
            elif choice == 4:
                player.heal()
            elif choice == 5:
                player.display_stats()
                continue
            else:
                print("Invalid choice, try again.")
                continue
        except:
            print("Invalid choice, input a number.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.start_turn()
            if wizard.health > 0:
                if wizard.awake:
                    wizard.regenerate()
                    wizard.attack(player)
                elif random.random() < 0.5:
                    wizard.awake = True
                    print(f"{wizard.name} has woken up.")
                else:
                    print(f"{wizard.name} is still asleep.")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)


if __name__ == "__main__":
    main()
