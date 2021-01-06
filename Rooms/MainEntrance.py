from Rooms.Room import Room
from Png.Inventory import Inventory


class MainEntrance(Room):
    def __init__(self, room_name, reward, user):
        super().__init__(room_name)
        self.reward = reward
        self.user = user
        self.right_dir = 'TR'
        self.straight_dir = 'FR'
        self.left_dir = 'EM'

    def main_entrance_reward(self):
        print(f"Lucky day! you already find a treasure, its a {self.reward}")
        # Add dungeon map in user inventory
        print("")

    def v_main_entrance(self):
        print(f"{self.user.name} enters in the {self.room_name}")
        # User find a treasure
        self.main_entrance_reward()
        # Make reward into my inventory
        self.user.inventory["map"] = self.reward
        print(f"{self.user.inventory['map']} added in your inventary !")
        print("")
        print(f"You are at the {self.room_name}.")

    def choose_direction(self):
        inventory = Inventory(self.user)
        # Propose to take a potion if user has less than 100 PV
        return inventory.can_check_inventory_room_direction(f"In which room you want to go ?: 'I' "
                                                            f"'{self.straight_dir}' '{self.left_dir}' "
                                                            f"'{self.right_dir}': ")
