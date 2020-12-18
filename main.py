from User.User import User
from Rooms.MainEntrance import MainEntrance
from Rooms.TrapRoom import TrapRoom
from Rooms.FightRoom import FightRoom
from Rooms.EmptyRoom import EmptyRoom

while True:
    def main():
        print("Welcome in the dungeon game !")
        # Choose username
        character_name = input("Choose a character name: ")
        print("")
        while True:
            is_enter = input("Do you want to enter in the dungeon ?: 'y' 'n' ")
            if is_enter == 'y':
                # Blocked in the dungeon
                print("YOU ENTER AND THE DOOR BEHIND YOU IS LOCKED ! YOU CANT LEAVE THE DUNGEON !!!")
                # Call user instance
                user = User(character_name, 100)
                # Call main entrance instance
                main_entrance = MainEntrance("Main entrance", "dungeon map", user)
                direction = main_entrance.v_main_entrance()
                # Fight Room instance
                if direction == 'FR':
                    print("You are in the fight room")
                # Empty Room Instance
                if direction == 'EM':
                    print("You are in the empty room")
                # Trap Room instance
                if direction == "TR":
                    print("You are in the trap room")
                break
            if is_enter == 'n':
                print("Game over")
                break
            else:
                print("Choose an existing choice")


    if __name__ == '__main__':
        main()

    is_restart = input("Do you want to restart ?: (yes/no): ")
    if is_restart == 'yes':
        print("Let's restart !")
    else:
        print("Bye bye see you soon!")
        break
