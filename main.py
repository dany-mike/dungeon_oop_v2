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
        is_enter = input("Do you want to enter in the dungeon ?: 'y' 'n' ")
        if is_enter == 'y':
            print("YOU ENTER AND THE DOOR BEHIND YOU IS LOCKED ! YOU CANT LEAVE THE DUNGEON !!!")
            # Call user instance
            user = User(character_name, 100)
            # Call main entrance instance
            main_entrance = MainEntrance("Main entrance", "dungeon map", user)
            main_entrance.v_main_entrance()

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
