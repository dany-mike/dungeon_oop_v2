from Png.Png import Png


class Goblin(Png):
    def __init__(self, name, pv, weapon_name, weapon_attack):
        Png.__init__(self, name, pv, weapon_name, weapon_attack)

    def attack(self):
        pass
