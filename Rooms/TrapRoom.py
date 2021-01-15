from Rooms.Room import Room
from Rooms.MiniBossRoom import MiniBossRoom
from Enemies.DarkUser import DarkUser
from Png.Inventory import Inventory


class TrapRoom(Room):
    def __init__(self, room_name, user, typewriter):
        super().__init__(room_name, typewriter)
        self.is_mini_boss_room_open = False
        self.is_trap_desactivate = False
        self.user = user
        self.arrow_attack = 60
        # boolean below into MiniBossRoom.py
        self.is_dark_user = True

    def trap_attack(self):
        print(f'No! there is a trap!!! {self.user.name} is attacked by arrows')
        inventory = Inventory(self.user)
        while True:
            use_shield = inventory.can_check_inventory(f"Do you want to use your "
                                                       f"{self.user.inventory['hylian_shield_name']}"
                                                       f" ?: 'I' "f"'y' 'n' ")
            if use_shield == 'y':
                # Block the trap method
                self.user.block_trap_with_shield(self.arrow_attack)
                break

            if use_shield == 'n':
                # arrow_attack without shield
                self.user.pv -= self.arrow_attack
                print("")
                print(f"{self.user.name} looses {self.arrow_attack} PV !")
                print("")
                break
            else:
                print("Choose an existing choice")
            # Deactivate trap
        print("The trap is deactivate...")
        self.is_trap_desactivate = True

    def v_trap_room(self):
        self.typewriter(f"{self.user.name} enters in the {self.room_name}")
        input("")
        if not self.is_trap_desactivate:
            self.trap_attack()
            if self.user.pv == 0:
                print("Arrows killed you !")

        if self.user.pv > 0:
            if self.is_trap_desactivate and self.is_mini_boss_room_open == False:
                self.find_door()
            else:
                print("There is nothing to do here")

    # Something to do for optimisation with this func (not deadend room)
    def find_door(self):
        # Check if user has a key if he has go to the Mini Boss Room.
        is_key = "key" in self.user.inventory
        if not is_key:
            print(f"{self.user.name} goes at the door in the back of the room but she is closed you need a key ....")
            print("")
            print(f"{self.user.name} goes back at the main entrance ....")
            print("")
        if is_key:
            self.is_mini_boss_room_open = True
            self.open_door()

    def open_door(self):
        inventory = Inventory(self.user)

        while True:
            use_key = inventory.can_check_inventory("Do you want to use your key ? 'I' 'y' 'n' ")

            if use_key == 'y':
                # Create an enemy wich is in the same state of my user
                print(f"{self.user.name} uses {self.user.inventory['key']}")
                mini_boss_room = MiniBossRoom('Mini Boss Room', self.user, 'boss key', self.is_dark_user,
                                              self.typewriter)
                mini_boss_room.v_mini_boss_room(DarkUser(f"Dark {self.user.name}", self.user.pv))
                break
            if use_key == 'n':
                print(f"{self.user.name} decides to do nothing. He goes back at the main entrance....")
            else:
                print("Choose an existing choice")

    @staticmethod
    def lose_fight(user):
        print("")
        print(f"{user.name} looe the fight :( ")
        print("you lose all your inventory :( ")
