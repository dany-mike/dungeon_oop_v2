from Rooms.Room import Room


class FightRoom(Room):
    def __init__(self, room_name, user, enemy):
        super().__init__(room_name)
        self.user = user
        self.enemy = enemy
        self.is_gobelin = True
        self.is_key = True

    def start_fight(self, user_name, enemy_name):
        if self.is_gobelin:
            print(f"A fight between {user_name} and {enemy_name} started !")
        else:
            print("There is nothing to do in this room....")