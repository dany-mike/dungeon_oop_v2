from Rooms.Room import Room
from Enemies.DarkUser import DarkUser
from Rooms.Fight import Fight


class MiniBossRoom(Room):
    dark_user = DarkUser("Dark User", 100)

    def __init__(self, room_name, user, reward, is_dark_user):
        super().__init__(room_name)
        self.user = user
        self.reward = reward
        self.is_dark_user = is_dark_user

    def v_mini_boss_room(self, dark_user):
        print(f"{self.user.name} enters in the Mini Boss room.. ")
        print("")
        # Call Fight instance
        fight = Fight()
        # execute start_fight and end_fight method in Fight.py
        fight.start_fight(self.user, dark_user, self.is_dark_user, self.reward, "boss_key", '', '')
