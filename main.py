from Png.Inventory import Inventory
from Rooms.EmptyRoom import EmptyRoom
from Rooms.FightRoom import FightRoom
from Rooms.MainEntrance import MainEntrance
from Rooms.TrapRoom import TrapRoom
from User.User import User
from tools import typewriter, message, user_choose_name, in_dungeon


while True:
    def main():
        typewriter(message)
        print("")
        print("")
        # Choose username
        character_name = user_choose_name()
        print('')
        user = User(character_name, 100)
        inventory = Inventory(user)
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
            # User in dungeon
            in_dungeon(user, main_entrance, fight_room, empty_room, trap_room)

    if __name__ == '__main__':
        main()

    is_restart = input("Do you want to restart ?: (yes/no): ")
    if is_restart == 'yes':
        print("Let's restart !")
    else:
        print("Bye bye see you soon!")
        break

