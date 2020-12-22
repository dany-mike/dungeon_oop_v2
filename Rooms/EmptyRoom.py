from Rooms.Room import Room


class EmptyRoom(Room):
    def __init__(self, room_name, user):
        super().__init__(room_name)
        self.user = user

    def v_empty_room(self):
        is_boss_key = "boss_key" in self.user.inventory
        print(f"{self.user.name} enters in the {self.room_name}")
        print("There is a close door in the room")
        print("")
        if is_boss_key:
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

    def find_door(self):
        # Check if user has a key if he has go to the Mini Boss Room.
        is_boss_key = "boss_key" in self.user.inventory
        if not is_boss_key:
            print(f"{self.user.name} goes at the door in the back of the room but she is closed you need a key ....")
            print("")
            print(f"{self.user.name} goes back at the main entrance ....")
            print("")
        if is_boss_key:
            self.open_door()

    def open_door(self):
        while True:
            use_key = input("Do you want to use your key ? 'y' 'n' ")

            if use_key == 'y':
                print(f"{self.user.name} uses {self.user.inventory['key']}")
                # mini_boss_room = MiniBossRoom('Mini Boss Room', self.user, True, 'boss key')
                # mini_boss_room.v_mini_boss_room(DarkUser(f"Dark {self.user.name}", self.user.pv))
                break
            if use_key == 'n':
                print(f"{self.user.name} decides to do nothing. He goes back at the main entrance....")
            else:
                print("Choose an existing choice")
