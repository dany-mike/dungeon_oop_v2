from Png.Png import Png
from Rooms.MainEntrance import MainEntrance


class User(Png):
    def __init__(self, name, pv):
        Png.__init__(self, name, pv)
        # User inventory
        self.inventory = {
            # Create a dynamic inventory later ex: I can choose my sword before the game etc:
            "red_potion": 30,
            "sword_name": "Excalibur",
            "sword_attack": 30,
            # if the shield is attacked by 100 he looses 50 pv
            "hylian_shield_name": "Hylian Shield",
            "hylian_shield_pv": 100,
        }

    # Enter in the dungeon
    def go_in_dungeon(self):
        while True:
            choice = input("Do you want to go in the dungeon ? ('yes' 'no'): ")
            if choice == 'yes':
                # Call the instance MainEntrance
                main_entrance = MainEntrance("dungeon main entrance", "dungeon map")
                print(f"{self.name} enters in the {main_entrance.room_name}")
                # User find a treasure
                main_entrance.main_entrance_reward()
                # Make reward into my inventory
                self.inventory["map"] = main_entrance.reward
                print(f"{self.inventory['map']} added in your inventary !")
                break
            if choice == 'no':
                print("Game over")
                break
            else:
                print("Choose an existing choice")

    def attack(self):
        pass

    def block_attack(self):
        pass


