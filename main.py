import sys
import time

from Enemies.Goblin import Goblin
from Png.Inventory import Inventory
from Rooms.EmptyRoom import EmptyRoom
from Rooms.FightRoom import FightRoom
from Rooms.MainEntrance import MainEntrance
from Rooms.TrapRoom import TrapRoom
from User.User import User


def typewriter(welcome_message):
    for char in welcome_message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


message = "- Welcome in the dungeon game \n\
 - Type 'I' to open your inventory- \n\
  If you want to select an object type the object_name"


while True:
    def main():
        typewriter(message)
        print("")
        print("")
        # Choose username
        while True:
            character_name = input("Choose a character name: ")
            if character_name == "":
                print("You have to choose a name")
            else:
                print('')
                user = User(character_name, 100)
                inventory = Inventory(user)
                break
        is_enter = inventory.can_check_inventory("Do you want to enter in the dungeon ? 'I': : 'y' 'n' ")
        print("")

        if is_enter == 'y':
            # Blocked in the dungeon
            print("YOU ENTER AND THE DOOR BEHIND YOU IS LOCKED ! YOU CANT LEAVE THE DUNGEON !!!")
            print("")
            # Call main entrance instance
            main_entrance = MainEntrance("Main entrance", "dungeon map", user)
            # Call TrapRoom instance
            trap_room = TrapRoom("Trap Room", user)
            # Fight Room instance
            fight_room = FightRoom("Fight Room", user, "key")
            # Empty room instance
            empty_room = EmptyRoom("Empty Room", user)
            # Execute the method v_main_entrance
            main_entrance.v_main_entrance()

            # Possibility to win the game
            while True:
                is_exit_key = "ext_key" in user.inventory
                if is_exit_key:
                    print(f"{user.name} leave the dungeon with his {user.inventory['ext_key']} !")
                    print(f"He got {user.inventory['gold']} during his journey !!!")
                    print(f"Congratulation {user.name} you win the party !")
                    print()
                    print(f"SEE YOU LATER {user.name} !")
                    break

                print("")
                print(f"{user.name} has {user.pv} PV.")
                # Execute the method choose_direction
                print("")
                direction = main_entrance.choose_direction()
                print("")
                if direction == 'FR':
                    fight_room.v_fight_room(Goblin("Goblin", 50))
                    if user.pv <= 0:
                        print("Game over")
                        break
                if direction == 'EM':
                    # Empty Room Instance
                    empty_room.v_empty_room()
                    if user.pv <= 0:
                        print("Game over")
                        break
                if direction == "TR":
                    # Trap Room instance
                    trap_room.v_trap_room()
                    if user.pv <= 0:
                        print("Game over")
                        break
        else:
            print("Game over")


    if __name__ == '__main__':
        main()

    is_restart = input("Do you want to restart ?: (yes/no): ")
    if is_restart == 'yes':
        print("Let's restart !")
    else:
        print("Bye bye see you soon!")
        break
