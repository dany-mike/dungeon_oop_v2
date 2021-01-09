from Enemies.Enemy import Enemy


class FireDragon(Enemy):
    def __init__(self, name, pv):
        Enemy.__init__(self, name, pv, attack_name="Fireball", attack_domage=50, weakness="Royal Sword")
