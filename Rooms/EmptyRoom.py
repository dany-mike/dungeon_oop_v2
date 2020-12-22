from Rooms.Room import Room


class EmptyRoom(Room):
    def __init__(self, room_name, user):
        super().__init__(room_name)
        self.user = user

    def v_empty_room(self):
        print(f"{self.user.name} enters in the {self.room_name}")
        print("There is a close door in the room")
        if self.user.inventory['boss_key']:
            while True:
                is_open = input("Do you want to open the door with your key ? 'y' 'n': ")
                if is_open == 'y':
                    print(f"{self.user.name} opens the door")
                    break
                if is_open == 'n':
                    print(f"{self.user.name} does not want to open the door")
                    break
                else:
                    print("Choose an existing choice")
        else:
            print("Seems you need a key to open this door !")
