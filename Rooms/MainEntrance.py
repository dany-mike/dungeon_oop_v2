from Rooms.Room import Room


class MainEntrance(Room):
    def __init__(self, room_name, reward, user):
        super().__init__(room_name)
        self.reward = reward
        self.user = user

    def main_entrance_reward(self):
        print(f"Lucky day! you already find a treasure, its a {self.reward}")
        # Add dungeon map in user inventory
        print("")

    def v_main_entrance(self):
        # Call the instance MainEntrance
        print(f"{self.user.name} enters in the {self.room_name}")
        # User find a treasure
        self.main_entrance_reward()
        # Make reward into my inventory
        self.user.inventory["map"] = self.reward
        print(f"{self.user.inventory['map']} added in your inventary !")
        print("")
        return self.choose_direction()

    def choose_direction(self):
        print(f"You are at the {self.room_name}.")
        direction = input("In which room you want to go ?: 'FR' 'EM' 'TR' 'EXIT' ")
        if direction == 'FR':
            print("Time to fight")
        if direction == 'EM':
            print("Room is empty")
        if direction == 'TR':
            print("Trap in the room !")
        if direction == 'EXIT':
            input("Do you really want to exit the dungeon ? 'y' 'n' ")
