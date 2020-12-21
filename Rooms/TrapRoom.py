from Rooms.Room import Room


class TrapRoom(Room):
    def __init__(self, room_name, user):
        super().__init__(room_name)
        self.is_mini_boss_room_open = False
        self.is_trap_desactivate = False
        self.user = user
        self.arrow_attack = 60

    def trap_attack(self):
        print(f'No! there is a trap!!! {self.user.name} is attacked by arrows')
        while True:
            use_shield = input(f"Do you want to use your {self.user.inventory['hylian_shield_name']} ?: "
                               f"'yes' 'no' ")
            if use_shield == 'yes':
                # Block the trap method
                self.user.block_trap_with_shield(self.arrow_attack)
                break

            if use_shield == 'no':
                # arrow_attack without shield
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
        if not self.is_trap_desactivate:
            self.trap_attack()
        if self.is_trap_desactivate:
            self.find_door()

    def find_door(self):
        # Check if user has a key if he has go to the Mini Boss Room.
        print(f"{self.user.name} goes at the door in the back of the room")
