from Rooms.Room import Room
from Enemies.FireDragon import FireDragon
from Rooms.BossRoom import BossRoom
from Png.Inventory import Inventory


class EmptyRoom(Room):
    def __init__(self, room_name, user, typewriter):
        super().__init__(room_name, typewriter)
        self.user = user

    def v_empty_room(self):
        # Check if I have the boss key
        is_boss_key = "boss_key" in self.user.inventory
        inventory = Inventory(self.user)
        self.typewriter(f"{self.user.name} enters in the {self.room_name}")
        input("")
        print("")
        self.typewriter("There is a close door in the room")
        print("")
        if is_boss_key:
            while True:
                is_open = inventory.can_check_inventory("Do you want to open the door with your key ? 'I' 'y' 'n': ")
                if is_open == 'y':
                    self.open_door()
                    break
                if is_open == 'n':
                    print(f"{self.user.name} does not want to open the door")
                    break
                else:
                    print("Choose an existing choice")
        else:
            print("Seems you need a key to open this door !")

    def open_door(self):
        print(f"{self.user.name} uses {self.user.inventory['key']}")
        print(f"{self.user.name} opens the door")
        boss_room = BossRoom('Boss Room', self.user, '1 000 000 gold coin', self.typewriter)
        boss_room.v_boss_room(FireDragon(f"Fire Dragon", 100))

