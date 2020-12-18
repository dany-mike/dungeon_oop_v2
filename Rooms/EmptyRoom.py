from Rooms.Room import Room


class EmptyRoom(Room):
    def __init__(self, room_name):
        super().__init__(room_name)