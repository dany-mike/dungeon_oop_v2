from User.User import User
from Rooms.MainEntrance import MainEntrance

while True:
    def main():
        print("Welcome in the dungeon game !")
        # Choose username
        character_name = input("Choose a character name: ")
        print("")
        # Call user instance
        user = User(character_name, 100)
        # Call main entrance instance
        main_entrance = MainEntrance("Main entrance", "dungeon map", user)
        main_entrance.v_main_entrance()

    if __name__ == '__main__':
        main()

    is_restart = input("Do you want to restart ?: (yes/no): ")
    if is_restart == 'yes':
        print("Let's restart !")
    else:
        print("Bye bye see you soon!")
        break
