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

    def attack(self):
        pass

    def block_attack(self):
        pass

    def take_potion(self):
        pass
