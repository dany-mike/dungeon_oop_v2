from Enemies.Enemy import Enemy


class Goblin(Enemy):
    def __init__(self, name, pv):
        Enemy.__init__(self, name, pv, attack_name="Punch and Kick", attack_domage=30, weakness="Fire Sword")
