from Png.Png import Png
import colorama
from colorama import Fore
colorama.init()


class User(Png):
    def __init__(self, name, pv):
        Png.__init__(self, name, pv)
        # User inventory
        self.inventory = {
            # Create a dynamic inventory later ex: I can choose my sword before the game etc:
            "red_potion": 90,
            "sword_name": "Excalibur",
            "sword_attack": 30,
            'magic_attack': 50,
            # if the shield is attacked by 100 he looses 50 pv
            "hylian_shield_name": "Hylian Shield",
            "hylian_shield_pv": 100,
        }

    def attack(self, enemy):
        while True:
            print("")
            attack_choice = input("What do you want to do ? 'sword_attack' (-30PV: Enemy) 'magic_attack'(-50 PV: "
                                  "Enemy) (-10PV: User) 'I': "
                                  "")
            if attack_choice == 'sword_attack':
                # Sword attack
                print("")
                print(f"{self.name} uses the Sword Attack !")
                enemy.pv -= self.inventory['sword_attack']
                print(f"{enemy.name} looses {self.inventory['sword_attack']} PV !")
                break
            if attack_choice == 'magic_attack':
                # Magic attack
                print(f"{self.name} uses the Magic Attack !")
                enemy.pv -= self.inventory['magic_attack']
                print(f"{enemy.name} loose {self.inventory['magic_attack']} PV !")
                self.pv -= 10
                print(f"But {self.name} looses 10 PV")
                break
            # Add a protection attack
            if attack_choice == 'I':
                self.print_inventory()
            else:
                print("Choose an existing choice.")

    def block_trap_with_shield(self, attack):
        # calculte User dommage
        protected_by_trap = (attack / 2)
        self.pv -= protected_by_trap
        print(f"{self.name} looses {protected_by_trap} PV !")
        # calculate shield dommages
        self.inventory["hylian_shield_pv"] -= protected_by_trap
        print(f"{self.inventory['hylian_shield_name']} looses {protected_by_trap} PV !")
        print("")
        print(f"{self.inventory['hylian_shield_name']} has "
              f"{self.inventory['hylian_shield_pv']} PV !")

    def take_potion(self):
        # Check if the user has a potion or no.
        is_potion = "red_potion" in self.inventory
        if self.pv < 100 and is_potion:
            while True:
                is_use_potion = input(f"Do you want to use a potion to retrieve 90 PV ? 'I' 'y' 'n'")
                print("")
                if is_use_potion == 'y':
                    print(f"{self.name} takes a red potion")
                    self.pv += self.inventory["red_potion"]
                    # Make my pv at 100 if its above
                    if self.pv > 100:
                        self.pv = 100
                        print(f"{self.name} has {self.pv} PV")
                    self.inventory.pop("red_potion")
                    break
                if is_use_potion == 'n':
                    print(f"{self.name} does not use his potion...")
                    print("")
                    break
                if is_use_potion == 'I':
                    self.print_inventory()
                else:
                    print("Choose an exist choice.")

        if self.pv >= 100:
            print(f"{self.name} continues in the dungeon ...")

    def print_inventory(self):
        print('')
        print(Fore.BLUE + "\033[1m" + str(self.inventory) + "\033[0m")
        print('')
