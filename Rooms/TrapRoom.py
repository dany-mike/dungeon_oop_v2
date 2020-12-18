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

    def v_trap_room(self):
        print(f"{self.user.name} enters in the {self.room_name}")
        self.trap_attack()
