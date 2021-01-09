from Png.Png import Png


class Enemy(Png):
    def __init__(self, name, pv, attack_name, attack_domage, weakness):
        Png.__init__(self, name, pv)
        self.attack_name = attack_name
        self.attack_domage = attack_domage
        self.weakness = weakness

    def attack(self, user):
        print("")
        print(f"{self.name} uses the {self.attack_name} !")
        user.pv -= self.attack_domage
        print(f"{user.name} looses {self.attack_domage} PV !")
        print("")
