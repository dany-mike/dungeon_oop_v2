from Rooms.Room import Room


class MainEntrance(Room):
    def __init__(self, room_name, reward):
        super().__init__(room_name)
        self.reward = reward

    def main_entrance_reward(self):
        print(f"Lucky day! you already find a treasure, its a {self.reward}")
        # Add dungeon map in user inventory
        print("")
