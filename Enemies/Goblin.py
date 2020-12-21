from Png.Png import Png


class Goblin(Png):
    def __init__(self, name, pv):
        Png.__init__(self, name, pv)
        self.attack_name = "Punch and Kick"
        self.attack_domage = 30

    # Make an other attack the choice will be random
    def attack(self, user):
        print("")
        print(f"{self.name} uses the {self.attack_name} !")
        user.pv -= self.attack_domage
        print(f"{user.name} looses {self.attack_domage} PV !")
        print("")
