from Rooms.Room import Room
from Enemies.FireDragon import FireDragon
from Rooms.Fight import Fight


class BossRoom(Room):
    dragon = FireDragon("Goblin", 50)

    def __init__(self, room_name, user, reward):
        super().__init__(room_name)
        self.user = user
        self.reward = reward

    def v_boss_room(self, dragon):
        print(f"{self.user.name} enters in the FR room.. ")
        fight = Fight()
        # execute start_fight and end_fight method in Fight.py
        fight.start_fight(self.user, dragon, True, self.reward, "gold", 'exit key', 'ext_key')
