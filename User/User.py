from Png.Png import Png
from Rooms.MainEntrance import MainEntrance
from Enemies.Goblin import Goblin

class User(Png):
    def __init__(self, name, pv):
        Png.__init__(self, name, pv)
        # User inventory
        self.inventory = {
            # Create a dynamic inventory later ex: I can choose my sword before the game etc:
            "red_potion": 30,
            "sword_name": "Excalibur",
            "sword_attack": 30,
            'magic_attack': 50,
            # if the shield is attacked by 100 he looses 50 pv
            "hylian_shield_name": "Hylian Shield",
            "hylian_shield_pv": 100,
        }

    def attack(self, enemy):
        print("")
        attack_choice = input("What do you want to do ? 'sword_attack' 'magic_attack' (-10PV): "
                              "")
        if attack_choice == 'sword_attack':
            print("")
            print(f"{self.name} uses the Sword Attack !")
            enemy.pv -= self.inventory['sword_attack']
            print(f"{enemy.name} looses {self.inventory['sword_attack']} PV !")
        if attack_choice == 'magic_attack':
            print(f"{self.name} uses the Magic Attack !")
            enemy.pv -= self.inventory['magic_attack']
            print(f"{enemy.name} loose {self.inventory['magic_attack']} PV !")
            self.pv -= 10
            print(f"But {self.name} looses 10 PV")


    def take_potion(self):
        pass
