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

    def attack(self, enemy):
        attack_choice = input("What do you want to do ? 'sword_attack' 'block_shield' ('magic_attack' -10PV )")
        if attack_choice == 'sword_attack':
            print()
        if attack_choice == 'block_shield':
            print()
        if attack_choice == 'magic_attack':
            print()

    def block_attack(self, attack):
        print(f"{self.name} uses his {self.inventory['hylian_shield_name']} !")
        # Mid of the attack on the shield
        self.inventory['hylian_shield_pv'] - (attack / 2)
        self.pv - (attack / 2)
        print(f"{self.inventory['hylian_shield_name']} has {self.inventory['hylian_shield_pv']} PV !")
        print(f"{self.name} has {self.pv} PV !")

    def take_potion(self):
        pass
