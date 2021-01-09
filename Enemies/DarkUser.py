from Enemies.Enemy import Enemy


class DarkUser(Enemy):
    def __init__(self, name, pv):
        Enemy.__init__(self, name, pv, attack_name='Dark sword_attack', attack_domage=15, weakness="Excalibur")

