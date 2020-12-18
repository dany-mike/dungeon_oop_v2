from Rooms.Room import Room


class TrapRoom(Room):
    def __init__(self, room_name, user, arrow_attack):
        super().__init__(room_name)
        self.is_mini_boss_room_open = False
        self.is_trap_desactivate = False
        self.user = user
        self.arrow_attack = arrow_attack

    def trap_attack(self):
        print(f'No! there is a trap!!! {self.user.name} is attacked by arrows')
        while True:
            use_shield = input(f"Do you want to use your {self.user.inventory['hylian_shield_name']} ?: "
                               f"'yes' 'no' ")
            if use_shield == 'yes':
                # calculte User dommage
                protected_by_trap = (self.arrow_attack / 2)
                self.user.pv -= protected_by_trap
                print(f"{self.user.name} looses {protected_by_trap} PV !")
                # calculate shield dommages
                self.user.inventory["hylian_shield_pv"] -= protected_by_trap
                print(f"{self.user.inventory['hylian_shield_name']} looses {protected_by_trap} PV !")
                print(f"{self.user.inventory['hylian_shield_name']} has "
                      f"{self.user.inventory['hylian_shield_pv']} PV !")
                break
            # Not protect with shield
            if use_shield == 'no':
                self.user.pv -= self.arrow_attack
                print(f"{self.user.name} looses {self.arrow_attack} PV !")
                break
            else:
                print("Choose an existing choice")
            # Deactivate trap
        print("Seems the trap is deactivate...")
        self.is_trap_desactivate = True

    def v_trap_room(self):
        print(f"{self.user.name} enters in the {self.room_name}")
        self.trap_attack()
