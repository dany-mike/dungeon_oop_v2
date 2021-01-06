from User.User import User
from Rooms.MainEntrance import MainEntrance
from Rooms.TrapRoom import TrapRoom
from Rooms.FightRoom import FightRoom
from Rooms.EmptyRoom import EmptyRoom
from Enemies.Goblin import Goblin


while True:
    def main():
        print("Welcome in the dungeon game !")
        # Choose username
        character_name = input("Choose a character name: ")
        print("")
        is_enter = input("Do you want to enter in the dungeon ?: 'y' 'n' ")
        if is_enter == 'y':
            # Blocked in the dungeon
            print("YOU ENTER AND THE DOOR BEHIND YOU IS LOCKED ! YOU CANT LEAVE THE DUNGEON !!!")
            # Call user instance
            user = User(character_name, 100)
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
            while True:
                is_exit_key = "ext_key" in user.inventory
                if is_exit_key:
                    print(f"{user.name} leave the dungeon with his {user.inventory['ext_key']} !")
                    print(f"He got {user.inventory['gold']} during his journey !!!")
                    print(f"Congratulation {user.name} you win the party !")
                    print()
                    print(f"SEE YOU LATER {user.name} !")
                    break

                print(f"{user.name} has {user.pv} PV.")
                user.take_potion()
                # Execute the method choose_direction
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
